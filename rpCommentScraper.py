import requests
from BeautifulSoup import BeautifulSoup
url = 'https://us.battle.net/forums/en/wow/topic/20768997089'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
forum = soup.find('div', attrs={'class': 'TopicPost-bodyContent'})
print forum.prettify()
