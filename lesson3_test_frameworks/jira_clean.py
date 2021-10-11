from operator import index

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

link = "https://employeesgate.atlassian.net/jira/software/c/projects/VISA/boards/23/backlog"

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(12)
wait =  WebDriverWait(browser, 10)
browser.get(link)

google_btn = browser.find_element_by_id("google-auth-button").click()
name=browser.find_element_by_css_selector("[type='email']").send_keys("dmitriy.khvoros*******com")
next1 = browser.find_element_by_xpath('//*[contains(text(),"Далее")]').click()
WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='password']"))
        )
password_field = browser.find_element_by_css_selector("[type='password']").send_keys('******')
next2 = browser.find_element_by_xpath('//*[contains(text(),"Далее")]').click()

"""for x in range(50):
        issues = browser.find_elements_by_xpath("//*[contains(text(),'Establishing')]")
        issues[x].click()
        browser.find_element_by_xpath('//*[contains(text(),"To Do")]').click()
        browser.find_element_by_xpath('//*[contains(text(),"Won")]').click()
        time.sleep(1)"""
#Code above is working

issues = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[contains(text(),"VISA-3")]')))
print(len(issues))
for x in range(len(issues)):
        #issues = browser.find_elements_by_xpath("//*[contains(text(),'Establishing')]")
        issues[x].click()
        print(len(issues))
        browser.find_element_by_xpath('//*[contains(text(),"To Do")]').click()
        browser.find_element_by_xpath('//*[contains(text(),"Won")]').click()
        #time.sleep(1)