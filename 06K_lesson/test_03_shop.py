import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    # 9. Закройте браузер
    driver.quit()


def test_saucedemo_shop(driver):
    # 1. Откройте сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавьте в корзину товары
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейдите в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажмите Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполните форму своими данными
    driver.find_element(By.ID, "first-name").send_keys("Задания")
    driver.find_element(By.ID, "last-name").send_keys("Очень")
    driver.find_element(By.ID, "postal-code").send_keys("Не интересные")

    # 7. Нажмите кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитайте со страницы итоговую стоимость (Total)
    total_label = driver.find_element(By.CLASS_NAME,
                                      "summary_total_label").text

    # 10. Проверьте, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_label, \
        f"Ожидалась сумма $58.29, но на странице отображается: '{total_label}'"
