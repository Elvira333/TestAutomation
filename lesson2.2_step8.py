# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    # Открываю браузер, запускаю ссылку, заполняю все важные поля
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys('Эльвира')
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys('Аннаева')
    email = browser.find_element(By.NAME, "email")
    email.send_keys('elviraw@mail.ru')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'ggg.txt')
    print(file_path)

    element = browser.find_element(By.CSS_SELECTOR, '[type="file"][name="file"]')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
