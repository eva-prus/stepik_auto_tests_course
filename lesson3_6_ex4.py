import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAbs():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", 
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"
                                    ])
    def test_abs1(browser,link):
        try:
            now_link = link
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(now_link)

            # Ваш код, который заполняет обязательные поля
            element1 = browser.find_element(By.CSS_SELECTOR, "#ember33")
            element1.click()
            element2 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
            element3 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
            element4 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            element2.send_keys("**")
            element3.send_keys("**")
            element4.click()
            button = WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "#ember33"))
        )
            element5 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
            answer = math.log(int(time.time()))
            element5.send_keys(str(answer))
            element6 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
            element6.click()
            answer_code = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
            print(answer_code)
            assert answer_code=="Correct!",f'При значении {answer} тест упал с кодовым ответом {answer_code}'

        finally:
            time.sleep(5)
            browser.quit()




