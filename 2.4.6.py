from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    book = browser.find_element_by_css_selector('#book').click()
    x_val = browser.find_element_by_css_selector("#input_value")
    x = x_val.text
    result = calc(x)
    answer = browser.find_element_by_css_selector("#answer").send_keys(result)
    submit = browser.find_element_by_css_selector('#solve').click()
finally:
    time.sleep(5)
    browser.quit()