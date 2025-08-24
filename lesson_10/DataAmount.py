import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataAmount():
    """
    Этот класс представляет:

       - страницу с вводом данных для последующей оплаты товаров
       - кнопку для просмотра и поиска общей суммы заказа.
    """
    def __init__(self, driver):
        """
        Конструктор класса DataAmount.
        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step(
            "Ввод данных пользователя: имени {first_name}, фамилии {last_name}, индекса {postal_codee}"
            )
    def pole_data_click(self, first_name: str, last_name: str, postal_codee: str) -> None:
        """
        Вводит аднные для последующей оплаты товара в поле ввода.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param last_name: Индекс.
        :type username: str
        :return: None
        """
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="first-name"]').send_keys(first_name)

        self._driver.find_element(
            By.CSS_SELECTOR, '[id="last-name"]').send_keys(last_name)

        self._driver.find_element(
            By.CSS_SELECTOR, '[id="postal-code"]').send_keys(postal_codee)

    @allure.step("Нажатие кнопки для просмотра цены {click_pass}")
    def clickey_pass(self, click_pass: str) -> bool:
        """
        Нажимает кнопку для просмотра цены.

        :param click_pass: id кнопки для переходак просмотру цены.
        """
        # Добавляем +30 секунд к задержке для надежности
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[id='{click_pass}']"))).click()

    @allure.step("Получение общей суммы корзины в виде числа")
    def prise_ware(self):
        """
        Находит и возвращает общую сумму крзины.

        :return: float — общая сумма к оплате товаров, преобразованное в дробное число.
        """
        text_prise = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        text_prise_value = float(text_prise.split("$")[1])
        return text_prise_value
