# 지하철역·철도역 17개 페이지 집계.
# 역 이름만 바꾼 반복/노선·방향별 중복 페이지는 만들지 않는다. 별내역은 환승역이지만 1개 페이지로만 처리한다.
from .stations_g1 import PAGES as _G1
from .stations_g2 import PAGES as _G2
from .stations_g3 import PAGES as _G3

PAGES = _G1 + _G2 + _G3
