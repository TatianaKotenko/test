from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoraisPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
    
    def fill_out_the_form(self, term1, term2):
        self._driver.find_element(By.CSS_SELECTOR, '[id="user-name"]').send_keys(term1)
        self._driver.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys(term2)

        WebDriverWait(self._driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login-button']"))).click()