from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver):
        self.driver = driver
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/slow-calculator.html")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, button_text: str):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def get_result_text(self) -> str:
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected_text: str, timeout: int = 50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
