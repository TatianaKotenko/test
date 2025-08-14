from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InteractingWithElements:
    def __init__(self, driver):
        self._driver = driver

    def click_seconds(self, delay_text):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self._driver.maximize_window()

        delay_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(delay_text)

    def calculator_buttons(self, button):
        self._driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    def result_output_field(self, res):
        WebDriverWait(self._driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), res))
        result = self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text

        return result
