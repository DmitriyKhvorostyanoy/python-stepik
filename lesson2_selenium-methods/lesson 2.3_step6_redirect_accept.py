from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".container > button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_css_selector("#answer")
    field.send_keys(y)

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла