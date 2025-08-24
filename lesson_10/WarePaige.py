import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WarePaige:
    """
    Этот класс представляет:

      - страницу с товарами
      - кнопкой для добавления товара в корзину
      - кнопкой для перехода к последующей оплате товаров
    """
    def __init__(self, driver):
        """
        Конструктор класса WarePaige.
        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Нажатие кнопки {product} для добавления товара в корзину")
    def product_in_the_cart(self, product: str) -> bool:
        """
        Нажимает кнопку для добавления товара в корзину.

        :param product: id кнопки продукта, который необходимо добавить
        """
        # Добавляем +10 секунд к задержке для надежности
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[id={product}]"))
                    ).click()

    @allure.step("Нажатие кнопки {clickay} для перехода в корзину")
    def clickey_bag(self, clickay) -> bool:
        """
        Нажимает кнопку для перехода в корзину.

        :param clickay: id кнопки перехода в корзину.
        """
        # Добавляем +30 секунд к задержке для надежности
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"{clickay}"))).click()
