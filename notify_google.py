#!/usr/bin/env python3
"""(선택) 구글 Indexing API 색인 통보 스크립트.

⚠️ 중요 — 솔직한 안내:
  - 구글은 IndexNow 에 참여하지 않습니다. 구글에 즉시 색인을 알리는 공식 통로는
    Indexing API 뿐인데, 이 API 는 공식적으로 JobPosting·BroadcastEvent 페이지에만
    지원됩니다. 그 외 일반 페이지 제출은 보장되지 않으며 권장되지 않습니다.
  - 구글의 sitemap ping 엔드포인트(google.com/ping?sitemap=)는 2023년 폐지됐습니다.
  - 일반 페이지의 가장 확실하고 정책에 맞는 구글 색인 경로는
    Google Search Console 에 sitemap.xml 을 등록하는 것입니다.

따라서 이 스크립트는 "필요할 때만" 쓰는 선택 도구입니다. 빙·네이버는
notify_indexnow.py 로 즉시 통보하고, 구글은 Search Console + sitemap 을 권장합니다.

준비물:
  pip install google-auth
  GCP 서비스 계정 JSON 키 (Indexing API 사용 설정 + Search Console 소유자 등록)

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=service-account.json \\
      python3 notify_google.py <url> [<url> ...]
  (인자 없으면 urls.txt 전체)
"""
import json
import sys
import urllib.request
import urllib.error

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def load_urls(args):
    if args:
        return args
    with open("urls.txt", encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def get_token():
    try:
        import google.auth
        from google.auth.transport.requests import Request
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth")
    creds, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/indexing"]
    )
    creds.refresh(Request())
    return creds.token


def publish(url, token):
    body = json.dumps({"url": url, "type": "URL_UPDATED"}).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  [{resp.status}] {url}")
            return True
    except urllib.error.HTTPError as e:
        print(f"  [{e.code}] {url} — {e.read().decode('utf-8', 'ignore')[:200]}")
        return False


if __name__ == "__main__":
    urls = load_urls(sys.argv[1:])
    token = get_token()
    print(f"구글 Indexing API 로 {len(urls)}건 통보 (URL_UPDATED):")
    ok = sum(publish(u, token) for u in urls)
    print(f"완료: {ok}/{len(urls)}")
    sys.exit(0 if ok == len(urls) else 1)
