from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataAmount():
    def __init__(self, driver):
        self._driver = driver

    def pole_data_click(self, first_name, last_name, postal_codee):
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="first-name"]').send_keys(first_name)

        self._driver.find_element(
            By.CSS_SELECTOR, '[id="last-name"]').send_keys(last_name)

        self._driver.find_element(
            By.CSS_SELECTOR, '[id="postal-code"]').send_keys(postal_codee)

        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='continue']"))).click()

    def prise_ware(self):
        text_prise = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        text_prise_value = float(text_prise.split("$")[1])
        return text_prise_value
