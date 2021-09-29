import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:


   link = "http://suninjuly.github.io/selects2.html"
   browser = webdriver.Chrome()
   browser.get(link)

   a = int(browser.find_element_by_id("num1").text)
   print(a)
   b = int(browser.find_element_by_id("num2").text)
   print(b)
   x = str(a+b)
   print(x)

   select = Select(browser.find_element_by_id("dropdown"))
   select.select_by_value(x)

   submit = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
