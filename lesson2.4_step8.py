# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()




    # Нахожу значение "х" и вставляю в поле ответа
    find_x = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(find_x))

    # Скролю страницу вниз
    button1 = browser.find_element(By.CSS_SELECTOR,'[type="submit"][class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)

    # Нажимаю кнопку "Submit"
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
