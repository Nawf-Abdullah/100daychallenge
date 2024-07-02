from selenium import webdriver
from time import *

driver = webdriver.Chrome('C:/developer/chromedriver.exe')

'''
driver.get('https://www.python.org/')

events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
dates  = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')

#print(dates)
#print(events)
event_list = [i.text for i in events]
dates_list = [j.text for j in dates]

required_dict = dict(zip(dates_list,event_list))
print(required_dict)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
sleep(3)
number_el = driver.find_element_by_css_selector('#articlecount a')
sleep(2)
number_el.click()
print(number_el.text)
'''
'''
driver.get('http://secure-retreat-92358.herokuapp.com/')
sleep(3)
First_el = driver.find_element_by_name('fName')
First_el.send_keys('Nawf')
sleep(1)
Last_el = driver.find_element_by_name('lName')
Last_el.send_keys('Abdullah')

sleep(1)
email_el = driver.find_element_by_name('email')
email_el.send_keys('valimama1@pulip.com')

sleep(1)
button_el = driver.find_element_by_css_selector('button')
button_el.click()
sllep(10)
'''
driver.get('http://orteil.dashnet.org/experiments/cookie/')
sleep(5)
x = driver.find_element_by_xpath('//*[@id="cookie"]')

timeout = time() + 60*5 
while True:
    test = 0
    x.click()

    if test == 5 or time() > timeout:
        break
    test = test - 1

driver.quit()
