import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_should_exist(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button, "Should be button"