from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    #Нахожу элемент Х, присваиваю его текст переменной х, выполняю функцию заданную выше по подсчету и присваиваю его значение переменной y
    x_element = browser.find_element_by_css_selector (".form-group #input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    #нажатие на чекбокс
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    # переключаю радиобаттон
    option2 = browser.find_element_by_css_selector("[value = 'robots']")
    option2.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
