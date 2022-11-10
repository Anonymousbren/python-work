from selenium import webdriver
from getpass import getpass
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
username = input(' enter your facebook username, email or phone number: ')
passwd = getpass('enter your facebook password: ') 


driver = webdriver.Chrome(ChromeDriverManager().install)
driver.get('http://facebook.com')
