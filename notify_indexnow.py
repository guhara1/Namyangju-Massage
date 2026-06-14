#!/usr/bin/env python3
"""IndexNow 색인 통보 스크립트 — 빙·네이버·얀덱스에 즉시 색인 요청.

IndexNow 는 하나의 엔드포인트(api.indexnow.org)로 제출하면 참여 검색엔진
(Bing, Naver, Yandex, Seznam)에 동시에 전달된다. 글을 올리거나 수정할 때마다
실행하면 가장 빠르게 색인 통보가 이루어진다.

사용법:
  python3 build.py                     # 먼저 빌드 (urls.txt·키 파일 생성)
  python3 notify_indexnow.py           # urls.txt 의 전체 URL 통보
  python3 notify_indexnow.py <url> ... # 특정 URL만 통보 (글 1건 올렸을 때)

GitHub Actions/배포 훅에서 배포 직후 호출하면 자동화된다.
"""
import json
import sys
import urllib.request
import urllib.error
from urllib.parse import urlsplit

sys.path.insert(0, ".")
from content.site import BASE_URL, INDEXNOW_KEY

ENDPOINT = "https://api.indexnow.org/indexnow"
HOST = urlsplit(BASE_URL).netloc
KEY_LOCATION = f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt"


def load_urls(args):
    if args:
        return args
    try:
        with open("urls.txt", encoding="utf-8") as f:
            return [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        sys.exit("urls.txt 가 없습니다. 먼저 python3 build.py 를 실행하세요.")


def submit(urls):
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow 응답: HTTP {resp.status} (URL {len(urls)}건 제출)")
            # 200/202 = 정상 접수. 키 파일이 배포된 뒤 실행해야 한다.
            return 0 <= resp.status < 300
    except urllib.error.HTTPError as e:
        print(f"IndexNow 오류: HTTP {e.code} — {e.read().decode('utf-8', 'ignore')}")
        return False
    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e.reason}")
        return False


if __name__ == "__main__":
    urls = load_urls(sys.argv[1:])
    print(f"host={HOST}  key={INDEXNOW_KEY[:8]}…  대상 {len(urls)}건")
    ok = submit(urls)
    sys.exit(0 if ok else 1)
