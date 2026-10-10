from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class InventoryPage:
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_required_products(self):
        self.driver.find_element(*self.BACKPACK_BTN).click()
        self.driver.find_element(*self.TSHIRT_BTN).click()
        self.driver.find_element(*self.ONESIE_BTN).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self) -> str:
        return self.driver.find_element(*self.TOTAL_LABEL).text
