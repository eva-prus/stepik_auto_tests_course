from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 100).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()
    x1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x1.text
    element = browser.find_element(By.CSS_SELECTOR, "#answer")
    element.send_keys(calc(x))
    button = browser.find_element(By.ID, "solve")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()