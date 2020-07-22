from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.maximize_window()
    browser.get(link)
    x_val = browser.find_element_by_css_selector("#input_value")
    x = x_val.text
    result = calc(x)
    print(result)
    answer = browser.find_element_by_css_selector("#answer").send_keys(result)
    check = browser.find_element_by_css_selector('#robotCheckbox').click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robot_rule = browser.find_element_by_css_selector("[value = 'robots'").click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()