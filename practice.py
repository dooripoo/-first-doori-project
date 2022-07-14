import requests
from bs4 import BeautifulSoup

base_url = "https://news.google.com"
# search_url = base_url + "/search?q=%EC%86%8D%EB%B3%B4&rlz=1C1NHXL_koKR987KR987&ie=UTF-8"
search_url = "https://www.google.com/search?q=%EC%86%8D%EB%B3%B4&rlz=1C1NHXL_koKR987KR987&oq=%EC%86%8D%EB%B3%B4&sourceid=chrome&ie=UTF-8"
res = requests.get(search_url)
html_src = res.text
soup = BeautifulSoup(html_src, 'html.parser')

#
news_items = soup.select('div id="search"')
print(len(news_items))
print(soup)



