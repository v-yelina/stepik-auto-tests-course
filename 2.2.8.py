#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"


import selenium
from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
	
	option1 = browser.find_element_by_name("firstname")
	option1.send_keys("Vanja")
	option2 = browser.find_element_by_name("lastname")
	option2.send_keys("Ivanov")
	option3 = browser.find_element_by_name("email")
	option3.send_keys("dfg@gmail.com")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	
	option4 = browser.find_element_by_id("file")
	option4.send_keys(file_path)
	
	button = browser.find_element_by_xpath('//button[text()="Submit"]')
	button.click()

finally:
    time.sleep(30)
    browser.quit()
