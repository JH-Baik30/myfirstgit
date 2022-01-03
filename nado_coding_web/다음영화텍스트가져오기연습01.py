'''
미 완료 과제
xpath를 활용해봅시다.
제    목 = //*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/div/a
평    점 = //*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/dl[1]/dd[1]/em
개봉일   = //*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/dl[2]/dd
관람객수 = //*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/dl[3]/dd
누적관객 = //*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/dl[4]/dd
'''

import requests
from bs4 import BeautifulSoup

for i in range(2020, 2014, -1):
  url = f'https://search.daum.net/search?w=tot&q=20{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')
  movies = soup.find('div', attrs={'class':'mg_cont'})
  print(f'{i}년도 5순위')
  titles = movies.find_all('a', attrs={'class':'tit_main'})
  for i, title in enumerate(titles):
    if i <= 4:
      print(title.get_text())
