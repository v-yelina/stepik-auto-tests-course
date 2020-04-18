#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#Принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом


import selenium
from selenium import webdriver
import time
import math
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
	button1 = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
	button1.click()
	
	confirm = browser.switch_to.alert
	confirm.accept()
	
	x = browser.find_element_by_id("input_value").text
	x = int(x)
	y = log(abs(12 * sin(x)))
	y = str(y)
	
	option1 = browser.find_element_by_id("answer")
	option1.send_keys(y)
	
	button2 = browser.find_element_by_xpath('//button[text()="Submit"]')
	button2.click()

finally:
    time.sleep(30)
    browser.quit()