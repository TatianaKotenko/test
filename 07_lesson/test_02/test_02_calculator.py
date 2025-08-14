from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from InteractingWithElements import InteractingWithElements

def test_answer_calculator():
    driver = webdriver.Firefox()
    click_second_num = InteractingWithElements(driver)
    click_second_num.click_seconds("5")

    calculator_buttons_click = InteractingWithElements(driver)
    calculator_buttons_click.calculator_buttons()

    result_text = InteractingWithElements(driver)
    to_be = result_text.result_output_field ("15")
    as_is = "15"

    assert to_be == as_is

    driver.quit()
