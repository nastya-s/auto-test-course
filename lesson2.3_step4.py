from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    form = browser.find_element(By.ID, 'answer')
    form.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()


finally:
    time.sleep(5)
    browser.quit()