import pytest
import allure
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage

# Проверка авторизация зарегестрированного пользователя
@pytest.mark.parametrize("email, password", [
    ("123456", "123456")
])
def auth_test(browser, email, password):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.enter_email(email)
    auth_page.enter_password(password)
    auth_page.click_button()
    WebDriverWait(browser, 10).until(EC.url_to_be("https://ratzzzsmsbot.ru/admin/#/transfers"))
    
    with allure.step(f"Текущий URL: {auth_page.get_current_url()}"):
       pass  # Логируем URL в отчете Allure

    with allure.step("Проверка редиректа после авторизации"):
        assert auth_page.get_current_url().endswith("admin/#/transfers"), "Редирект не произошел или URL некорректный"