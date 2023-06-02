from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox1 = browser.find_element(By.ID, 'robotCheckbox')
    checkbox1.click()
    radiobtn = browser.find_element(By.ID, 'robotsRule')
    radiobtn.click()
    button.click()
finally:
    time.sleep(5)
    browser.quit()
