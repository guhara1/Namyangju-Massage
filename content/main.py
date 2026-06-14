# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import (AREAS, BASE_URL, BRAND, PHONE, PHONE_DISPLAY, STATIONS,
                   area_url, station_url)
from .pricing import PRICING

_AREA_CARDS = "".join(
    f'<li><a href="{area_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in AREAS
)
_STATION_CARDS = "".join(
    f'<li><a href="{station_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in STATIONS
)

_JSONLD = f"""<meta name="naver-site-verification" content="60db34c2e8adccdcaf51e8d9732fde69cebf3f09">
<link rel="preload" as="image" href="/assets/hero.webp" type="image/webp" fetchpriority="high">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "경기도 남양주시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 남양주시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "남양주시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "와부읍, 진접읍, 화도읍, 진건읍, 오남읍, 퇴계원읍과 별내면, 수동면, 조안면, 그리고 호평동·평내동·금곡동·양정동·다산동·별내동 등 읍·면·대표 행정동을 기준으로 남양주시 전지역을 안내합니다. 수동면·조안면 같은 외곽 지역은 차량 이동 기준으로 가능 여부를 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "다산1동과 다산2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "다산1동·다산2동은 다산동 대표 페이지로 통합해 중복 페이지 위험을 줄였습니다. 다산역·도농역 생활권을 한 페이지에서 함께 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "별내역은 경춘선·8호선 페이지가 따로 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "별내역은 경춘선과 8호선 별내선이 만나는 환승역이지만 노선별로 페이지를 나누지 않고 별내역 출장마사지 1개 페이지로 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "외곽 지역은 추가 이동비가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "수동면, 조안면처럼 이동 거리가 먼 외곽 지역은 추가 이동비가 발생할 수 있으며, 예약 시 총비용으로 먼저 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "지하철역 주변도 예약할 수 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "다산역, 별내역, 평내호평역, 마석역, 덕소역, 진접역 등 남양주를 지나는 8호선·경춘선·진접선·경의중앙선 역세권은 지하철역별 안내 페이지에서 주변 생활권과 함께 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner hero-grid">
    <div class="hero-text">
      <p class="hero-badge">Premium Visiting Spa · 경기도 남양주시 전지역</p>
      <h1>남양주 출장마사지·남양주시 홈타이<br>지역별 예약 안내</h1>
      <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>남양주시 읍·면·동 어디든 전화 한 통이면 예약이 끝납니다.</p>
      <div class="hero-actions">
        <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
        <a class="hero-btn" href="#areas">지역별 안내 보기</a>
      </div>
      <ul class="hero-stats">
        <li><strong>15곳</strong><span>읍·면·대표 동</span></li>
        <li><strong>17개</strong><span>지하철·철도역</span></li>
        <li><strong>전지역</strong><span>방문 가능</span></li>
        <li><strong>24시간</strong><span>예약 상담</span></li>
      </ul>
    </div>
    <div class="hero-media">
      <picture>
        <source srcset="/assets/hero.webp" type="image/webp">
        <img src="/assets/hero.jpg" alt="남양주 출장마사지·남양주시 홈타이 방문 관리 안내" width="1200" height="675" fetchpriority="high" decoding="async">
      </picture>
    </div>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>남양주시에서 출장마사지를 찾는 이유</h2>
<p>남양주 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 남양주시는 서울 동북권과 구리, 하남, 포천, 가평, 양평 생활권과 연결되는 넓은 도시입니다. 다산동과 별내동은 신도시 주거 수요가 많고, 평내동과 호평동은 경춘선 생활권을 중심으로 움직입니다. 와부읍과 조안면은 한강과 경의중앙선 생활권이 강하고, 진접읍과 오남읍은 4호선 진접선 역세권을 기준으로 검색 의도가 나뉩니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 이 페이지는 남양주 전체 구조를 설명하는 허브 역할을 합니다. 더 자세한 내용은 읍·면·대표 행정동 페이지와 지하철역·철도역 페이지에서 확인하실 수 있습니다.</p>
<p>남양주시는 고양시처럼 행정구가 있는 도시가 아니기 때문에, 이 사이트는 메인 아래에 바로 읍·면·대표 행정동 페이지를 배치합니다. 행정구를 억지로 만들지 않고 실제 생활권을 기준으로 구성하는 편이 자연스럽고, 사용자가 본인 위치를 더 빨리 찾을 수 있습니다.</p>
</section>

<section id="coverage">
<h2>남양주 홈타이 이용 전 확인할 사항</h2>
<p>남양주 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 와부읍, 진접읍, 화도읍, 진건읍, 오남읍, 퇴계원읍, 별내면, 수동면, 조안면, 호평동, 평내동, 금곡동, 양정동, 다산동, 별내동을 각각 대표 지역으로 두고, 페이지마다 생활권과 이동 기준을 다르게 설명합니다. 번호가 붙은 행정동은 개별 페이지로 만들지 않습니다. 다산1동과 다산2동은 다산동으로 통합해 중복 콘텐츠 위험을 줄였습니다. 이렇게 구성하면 페이지 수를 무리하게 늘리지 않으면서도 남양주시 전체 지역을 충분히 커버할 수 있습니다.</p>
</section>

<section id="areas">
<h2>읍·면·대표 행정동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 남양주시 읍·면·대표 행정동 15곳을 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역, 방문 전 확인사항, 예약 가능 시간, 추가 이동비 여부를 지역마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 지역을 선택해 주세요.</p>
<ul class="card-grid">
{_AREA_CARDS}
</ul>
<p>다산동·별내동은 신도시 주거 생활권을, 호평동·평내동은 평내호평역 경춘선 생활권을, 와부읍·조안면은 한강과 경의중앙선 생활권을, 진접읍·오남읍은 진접선 역세권을, 수동면은 차량 이동 기준 외곽 지역을 중심으로 안내합니다.</p>
</section>

<section id="stations">
<h2>지하철역·철도역별 지역 SEO 구조</h2>
<p>지하철역과 철도역 페이지는 남양주 지역 SEO에서 중요한 역할을 합니다. 8호선 별내선의 다산역·별내역, 경춘선의 평내호평역·마석역·별내역, 진접선의 오남역·진접역, 경의중앙선의 덕소역·팔당역·운길산역처럼 실제 검색어와 가까운 제목을 사용해 검색 의도를 분명히 합니다. 같은 역을 노선별로 중복해서 만들지 않으며, 별내역은 경춘선과 8호선 환승역이지만 1개 페이지로만 안내합니다.</p>
<ul class="card-grid">
{_STATION_CARDS}
</ul>
<p>8호선 별내선은 2024년 8월 10일 개통되어 남양주 구간에 다산역·별내역이 포함됩니다. 개통 전 예정역인 왕숙역·풍양역은 단독 색인 페이지를 만들지 않고, 별내선 연장 이슈는 별내동·별내역 본문에서 보조 설명으로 다룹니다.</p>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 남양주시는 도시 면적이 넓어 다산동·별내동 같은 신도시 생활권과 조안면·수동면 같은 외곽 생활권의 이동 시간이 크게 다를 수 있습니다. 특히 차량 이동 지역은 추가 이동비 여부와 예약 가능 시간을 명확히 안내해야 하므로, 자세한 준비 방법은 <a href="/precautions/">이용 전 확인사항</a>에서, 예약 절차와 결제·이동비 안내는 <a href="/reservation/">예약안내</a>에서 확인해 주세요. 홈타이가 처음이라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>를 함께 보시면 도움이 됩니다.</p>
</section>

<section id="guide">
<h2>남양주 출장마사지 사이트 이용 가이드</h2>
<p>메인페이지는 남양주시 전체 안내를 담당하고, 읍·면·대표 행정동 페이지는 세부 지역 검색을, 역세권 페이지는 다산역·별내역·평내호평역·마석역·덕소역·진접역처럼 실제 검색 수요가 생길 수 있는 키워드를 담당합니다. 거주 지역이 익숙하면 행정동 페이지를, 역 기준 위치가 익숙하면 역세권 페이지를 보시면 됩니다. 어느 페이지를 보셔도 예약 절차와 비용 기준은 동일하며, 최종 안내는 언제나 정확한 주소를 기준으로 이루어집니다. 과장된 표현이나 허위 후기, 불법·선정적인 안내는 사용하지 않으며, 이용 가능 지역과 예약 절차, 취소 기준, 개인정보 처리 기준을 분명하게 보여드리는 것을 원칙으로 합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>남양주시 전지역 방문이 가능한가요?</h3>
<p>읍·면·대표 행정동 15곳과 지하철역·철도역 17곳을 기준으로 남양주시 전지역을 안내합니다. 수동면·조안면 같은 외곽 지역은 차량 이동 기준으로 가능 여부를 확인합니다.</p>
</div>
<div class="faq-item">
<h3>다산1동·다산2동처럼 번호 동은 왜 페이지가 없나요?</h3>
<p>다산1·2동은 다산동 대표 페이지에서 통합 안내합니다. 같은 생활권을 나눠 반복 설명하지 않기 위해서입니다.</p>
</div>
<div class="faq-item">
<h3>별내역은 경춘선·8호선 페이지가 따로 있나요?</h3>
<p>별내역은 경춘선과 8호선 별내선 환승역이지만, 노선별로 나누지 않고 별내역 출장마사지 1개 페이지로 안내합니다.</p>
</div>
<div class="faq-item">
<h3>외곽 지역은 추가 이동비가 붙나요?</h3>
<p>수동면, 조안면처럼 이동 거리가 먼 지역은 추가 이동비가 발생할 수 있습니다. 예약 시 총비용으로 먼저 안내해 드립니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>남양주 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "남양주 출장마사지｜남양주시 홈타이 지역별 예약 안내",
    "desc": "남양주 출장마사지·홈타이 예약 전 읍면동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "남양주 출장마사지 · 남양주시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
