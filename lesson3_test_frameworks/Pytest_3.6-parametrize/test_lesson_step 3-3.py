import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:


   link = "https://stepik.org/lesson/236895/step/1"
   browser = webdriver.Chrome()
   browser.implicitly_wait(12)
   browser.get(link)
   answer = str(math.log(int(time.time())))
   field = browser.find_element_by_css_selector("#ember85").send_keys(answer)
   submit = browser.find_element_by_css_selector(".attempt__actions  button").click()
   b = browser.find_element_by_css_selector(".smart-hints__hint").text
   print(b)
   assert"Correct!"==b, "the text is not the same"

finally:
    time.sleep(10)
    browser.quit()
