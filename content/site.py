# 사이트 공통 설정
# 배포 도메인: Cloudflare Pages
BASE_URL = "https://namyangju-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# IndexNow 키 — 빙·네이버·얀덱스 즉시 색인 통보용. 루트에 {KEY}.txt 키 파일이 생성된다.
INDEXNOW_KEY = "d3c8484a0f8c835b5d83afa526179272"

# 읍·면·대표 행정동 15곳 (slug, 한글명) — 내부링크·메뉴 공용
# 번호 행정동(다산1·2동)은 개별 페이지를 만들지 않고 대표 동(다산동)으로 통합한다.
AREAS = [
    ("wabu-eup-chuljangmassage", "와부읍"),
    ("jinjeop-eup-chuljangmassage", "진접읍"),
    ("hwado-eup-chuljangmassage", "화도읍"),
    ("jingeon-eup-chuljangmassage", "진건읍"),
    ("onam-eup-chuljangmassage", "오남읍"),
    ("toegyewon-eup-chuljangmassage", "퇴계원읍"),
    ("byeollae-myeon-chuljangmassage", "별내면"),
    ("sudong-myeon-chuljangmassage", "수동면"),
    ("joan-myeon-chuljangmassage", "조안면"),
    ("hopyeong-dong-chuljangmassage", "호평동"),
    ("pyeongnae-dong-chuljangmassage", "평내동"),
    ("geumgok-dong-chuljangmassage", "금곡동"),
    ("yangjeong-dong-chuljangmassage", "양정동"),
    ("dasan-dong-chuljangmassage", "다산동"),
    ("byeollae-dong-chuljangmassage", "별내동"),
]

# 지하철역·철도역 17곳 (slug, 한글명)
# 예정역(왕숙역·풍양역)은 단독 페이지를 만들지 않는다. 별내역은 경춘선·8호선 환승역이지만 1개 페이지로만 처리한다.
STATIONS = [
    ("dasan-station-chuljangmassage", "다산역"),
    ("byeollae-station-chuljangmassage", "별내역"),
    ("byeollae-byeolgaram-station-chuljangmassage", "별내별가람역"),
    ("onam-station-chuljangmassage", "오남역"),
    ("jinjeop-station-chuljangmassage", "진접역"),
    ("donong-station-chuljangmassage", "도농역"),
    ("yangjeong-station-chuljangmassage", "양정역"),
    ("deokso-station-chuljangmassage", "덕소역"),
    ("dosim-station-chuljangmassage", "도심역"),
    ("paldang-station-chuljangmassage", "팔당역"),
    ("ungilsan-station-chuljangmassage", "운길산역"),
    ("toegyewon-station-chuljangmassage", "퇴계원역"),
    ("sareung-station-chuljangmassage", "사릉역"),
    ("geumgok-station-chuljangmassage", "금곡역"),
    ("pyeongnae-hopyeong-station-chuljangmassage", "평내호평역"),
    ("cheonmasan-station-chuljangmassage", "천마산역"),
    ("maseok-station-chuljangmassage", "마석역"),
]


def area_url(slug):
    return f"/namyangju/{slug}/"


def station_url(slug):
    return f"/namyangju/{slug}/"


# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/#service", [
        ("서비스 안내", "/#service"),
        ("전지역 방문 가능", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("지역별 안내", "/#areas", [
        (name, area_url(slug)) for slug, name in AREAS
    ]),
    ("지하철역별 안내", "/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("외곽 지역 이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
