from selenium import webdriver
import time
import unittest

class Test_Uniq_Selectors(unittest.TestCase):
    def test_selectors1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block >.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second_class :nth-child(2)")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input3.send_keys("email@email.email")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Message is not displayed")
        browser.quit()

    def test_selectors2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block >.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second_class :nth-child(2)")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input3.send_keys("email@email.email")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Message is not displayed")
        browser.quit()

if __name__ == "__main__":
    unittest.main()