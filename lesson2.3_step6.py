# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'trollface')
    button.click()

    # Запоминаю путь к первой вкладке и записываю путь ко второй вкладке
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    # Переключаю для дальнейшей работы в новой вкладке, иначе код будет работать со старой вкладкой
    browser.switch_to.window(new_window)

    # Нахожу значение "х" и вставляю в поле ответа
    find_x = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(find_x))

    # Нажимаю кнопку "Submit"
    button1 = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button1.click()

finally:
    time.sleep(5)
    browser.quit()
