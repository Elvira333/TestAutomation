# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
# Нахожу элемент-картинку, беру атрибут valuex, считаю мат.функцию и вывожу в нужное поле ответ
    input1 = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(calc(input1))
# Отмечаю checkbox "I'm the robot" и выбираю radiobutton "Robots rule!"
    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.click()
    time.sleep(2)
    button2 = browser.find_element(By.ID, 'robotsRule')
    button2.click()
# Нажимаю на кнопку "Submit"
    button3 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


