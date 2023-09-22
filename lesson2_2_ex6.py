from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x1.text
    button = browser.find_element(By.TAG_NAME, "button")
    element = browser.find_element(By.CSS_SELECTOR, "#answer")
    element.send_keys(calc(x))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()