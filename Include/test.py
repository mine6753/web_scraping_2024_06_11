# requests: 파이썬 HTTP 라이브러리(HTTP, HTTPS 웹 사이트 요청)
# 웹 스크래핑 과정에서 requests 모듈을 이용해서 소스코드 파싱
import requests

# HTML 정보로부터 원하는 데이터를 쉽게 가져오는 라이브러리
from bs4 import BeautifulSoup

# 웹사이트 URL 설정
url = "https://news.naver.com/section/101"

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url)

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 태그 찾기
# find(), find_all()
news_titles = soup.find_all("strong", class_="sa_text_strong")
news_body = soup.find_all("div", class_="sa_text_press")

# 출력
print(news_titles)
print(news_body)

# news_titles에서 headline만 출력
for headline in news_titles:
  print(headline.text)

# news_titles에서 body만 출력
for body in news_body:
  print(body.text)