from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WarePaige:
    def __init__(self, driver):
        self._driver = driver

    def product_in_the_cart(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-backpack']"))
                    ).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']")
                    )).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']"))
                    ).click()

        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.shopping_cart_link"))).click()
