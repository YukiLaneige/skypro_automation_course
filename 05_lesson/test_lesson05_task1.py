from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    assert "/forms/post" in driver.current_url

    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online"
# Требует слэш в конце, это считается за ошибку?

    driver.quit()
