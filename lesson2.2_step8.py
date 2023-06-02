from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.NAME, 'firstname')
    firstname.send_keys('Nastya')
    lastname = browser.find_element(By.NAME, 'lastname')
    lastname.send_keys('Razanava')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('test1@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__)) #определение пути для загрузки файла
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    choose_file = browser.find_element(By.ID, 'file')
    choose_file.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
