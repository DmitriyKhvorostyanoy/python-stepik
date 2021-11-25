import pytest
from selenium import webdriver
import time

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'

def test_en_lan(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form [type='submit']")
    time.sleep(30)