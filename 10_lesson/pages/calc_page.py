import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора с веб-драйвером.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev"
            "selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        """
        Открывает URL страницы калькулятора в браузере.
        """
        self.driver.get(self.url)

    @allure.step("Установить задержку {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Очищает поле задержки и вводит указанное количество секунд.
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать на кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Находит кнопку калькулятора по её тексту и кликает на неё.
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Получить текущий текст с экрана калькулятора")
    def get_result_text(self) -> str:
        """
        Возвращает текстовое значение, отображаемое на экране калькулятора.
        """
        return self.driver.find_element(*self.SCREEN).text

    @allure.step("Ожидать появление результата '{expected_text}'")
    def wait_for_result(self, expected_text: str, timeout: int = 50) -> None:
        """
        Ожидает в течение timeout секунд, пока на экране калькулятора
        появится ожидаемый текст.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
