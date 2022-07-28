# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
   return math.log(abs(12 * math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button.click()

    # Принимаю модальное окно и нажимаю на кнопку "ок"
    confirm = browser.switch_to.alert
    confirm.accept()

    # Нахожу переменную "x" и кладу её в поле с ответом
    find_x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(find_x))

    button1 = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button1.click()


finally:
    time.sleep(5)
    browser.quit()
