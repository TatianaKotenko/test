import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserAuthorization:
    def __init__(self, driver):
        self._driver = driver

    def enter(self, site):
        self._driver.get(site)

    def autorization(self, clickay):
        WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, (clickay)))).click()

    def data_number(self, data: str) -> None:
        self._driver.find_element(
            By.CSS_SELECTOR, 'ui-input-phone__input.ui-input-phone__input--short.chg-app-input__control.chg-app-input__control--prefix').send_keys(data)

    def get_code(self, click_get):
        WebDriverWait(self._driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, (click_get)))).click()

    def element(self):
        text_heading = self._driver.find_element(
            By.CSS_SELECTOR, "_H4_1mkgt_24._Title_1il3o_53._Title_center_1il3o_1").text
        return text_heading
