#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ

import selenium
from selenium import webdriver
import time
import math
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
	button1 = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
	button1.click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
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