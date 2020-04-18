#В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение



import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import log, sin

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button1 = browser.find_element_by_id("book")
exception1 = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button1.click()

x = browser.find_element_by_id("input_value").text
x = int(x)
y = log(abs(12 * sin(x)))
y = str(y)

option1 = browser.find_element_by_id("answer")
option1.send_keys(y)

button2 = browser.find_element_by_xpath('//button[text()="Submit"]')
button2.click()
