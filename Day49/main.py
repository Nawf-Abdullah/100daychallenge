from selenium import webdriver
from time import sleep

email = 'nawfabdullah2711@gmail.com'
password = 'Klugnawf'

driver = webdriver.Chrome('C:/developer/chromedriver.exe')
driver.get('https://www.linkedin.com/')
sleep(2)
first_btn = driver.find_element_by_css_selector('.nav__button-secondary')
first_btn.click()
sleep(2)
email_input =driver.find_element_by_css_selector('#username')
email_input.send_keys(email)

sleep(2)
password_input =driver.find_element_by_css_selector('#password')
password_input.send_keys(password)
sleep(2)
sign_in_btn = driver.find_element_by_css_selector('.login__form_action_container button')
sign_in_btn.click()
driver.get('https://www.linkedin.com/jobs/view/2747229622/?eBP=JOB_SEARCH_ORGANIC&refId=AYMc0%2BK54IQbJOubcagAGg%3D%3D&trackingId=YRK3g45TSMhmKY8h3bQyAA%3D%3D')

sleep(2)

#easy_apply = driver.find_element_by_xpath('//*[@id="ember102"]')
#easy_apply.click()

sleep(5)

apply_now = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/div/button[2]')
apply_now.click()
