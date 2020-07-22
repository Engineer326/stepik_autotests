from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    btn = browser.find_element_by_css_selector('.btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_val = browser.find_element_by_css_selector("#input_value")
    x = x_val.text
    result = calc(x)
    answer = browser.find_element_by_css_selector("#answer").send_keys(result)
    submit = browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()