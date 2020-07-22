import os
from selenium import webdriver
import time
browser = webdriver.Chrome()
try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    input1 = browser.find_element_by_name('firstname').send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname').send_keys('ivanov')
    input3 = browser.find_element_by_name('email').send_keys('bla@bla.com')
    upload = browser.find_element_by_css_selector('#file')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    upload.send_keys(file_path)

    submit = browser.find_element_by_css_selector('.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
