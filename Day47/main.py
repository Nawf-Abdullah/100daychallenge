from bs4 import BeautifulSoup
import requests
import smtplib

#-----------------------------------------------CONSTANTS------------------------------------------------------------------------------#
MY_EMAIL = "hungrypy6@gmail.com"
MY_PASSWORD = "klugnawf"
TARGET_PRICE    =  10000
ACCEPT_LANGUAGE = 'en-IN,en;q=0.9'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'

#-------------------------------------------------Getting Data ------------------------------------------------------------------------#
headers={
	'Accept-Language':ACCEPT_LANGUAGE,
	'User-Agent':USER_AGENT
}
product_url = 'https://www.amazon.com/Xperia-III-Smartphone-display-lengths/dp/B091YC2SJZ/ref=sr_1_4'
response = requests.get(product_url,headers=headers)
contents = response.text
soup = BeautifulSoup(contents,'html.parser')
#--------------------------------------------------Getting Product Name ---------------------------------------------------------------#
name = soup.find(name='span',id='productTitle')
print(name.getText())


#--------------------------------------------------Getting Price----------------------------------------------------------------------#
price = soup.find(name = 'span',class_= "a-size-medium a-color-price priceBlockBuyingPriceString") 
price_in_rupees = float(price.getText().replace('$','').replace(',',''))*75.01
print(price_in_rupees)

#-------------------------------------------------Checking target Price --------------------------------------------------------------#


if TARGET_PRICE >= price_in_rupees:
	with smtplib.SMTP('smtp.gmail.com',587) as connection:
		connection.starttls()
		connection.login(MY_EMAIL,MY_PASSWORD)
		connection.sendmail(
			from_addr = MY_EMAIL,
			to_addrs  = 'nawfabu@gmail.com',
			msg = f'''Subject:The product cost less than your product price \n\n {name} is ₹{price_in_rupees} go and get it. Enjoy :)  '''
			)
		print("mail sent")

