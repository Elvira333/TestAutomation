# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return math.log(abs(12 * math.sin(int(x))))

try:
    # Открыла страницу, нашла значение x и записала, нашла поле answer и используя метод вычисления положила в него правильный ответ
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    # Скролю страницу вниз
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"][class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбираю checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Переключаю radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    # Нажимаю на кнопку "Submit"
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()