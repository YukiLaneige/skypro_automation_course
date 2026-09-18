from selenium import webdriver
from selenium.webdriver.common.by import By


def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    # Найдите радио-кнопку "Yes" и проверьте 1. отображается:
    driver.find_element(By.ID, "yesRadio").is_displayed()

    # 2. Что она доступна для клика (через метку)
    label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    assert label.is_enabled()

    driver.quit()
