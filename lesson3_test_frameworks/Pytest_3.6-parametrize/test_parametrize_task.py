from telnetlib import EC

import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("start browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    yield browser
    print("quit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_correct_answers(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time()-52.9)))
    field = browser.find_element_by_css_selector(".ember-text-area").send_keys(answer)
    submit = browser.find_element_by_css_selector(".attempt__actions  button").click()
    b = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(b)
    assert "Correct!" == b, "the text is not the same"
