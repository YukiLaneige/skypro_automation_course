import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # 1. Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле ввода по локатору #delay введите значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажмите на кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверьте (assert), что в окне отобразится результат 15 через 45 сек
    screen_locator = (By.CSS_SELECTOR, "div.screen")

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(screen_locator, "15")
    )

    result_text = driver.find_element(*screen_locator).text
    assert result_text == "15", \
        f"Ожидалось 15, но на экране отобразилось '{result_text}'"
