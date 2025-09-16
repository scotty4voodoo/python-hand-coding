# 정적 페이지에 대한 웹 크롤링 연습
# 웹 크롤링 절차는 다음과 같습니다.
# 1. 원하는 웹 페이지의 html 문서 내용을 다 가져온다
# 2. 긁어온 html 문서를 파싱 (Parsing) 한다
# 3. 파싱한 문서에서 원하는 내용을 골라서 사용한다.

##1. requests 사용하기
## requests 설치 : pip install requests

# 모듈 불러오기
import requests

# 불러올 웹 url 지정
url = "https://www.naver.com"

# get 메소드로 해당 url에서 웹 페이지 읽어오기
response = requests.get(url)
# print(response)

# 읽어온 내용을 text 로 저장
html_text = response.text

# print(html_text)





