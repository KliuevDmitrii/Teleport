import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider

class ProfilePage:
    """
    Этот класс предоставляет методы для выполнения действий на странице профиля администратора.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")  # self.url, а не просто url

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть страницу профиля администратора")
    def open_profile(self):
        profile_button = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'pi-user')]"))
        )
        profile_button.click()

    @allure.step("Прочитать информацию о пользователе")
    def get_account_info(self) -> list[str]:
        try:
        # Ожидаем, что элемент будет видимым на странице
            login_element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[@data-v-5481855f='']"))
        )
        
        # Печатаем текст, чтобы убедиться, что мы находим правильный элемент
            login_text = login_element.text.strip()
            print(f"Логин: {login_text}")
        
            return [login_text] if login_text else [""]
    
        except Exception as e:
        # Печатаем ошибку, если элемент не был найден
            print(f"Ошибка при получении логина: {e}")
            return [""]
