import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckAndButton():
    """
    Класс представляет кнопку для перехода к вводу данных по оплате товара.
    """
    def __init__(self, driver):
        """
        Конструктор класса CheckAndButton.
        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Нажатие кнопки {click_check} перехода к вводу данных по оплате товара")
    def click_wera(self, click_check: str) -> bool:
        """
        Нажимает кнопку для перехода к вводу данных для оплаты товара.

        :param click_check: id кнопки для перехода к вводу данных оплаты товара.
        """
        # Добавляем +30 секунд к задержке для надежности
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[id={click_check}]"))).click()
