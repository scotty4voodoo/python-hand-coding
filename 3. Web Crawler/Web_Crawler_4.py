## BS4 로 CSS Selector 찾기
## select_one 사용해보기

# 개발자 도구 -> Inspector 를 통해 원하는 html 위치 찾기
# CSS의 Selector 찾기
# 코드 적용!

# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&ackey=c8nzdwyp'

# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = bs(html,'html.parser')
#     title = soup.select_one('#fdr-2f72aea7e0104d4cae1ec8ce9b5df2dd > div > div > div.sds-comps-vertical-layout.sds-comps-full-layout.fds-web-list-root.fds-web-list-vert-padding > div:nth-child(3) > div.sds-comps-vertical-layout.sds-comps-full-layout.nCV0YMBaPE0SJQAiBleC > div.sds-comps-vertical-layout.sds-comps-full-layout.pxT4aG6o1Bp9mkWSwV4s.CjCkSS7HoRCEfnugZM8P > div.sds-comps-horizontal-layout.sds-comps-full-layout.D2H9UvQxBPUWc0yfYOw5 > a')
#     print(title, "\n")
#     ## text만 뽑아오고 싶을 때에는?
#     print(title.text)
# else:
#     print(response.status_code)

import requests
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?nso=&page=2&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=tab_pge&start=1&where=web'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = bs(html,'html.parser')
    div = soup.select_one('div#fdr-5e85123b5bf4476a8955313895ee0be7')
    print(div)
else:
    print(response.status_code)

#fdr-2f72aea7e0104d4cae1ec8ce9b5df2dd > div