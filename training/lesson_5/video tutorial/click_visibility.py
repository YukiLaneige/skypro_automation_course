from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/visibility")
sleep(1)

button_hide = driver.find_element(
    By.ID, "hideButton")
button_hide.click()

button_visibility_hidden = driver.find_element(
    By.ID, "invisibleButton")

if button_visibility_hidden.is_displayed():
    print("Кнопка видна")
else:
    print("Кнопка скрыта")

sleep(1)
driver.quit()
