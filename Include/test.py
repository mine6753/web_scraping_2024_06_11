# requests: 파이썬 HTTP 라이브러리(HTTP, HTTPS 웹 사이트 요청)
# 웹 스크래핑 과정에서 requests 모듈을 이용해서 소스코드 파싱
import requests

# HTML 정보로부터 원하는 데이터를 쉽게 가져오는 라이브러리
from bs4 import BeautifulSoup

# pandas import로 불러오기
import pandas as pd

# 웹사이트 URL 설정
url = "https://news.naver.com/section/101"

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url)

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 태그 찾기
# find(), find_all()
news_title = soup.find_all("strong", class_="sa_text_strong")
#news_body = soup.find_all("div", class_="sa_text_press")

# 출력
print(news_title)
#print(news_body)

# append() 통해 담을 빈 리스트 생성
news_titles = []

# news_titles에서 headline만 출력
for headline in news_title:
  news_titles.append(headline.text)

# news_titles에서 body만 출력
#for body in news_body:
#  body.append(body.text)

new_title_list = {"뉴스제목":news_titles }

# 엑셀을 저장할 위치와 데이터 넣기
df = pd.DataFrame(new_title_list)
df.to_excel("C:/Users/user/Desktop/pythonProjects/finals/뉴스제목.xlsx", index=False)

