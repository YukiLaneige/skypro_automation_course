from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/checkboxes")
sleep(1)

checkboxes = driver.find_elements(By.TAG_NAME, "input")

for i, checkbox in enumerate(checkboxes, 1):
    print(f"Чекбокс {i} выбран: {checkbox.is_selected()}")

sleep(1)
driver.quit()
