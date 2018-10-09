import requests
import random
from bs4 import BeautifulSoup as BS
data=[]
post=[]
count=0
max=0
sectionUrl = 'https://us.battle.net/forums/en/wow/1011637/'
url = 'https://us.battle.net/forums/en/wow/topic/20768997089'
response = requests.get(sectionUrl)
html = response.content

soup = BS(html , "lxml")


section = soup.find_all('a', class_='ForumTopic')

for links in section:
    data.append(links.get('href'))

max=len(data)

chosen = random.randint(1,max+1)

url = data[chosen]
url = "https://us.battle.net"+url


response = requests.get(url)
html = response.content

soup = BS(html , "lxml")

forum = soup.find_all('div', class_='TopicPost-bodyContent')

for comment in forum:
    post.append(comment.text)

max=len(post)

chosen = random.randint(1,max)

if max<=0:
    print("No posts")
else:
    print(post[chosen])