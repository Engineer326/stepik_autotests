from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(treasure_val)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    treasure_val = treasure.get_attribute("valuex")
    y = calc(treasure_val)

    answer = browser.find_element_by_css_selector("#answer").send_keys(y)
    check = browser.find_element_by_css_selector('#robotCheckbox').click()
    robot_rule = browser.find_element_by_css_selector("[value = 'robots'").click()
    submit = browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()