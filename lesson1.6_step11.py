from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "form-control.first[required]")
    input1.send_keys("IvanIvanIvanIvanIvanIvanIvanIvan")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second[required]")
    input2.send_keys("PetrovPetrovPetrovPetrovPetrovvv")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third[required]")
    input3.send_keys("testtesttesttesttesttes@test.com")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    time.sleep(1)
    welcome_text_elt=browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
