# vrp-songpha

Route finding for checking Songpha-gu's facilities using VRP
  
VRP 알고리즘을 활용한 송파구 제설함 점검 최적 경로 찾기

![thumbnail](/ex.png)

## 목적

1. 폭설 대비 송파구 내에 제설함 점검을 위한 최적의 경로를 찾습니다.
2. 제설제 보관기지의 적절한 장소를 제시합니다.

## 데이터
- 서울시 제설함 위치정보 (서울 열린데이터 광장(공공데이터))
- 송파구청 좌표 (국토정보플랫폼)
> 좌표계는 GRS80TM으로, 최소 x,y값을 참조
- (참고) 2020/21 겨울철 제설대책 추진실태 점검 결과 보고 (송파구청)

## 주요 기능

1. TSP 알고리즘을 이용한 단일 인원의 제설함 점검 경로 찾기 (`2_tsp.py`)
2. VRP 알고리즘을 이용한 다 인원의 제설함 점검 경로 찾기 (`3_vrp.py`)
3. 휴리스틱으로 제설함을 최대 포용하는 제설제 보관기지 위치 제시 (`4_p-center.py`)
