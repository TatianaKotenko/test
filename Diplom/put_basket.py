import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PutBasket:
    def __init__(self, driver):
        self._driver = driver

    def enter(self, site):
        self._driver.get(site)

    def search_field(self, author: str) -> None:
        self._driver.find_element(
            By.CSS_SELECTOR, 'div.search-form__input.search-form__input--search').send_keys(author)

    def author_search_button(self, author_clickay: str) -> bool:
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[class='{author_clickay}']"))).click()

    def click_book_basket(self, basket_clickay):
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[class='{basket_clickay}']"))).click()

    def basket_number(self):
        number_of_basket = self._driver.find_element(
            By.CSS_SELECTOR, "div.chg-indicator.chg-indicator--bg-red.chg-indicator--mod-m-l.header-controls__indicator").text
        return number_of_basket
