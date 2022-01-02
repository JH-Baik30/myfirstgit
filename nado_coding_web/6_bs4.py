import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
print(soup.title.get_text())

'''
웹페이지의 정보를 알때 쓰는 방법
soup.a          -> soup 객체에서 처음 발견되는 a 태그를 보여준다.
soup.a.attrs    -> a element 의 속성 정보들을 dict 형태로 보여준다.
soup.a['href']  -> a element 의 href 속성 정보를 보여준다.

잘 모를때
soup.find('a', attrs={'class':'Nbtn_upload'}) # class='Nbtn_upload' 인 a 태그를 찾아라.
soup.find(attrs={'class':'Nbtn_upload'})      # class='Nbtn_upload' 인 태그를 찾아라.
     
'''

# 네이버 웹툰 순위 1인 항목 가져오기
rank1 = soup.find('li', attrs={'class':'rank01'})  # li 태그 안의 class가 rank01인 애덜
print(rank1.a)                                     # 그중에 a 태그만 가져오기


