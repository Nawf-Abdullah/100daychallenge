from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
contents = response.text


soup = BeautifulSoup(contents,'html.parser')
tags = soup.find_all(name='h3',class_='jsx-4245974604')
#<div class="jsx-4245974604 listicle-item-content"><p><strong>1997</strong><br>
for tag in tags:
	print(tag)