from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_interaction():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Заполните поле "custname" значением "Иван Иванов"
    driver.find_element(By.NAME, "custname").send_keys("Иван Иванов")

    # Найдите кнопку отправки и кликните на нее
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()

    driver.quit()
