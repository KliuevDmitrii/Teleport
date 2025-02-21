from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage

def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("123456", "123456")
    WebDriverWait(browser, 10).until(EC.url_to_be("https://ratzzzsmsbot.ru/admin/#/transfers"))

    assert auth_page.get_current_url().endswith("admin/#/transfers")