import pytest
from selenium import webdriver
from pages.calc_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_po(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()

    calc_page.set_delay("45")
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result("15", timeout=50)

    result = calc_page.get_result_text()
    assert result == "15", \
        f"Ожидалось 15, но на экране отобразилось '{result}'"
