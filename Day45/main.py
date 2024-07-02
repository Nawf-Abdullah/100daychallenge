from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

account_sid = "ACd2651fd38ae527658b17f48ad80d37cd"
auth_token = "a9d3bdb432e3c5a6c9372b55b3ebadc7"

#with open('website.html','rb') as file:
#	contents = file.read()
#
#soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title)
response = requests.get('https://news.ycombinator.com/news')
contents = response.text

soup = BeautifulSoup(contents,'html.parser')
anchor_tags = soup.find_all(name='a',class_ = 'storylink')
upvote_tags = [int(i.getText().replace(' points','')) for i in soup.find_all(name='span',class_='score')]
print(upvote_tags)
article_texts = []
article_links = []
for anchor in anchor_tags:
	article_texts.append(anchor.getText())
	article_links.append(anchor.get('href'))





position = upvote_tags.index(max(upvote_tags))
max_article = article_texts[position]
print(max_article)

client = Client(account_sid, auth_token)

message = client.messages \
.create(
	body=f"{max_article}\n {article_links[position]} 😊😊",
    from_='+13312535780',
    to='+919894965489'
    )
print(message.status)