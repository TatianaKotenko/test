import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoraisPage:
    """
    Этот класс представляет:
      - страницу авторизации на сайте
      - кнопку входа на сайт.
    """
    def __init__(self, driver):
        """
        Конструктор класса AutoraisPage.
        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Загрузка страницы сайта {site} с авторизацией")
    def login_to_the_website(self, site: str) -> None:
        """
        Вводит адрес сайта.

        :param site: Строка адреса сайта.
        :type username: str
        :return: None
        """
        self._driver.get(site)

    @allure.step("Авторизация: ввод имени {term1}, пароля {term2}")
    def fill_out_the_form(self, term1: str, term2: str) -> None:
        """
        Вводит имя пользователя и пароль в поле ввода.

        :param term1: Имя пользователя для входа.
        :param term2: Пароль пользователя для входа.
        :type username: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="user-name"]').send_keys(term1)
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="password"]').send_keys(term2)

    @allure.step("Нажатие кнопки {clickay} для авторизации на сайте")
    def clickey(self, clickay: str) -> bool:
        """
        Нажимает кнопку входа на сайт.

        :param clickay: id кнопки авторизации на сайте.
        """
        # Добавляем +20 секунд к задержке для надежности
        WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[id='{clickay}']"))).click()
