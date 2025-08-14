from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckAndButton():
    def __init__(self, driver):
        self._driver = driver
    
    def check_ware(self):
        element = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cart_list"))).text
        element_text = str [element("Sauce Labs Onesie", "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt")]
        
        return element_text
    
    def click_wera(self):
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='checkout']"))).click()