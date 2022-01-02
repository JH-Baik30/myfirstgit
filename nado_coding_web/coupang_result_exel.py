'''
쿠팡에서 노트북으로 검색.

1. 주소 가져오기
2. User-Agent 로 자동화 블럭 뚫기
3. 제품명, 가격, 평점, 평가수 가져오기
4. 광고상품, Apple 제품, 평점이 없거나, 평가 수가 없는 제품은 제외하고 가져오기
5. 이제 여러페이지에서 상품 정보 가져오기 (5페이지)
ps. https://datalabbit.tistory.com/24 를 참고로 exel 저장
살이 붙어 갈수록 점점 길어진다. ^^
'''

import  requests
from bs4 import BeautifulSoup
import openpyxl                  # 엑셀 저장 모듈

wb = openpyxl.Workbook()         # 엑셀 저장관련
sheet = wb.active                # 상동

# user agent 값 가져와서 붙이기
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

for i in range(1, 5+1):
  print(f'{i} 페이지')
  url = f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=5&backgroundColor='


  res =requests.get(url, headers=headers)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, 'lxml')

  items = soup.find_all('li', attrs={'class':'search-product'})
  for j, item in enumerate(items):
    # 광고 제품 태그
    ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
    if ad_badge:
      # csvWriter.writerow(' <광고 상품 제외합니다.')
      # print(' <광고 상품 제외합니다.')
      continue
    
    # 상품명 가져오기
    name = item.find('div', attrs={'class':'name'}).get_text()
    
    # 애플 제품 제외
    if 'Apple' in name:
      # csvWriter.writerow('< Apple 상품 제외합니다.')
      # print('< Apple 상품 제외합니다.')
      continue
    
    # 링크 가져오기
    link = item.find('a', attrs={'class':'search-product-link'})['href']
    
    # 상품가격 가져오기
    price = item.find('strong', attrs={'class':'price-value'}).get_text()
    
    # 평점이 없으면 다음 item 으로 넘어간다.
    rate = item.find('em', attrs={'class':'rating'})
    if rate:
      rate = rate.get_text()
    else:
      # csvWriter.writerow(' < 평가가 없는 상품입니다.')
      # print(' < 평가가 없는 상품입니다.')
      continue
    
    # 평점수가 없으면 다음 item 으로 넘어간다.
    rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
    if rate_cnt:
      rate_cnt = rate_cnt.get_text()[1:-1]
          
    else:
      # csvWriter.writerow(' < 평점 수가 없습니다.')
      # print(' < 평점 수가 없습니다.')
      continue
    
    # 리뷰 100 개 이상, 평점 4.5 이상 되는 것만 출력
    if float(rate) >=4.5 and int(rate_cnt) >= 100:
      sheet.append([name, 'https://www.coupang.com'+link, price, rate, rate_cnt])   # 엑셀 저장관련
      
wb.save('note.xlsx')   # 최종 엑셀 저장
    
print('save complete')