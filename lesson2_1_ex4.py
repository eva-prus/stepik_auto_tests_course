from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x11 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x11.text
    x21 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x21.text
    result = int(x1)+int(x2)
    print(result)
    selectElement = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    selectElement.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()