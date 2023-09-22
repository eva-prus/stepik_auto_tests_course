from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    modal = browser.switch_to.alert
    modal.accept()
    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x1.text
    element = browser.find_element(By.CSS_SELECTOR, "#answer")
    element.send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()