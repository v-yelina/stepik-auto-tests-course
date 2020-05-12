#Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача - реализовать автотест со следующим сценарием действий: 

#открыть страницу 
#ввести правильный ответ 
#нажать кнопку "Отправить" 
#дождаться фидбека о том, что ответ правильный 
#проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.mark.parametrize(
	"link", 
	[
		("https://stepik.org/lesson/236895/step/1"), 
		("https://stepik.org/lesson/236896/step/1"),
		("https://stepik.org/lesson/236897/step/1"),
		("https://stepik.org/lesson/236898/step/1"),
		("https://stepik.org/lesson/236899/step/1"),
		("https://stepik.org/lesson/236903/step/1"),
		("https://stepik.org/lesson/236904/step/1"),
		("https://stepik.org/lesson/236905/step/1")
	]
)
def test_correct_text(link): 
	browser = webdriver.Chrome()
	browser.get(link)

	answer = math.log(int(time.time()))
	exception1 = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.TAG_NAME, "textarea"))
	)
	textarea = browser.find_element_by_tag_name("textarea")
	textarea.send_keys(str(answer))

	button1 = browser.find_element_by_tag_name('button')
	button1.click()

	exception2 = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
	)

	hint = browser.find_element_by_class_name('smart-hints__hint')
	hint_text = hint.text
	assert hint_text == "Correct!", "Text is not Correct!"
	
	browser.quit()