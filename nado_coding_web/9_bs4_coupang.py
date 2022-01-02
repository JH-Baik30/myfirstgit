'''
쿠팡에서 노트북으로 검색.

1. 주소 가져오기
2. User-Agent 로 자동화 블럭 뚫기
3. 제품명, 가격, 평점, 평가수 가져오기
4. 광고상품, Apple 제품, 평점이 없거나, 평가 수가 없는 제품은 제외하고 가져오기
5. 이제 여러페이지에서 상품 정보 가져오기 (5페이지)
'''

import  requests
from bs4 import BeautifulSoup

# requests 모듈의 헤더를 이용해서 크롤링을 막는 것을 풀어본다.
url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor='

# user agent 값 가져와서 붙이기
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# requests 에서 위의 헤더를 붙여서 url을 가져온다.
res =requests.get(url, headers=headers)
res.raise_for_status()

# 'lxml' 이 'html.parser' 보다 빠르다.
soup = BeautifulSoup(res.text, 'lxml')

# li 태그의 class 값으로 목록을 가져온다.
items = soup.find_all('li', attrs={'class':'search-product'})
for i, item in enumerate(items):
  # 광고 제품은 제외(순위와 상관없이 제일 위로 올라오기 때문에)
  ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
  if ad_badge:
    print(' <광고 상품 제외합니다.')
    continue
  
  # 상품명 가져오기
  name = item.find('div', attrs={'class':'name'}).get_text()
  
  # 애플 제품 제외
  if 'Apple' in name:
    print('< Apple 상품 제외합니다.')
    continue
  
  # 상품가격 가져오기
  price = item.find('strong', attrs={'class':'price-value'}).get_text()
  
  # 평점이 없으면 다음 item 으로 넘어간다.
  rate = item.find('em', attrs={'class':'rating'})
  if rate:
    rate = rate.get_text()
  else:
    print(' < 평가가 없는 상품입니다.')
    continue
  
  # 평점수가 없으면 다음 item 으로 넘어간다.
  rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
  if rate_cnt:
    rate_cnt = rate_cnt.get_text()  # (숫자) 형식으로 가져오므로
    rate_cnt = rate_cnt[1:-1]       # 1번부터 -1까지(뒤에서 2번째까지) 인덱싱
    # print('리뷰 수', rate_cnt)
  else:
    print(' < 평점 수가 없습니다.')
    continue
  
  # 리뷰 100 개 이상, 평점 4.5 이상 되는 것만 출력
  if float(rate) >=4.5 and int(rate_cnt) >= 100:
    print(i, name, price, rate, rate_cnt)
  
# 광고 상품 제외하기