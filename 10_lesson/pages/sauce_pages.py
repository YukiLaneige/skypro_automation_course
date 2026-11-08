import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу авторизации Saucedemo.
        """
        self.driver = driver
        self.url = "https://saucedemo.com"

    @allure.step("Открыть главную страницу магазина")
    def open(self) -> None:
        """
        Открывает URL интернет-магазина в окне браузера.
        """
        self.driver.get(self.url)

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Вводит логин, пароль и нажимает кнопку авторизации.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу каталога товаров (Inventory).
        """
        self.driver = driver

    @allure.step("Добавить обязательные товары в корзину "
                 "(рюкзак, футболку и боди)")
    def add_required_products(self) -> None:
        """
        Добавляет три определенных товара в корзину интернет-магазина.
        """
        self.driver.find_element(*self.BACKPACK_BTN).click()
        self.driver.find_element(*self.TSHIRT_BTN).click()
        self.driver.find_element(*self.ONESIE_BTN).click()

    @allure.step("Перейти в корзину магазина")
    def go_to_cart(self) -> None:
        """
        Кликает по иконке корзины для перехода
        на страницу предпросмотра выбранных товаров.
        """
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу корзины (Cart).
        """
        self.driver = driver

    @allure.step("Нажать на кнопку оформления заказа 'Checkout'")
    def click_checkout(self) -> None:
        """
        Кликает по кнопке начала процедуры оформления покупки.
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу оформления заказа
        и ввода контактных данных (Checkout).
        """
        self.driver = driver

    @allure.step("Заполнить форму доставки данными клиента:"
                 " {first_name} {last_name}, индекс: {postal_code}")
    def fill_checkout_form(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Вводит имя, фамилию и почтовый индекс в соответствующие поля.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    @allure.step("Нажать кнопку 'Continue' для перехода "
                 "на страницу подтверждения")
    def click_continue(self) -> None:
        """
        Кликает кнопку продолжения оформления заказа.
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Считать итоговую стоимость заказа с экрана")
    def get_total_price(self) -> str:
        """
        Возвращает текстовое значение итоговой стоимости заказа.
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
