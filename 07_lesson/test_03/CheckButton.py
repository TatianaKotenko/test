from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckAndButton():
    def __init__(self, driver):
        self._driver = driver

    def click_wera(self):
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='checkout']"))).click()
