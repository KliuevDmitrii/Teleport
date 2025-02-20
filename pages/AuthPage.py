from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ratzzzsmsbot.ru/admin/#/login?returnTo=/profile"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)