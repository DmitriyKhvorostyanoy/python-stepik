import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:


   link = "http://suninjuly.github.io/get_attribute.html"
   browser = webdriver.Chrome()
   browser.get(link)

   people_radio = browser.find_element_by_id("peopleRule")
   people_checked = people_radio.get_attribute("checked")
   print("value of people radio: ", people_checked)
   #assert people_checked is not None, "People radio is not selected by default"
   #assert people_checked == "false", "что-то пошло не так скука"

   robots_radio = browser.find_element_by_id("robotsRule")
   robots_checked = robots_radio.get_attribute("checked")
   #assert robots_checked is None, 'oops'
   #time.sleep(12)

   submit_btn = browser.find_element_by_css_selector("[type='submit']")
   submit_btn_attribute = submit_btn.get_attribute("disabled")
   print(submit_btn_attribute)
   assert submit_btn_attribute is None





finally:
    time.sleep(4)
    browser.quit()

