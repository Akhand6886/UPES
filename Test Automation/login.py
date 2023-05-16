from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')

username_field = driver.find_element_by_name('username')
username_field.send_keys('tomsmith')
password_field = driver.find_element_by_name('password')
password_field.send_keys('SuperSecretPassword!')

# Submit the login form
login_button = driver.find_element_by_class_name('radius')
login_button.click()