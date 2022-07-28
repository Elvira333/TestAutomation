# Программа должна выполнить следующие шаги:
# 1.Открыть страницу http://suninjuly.github.io/math.html.
# 2.Считать значение для переменной x.
# 3.Посчитать математическую функцию от x (код для этого приведён ниже).
# 4.Ввести ответ в текстовое поле.
# 5.Отметить checkbox "I'm the robot".
# 6.Выбрать radiobutton "Robots rule!".
# 7.Нажать на кнопку Submit.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нахождение значения х, выполнение математического примера и вывод в строку ответа
    input1 = browser.find_element(By.ID, 'input_value').text
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(calc(input1))
    time.sleep(2)
    # Нахождение чекбокса и ставлю галочку
    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.click()
    time.sleep(2)
    # Выбираю radiobutton "Robots rule!"
    button2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    button2.click()
    
    # Нажимаю кнопку Submit
    button3 = browser.find_element(By.TAG_NAME, 'button')
    button3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
