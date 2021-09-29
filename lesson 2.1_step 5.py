import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:


   link = "http://suninjuly.github.io/math.html"
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element_by_css_selector("#input_value")
   x = x_element.text
   y = calc(x)
   print(x)
   print(y)

   field = browser.find_element_by_css_selector("#answer")
   field.send_keys(y)

   chckbx = browser.find_element_by_css_selector("#robotCheckbox")
   chckbx.click()

   radio = browser.find_element_by_css_selector("#robotsRule")
   radio.click()

   submit = browser.find_element_by_css_selector("[type='submit']")
   submit.click()




finally:
    time.sleep(10)
    browser.quit()
