from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ratzzzsmsbot.ru/admin/#/login?returnTo=/profile"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин или эл. почта"]').send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, 'span.p-button-label[data-pc-section="label"]').click()

    def get_current_url(self):
        return self.__driver.current_url