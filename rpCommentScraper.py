import requests
from bs4 import BeautifulSoup as BS
data=[]
count=0
url = 'https://us.battle.net/forums/en/wow/topic/20768997089'
response = requests.get(url)
html = response.content

soup = BS(html , "lxml")


forum = soup.find_all('div', class_='TopicPost-bodyContent')

for comment in forum:
    comment = comment.text
    print("")
    print(comment)
    print("")