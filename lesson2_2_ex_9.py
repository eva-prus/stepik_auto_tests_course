from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    first_name.send_keys('test')
    last_name.send_keys('test')
    email.send_keys('test')
    file_but = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_test.txt')
    file_but.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()