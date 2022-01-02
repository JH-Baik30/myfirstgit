import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 가우스전자 제목과 링크 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})
# for cartoon in cartoons:
#   print(cartoon.a.text)
#   link = cartoon.a['href']
#   print('https://comic.naver.com'+link)

# 평점 가져오기
# stars = soup.find_all('div', attrs={'class':'rating_type'})
# for star in stars:
#   print(star.strong.get_text())
  

# 위의 두가지 항목 가져오기
cartoons = soup.find_all('td', attrs={'class':'title'})
stars = soup.find_all('div', attrs={'class':'rating_type'})

# for cartoon, star in zip(cartoons, stars):
#   text = cartoon.a.get_text()
#   link = cartoon.a['href']
#   score = star.strong.get_text()
#   print(text, score)
#   print('https://comic.naver.com'+link)