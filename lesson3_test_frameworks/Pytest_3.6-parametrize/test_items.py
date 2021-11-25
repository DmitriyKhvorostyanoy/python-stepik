import time

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_presense_of_button_for_es_lang(browser):
    browser.get(link)
    time.sleep(30)
    a = browser.find_elements_by_css_selector("#add_to_basket_form [type='submit']")
    assert len(a)==1,'button is not exist'
