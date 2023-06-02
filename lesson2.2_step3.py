from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# import math

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    num3 = int(num1) + int(num2)
    num4 = str(num3)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(num4)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(1)

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


