#Открыть страницу http://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".



import selenium
from selenium import webdriver
import time
import math
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

try:
	x = browser.find_element_by_id("input_value").text
	x = int(x)
	y = log(abs(12 * sin(x)))
	y = str(y)
	
	browser.execute_script("window.scrollBy(0, 100);")
	
	option1 = browser.find_element_by_id("answer")
	option1.send_keys(y)
	
	option2 = browser.find_element_by_id("robotCheckbox")
	option2.click()
	
	option3 = browser.find_element_by_id("robotsRule")
	option3.click()
	
	button = browser.find_element_by_xpath('//button[text()="Submit"]')
	button.click()

finally:
    time.sleep(20)
    browser.quit()