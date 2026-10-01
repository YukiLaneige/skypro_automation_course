import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    # 1.  Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполните форму значениями
    form_data = {
        "first-name": "Иван", "last-name": "Петров",
        "address": "Ленина, 55-3", "e-mail": "test@skypro.com",
        "phone": "+7985899998787", "city": "Москва",
        "country": "Россия", "job-position": "QA", "company": "SkyPro"
    }
    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    # 3. Нажмите кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait = WebDriverWait(driver, 10)

    # 4. Проверьте (assert), что поле Zip code подсвечено красным
    zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_class, \
        f"Поле Zip code не красное! Класс: {zip_class}"

    # 5. Проверьте (assert), что остальные поля подсвечены зеленым
    for element_id in form_data.keys():
        container_class = (
            driver.find_element(By.ID, element_id).get_attribute("class"))
        assert "alert-success" in container_class, \
            f"Поле {element_id} не зеленое! Класс: {container_class}"
