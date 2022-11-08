import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://library.gabia.com/")
soup = bs(page.text, "html.parser")

elements = soup.select('div.esg-entry-content a > span')

for index, element in enumerate(elements, 1):
		print("{} 번째 게시글의 제목: {}".format(index, element.text))
  
  
  
# 가비아 라이브러리 홈페이지에 존재하는 포스터들의 제목과 링크  
page = requests.get("https://library.gabia.com/")
soup = bs(page.text, "html.parser")

elements = soup.select('div.esg-entry-content a.eg-grant-element-0')

for index, element in enumerate(elements, 1):
		print("{} 번째 게시글: {}, {}".format(index, element.text, element.attrs['href'])) 