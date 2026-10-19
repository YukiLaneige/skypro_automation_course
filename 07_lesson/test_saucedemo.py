import pytest
from selenium import webdriver
from pages.sauce_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_shop_po(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_required_products()

    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Иван", "Иванов", "123456")

    checkout_page.click_continue()

    total_text = checkout_page.get_total_price()

    assert "Total: $58.29" in total_text, \
        f"Ожидалась сумма $58.29, но на странице отображается: '{total_text}'"
