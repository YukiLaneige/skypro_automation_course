import pytest
import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.calc_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Тест проверяет сложение чисел 7 и 8 на калькуляторе "
                    "с установленной задержкой вычислений в 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_slow_calculator_po(driver: WebDriver) -> None:
    calc_page = CalculatorPage(driver)
    calc_page.open()

    with allure.step("Выполнить математическую операцию: 7 + 8"):
        calc_page.set_delay("45")
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Дождаться окончания вычислений (задержка 45 сек)"):
        calc_page.wait_for_result("15", timeout=50)

    with allure.step("Проверить, что итоговый результат на экране равен 15"):
        result = calc_page.get_result_text()
        assert result == "15", \
            f"Ожидалось 15, но на экране отобразилось '{result}'"
