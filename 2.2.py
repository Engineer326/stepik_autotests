from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects2.html")

    x1 = int(browser.find_element_by_id("num1").text)
    x2 = int(browser.find_element_by_id("num2").text)
    # numlist = [x1, x2]
    # number_sum = sum(numlist)
    number_sum = x1 + x2
    print(number_sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(number_sum))

    bttn = browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(10)
    browser.quit()