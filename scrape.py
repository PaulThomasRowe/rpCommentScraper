import requests
from bs4 import BeautifulSoup as BS
url = 'https://us.battle.net/forums/en/wow/topic/20768997089'
response = requests.get(url)
html = response.content

soup = BS(html , "lxml")
forum = soup.find_all('div', class_='TopicPost-bodyContent')

print(forum)
