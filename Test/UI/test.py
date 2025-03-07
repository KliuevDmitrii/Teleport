import pytest
import allure
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage

def auth_test(browser, test_data: dict):
    username = test_data.get("username")
    password = test_data.get("pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.enter_email_username(username)
    auth_page.enter_password(password)
    auth_page.click_button()
    WebDriverWait(browser, 10).until(EC.url_to_be("https://ratzzzsmsbot.ru/admin/#/transfers"))
    
    with allure.step(f"Текущий URL: {auth_page.get_current_url()}"):
       pass  # Логируем URL в отчете Allure

    with allure.step("Проверка редиректа после авторизации"):
        assert auth_page.get_current_url().endswith("admin/#/transfers"), "Редирект не произошел или URL некорректный"