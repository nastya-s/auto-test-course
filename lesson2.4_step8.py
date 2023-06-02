from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until( # тут мы ждем пока цена не станет $100 
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

