###########################################################################################################

##2. BS4 로 html 문서에서 원하는 내용만 가져오기 (Parsing)
## bs4 설치 : pip install beautifulsoup4
# step1. request, bs4 모듈 불러오기

import requests
from bs4 import BeautifulSoup as bs

# step2. 추출하고자 하는 페이지 내 컨텐츠 찾기

url = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nx&ssc=tab.nx.all&query=%EB%AF%B8%EA%B5%AD+%EC%86%8C%EB%B9%84%EC%9E%90%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98&oquery=%EC%B6%94%EC%84%9D&tqi=jKBuhlqVOswss446euKssssssbG-185783&acq=%EB%AF%B8%EA%B5%AD+%EC%86%8C%EB%B9%84%EC%9E%90&acr=1&qdt=0&ackey=9hzwrkm3'


# step4. requests 패키지를 이용해 'url'의 html 문서 가져오기

response = requests.get(url)

html_text = response.text

soup = bs(response.text,'html.parser')

# print(soup)

## step 5 원하는 내용 추출
value = soup.find("strong",{"class":"num"})
print(value)

value2 = value.text.strip()
print(value2[0:4])