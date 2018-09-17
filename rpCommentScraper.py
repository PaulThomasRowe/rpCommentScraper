import requests
from bs4 import BeautifulSoup as BS
url = 'https://us.battle.net/forums/en/wow/topic/20768997089'
response = requests.get(url)
html = response.content

def num_appearances_of_tag(TopicPost-bodyContent, html):
    soup = BS(html)
    return len(soup.find_all(TopicPost-bodyContent)



soup = BS(html)
forum = soup.find('div', attrs={'class': 'TopicPost-bodyContent'})
print forum.prettify()
