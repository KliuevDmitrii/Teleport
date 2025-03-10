import pytest
import allure
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage
from pages.ProfilePage import ProfilePage

def auth_test(browser, test_data: dict):
    username = test_data.get("username")
    password = test_data.get("pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.enter_email_username(username)
    auth_page.enter_password(password)
    auth_page.click_button()
    WebDriverWait(browser, 10).until(EC.url_to_be("https://ratzzzsmsbot.ru/admin/#/transfers"))

    profile_page = ProfilePage(browser)
    profile_page.open_profile()
    info = profile_page.get_account_info()

    current_url = profile_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на admin/#/profile"):
        assert profile_page.get_current_url().endswith("admin/#/profile")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+username):
             assert info[0] == username


    
    # with allure.step(f"Текущий URL: {auth_page.get_current_url()}"):
    #    pass  # Логируем URL в отчете Allure

    # with allure.step("Проверка редиректа после авторизации"):
    #     assert auth_page.get_current_url().endswith("admin/#/transfers"), "Редирект не произошел или URL некорректный"
