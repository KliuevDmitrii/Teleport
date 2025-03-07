import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider

class AuthPage:
    """
    Этот класс предоставляет методы для выполнения действий на странице авторизации пользователя
    """

    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get("ui", "base_url")
        self.__url = url
        self.__driver = driver

    @allure.step("Открыть страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Ввести email\логин")
    def enter_email_username(self, email: str):
        element = self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин или эл. почта"]')
        element.clear()
        element.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password:str):
        element = self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
        element.clear()
        element.send_keys(password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'span.p-button-label[data-pc-section="label"]').click()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url