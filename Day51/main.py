from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#---------------Constants---------------------#
chrome_driver_path = 'C:/developer/chromedriver.exe'
DOWNSPEED_P = 100
UPSPEED_P = 8
TWITTER_USERNAME = 'Nawf34236838'
PASSWORD = 'Klugnawf'

class InternetSpeedTwitterBot:
	def __init__(self,driver_path):
		self.driver = webdriver.Chrome(executable_path=driver_path)
		self.up = 0
		self.down = 0

	def get_internet_speed(self):
		self.driver.get('https://www.speedtest.net/')
		sleep(2)
		check_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
		check_button.click()
		sleep(120)
		download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
		self.down = download_speed.text
		upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
		self.up = upload_speed.text


	def tweer_at_provider(self,TWITTER_USERNAME,PASSWORD):
		self.driver.get('https://twitter.com/')
		sleep(2)
		sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span').click()
		sleep(2)
		use_email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a').click()
		sleep(4)
		username_entry= self.driver.find_element_by_name('username')
		username_entry.send_keys(TWITTER_USERNAME)
		sleep(2)
		username_entry.send_keys(Keys.ENTER)
		sleep(4)
		password_entry = self.driver.find_element_by_name('password')
		password_entry.send_keys(PASSWORD)
		sleep(1)
		password_entry.send_keys(Keys.ENTER)
		sleep(4)
		tweet_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
		tweet_box.send_keys(f'Dear Internet provider, How can my internet speed is {self.down}Down/{self.up}Up while I am paying for 100down/8up? ')
		sleep(1)
		tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()




bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweer_at_provider(TWITTER_USERNAME,PASSWORD)
		