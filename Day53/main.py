from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from time import *

form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSeJ4GbjvOg1DW7WOQ8p7eFeEA5DMnii7hElmHAs_IQqWq-Mpg/viewform?usp=sf_link'
house_website_link = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
ACCEPT_LANGUAGE = 'en-IN,en;q=0.9'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'

#-------------------------------------------------Getting Data ------------------------------------------------------------------------#
headers={
	'Accept-Language':ACCEPT_LANGUAGE,
	'User-Agent':USER_AGENT
}
class Research:
	def __init__(self):
		self.response = requests.get(house_website_link,headers= headers)
		self.contents = self.response.text
		self.soup = BeautifulSoup(self.contents,'html.parser')

	def scrape(self):
		addrs = self.soup.find_all(name='address',class_="list-card-addr")
		price_obs = self.soup.find_all(name='div',class_='list-card-price')
		loc = self.soup.select('.list-card-top a')
		self.links = [link['href'] for link in loc]
		self.address_list = [addr.getText() for addr in addrs]
		self.prices = [link.getText() for link in price_obs]
		sleep(2)

	def save(self):
		self.driver = webdriver.Chrome(executable_path='C:/developer/chromedriver.exe')
		sleep(2)
		#self.driver.get(form_link)
		#sleep(4)
		#self.address_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
		#self.price_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
		#self.link_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
		#submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
		
		for n in range(len(self.prices)):
			self.driver.get(form_link)
			sleep(4)
			self.address_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
			self.price_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
			self.link_label = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
			submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
			sleep(2)
			self.address_label.send_keys(self.address_list[n])
			sleep(1)
			self.price_label.send_keys(self.prices[n])
			sleep(1)
			self.link_label.send_keys(self.links[n])
			sleep(1)
			submit_btn.click()
			
			




research = Research()
research.scrape()
sleep(2)
research.save()
print('Done')