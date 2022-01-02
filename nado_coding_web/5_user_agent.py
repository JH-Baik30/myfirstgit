# https://www.whatismybrowser.com/detect/what-is-my-user-agent
# 웹에서 접근을 막았을때 필요한 코드를 가져올 수 있다.
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36

import requests

url = "http://nadocoding.tistory.com"
res = requests.get(url)
res.status_code

with open('nadoti.html', 'w', encoding='utf8') as f:
  f.write(res.text)

# 영상처럼 안되야 되는데, 잘되서 패쓰.. ???