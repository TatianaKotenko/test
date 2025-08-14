from selenium import webdriver
from InteractingWithElements import InteractingWithElements


def test_answer_calculator():
    driver = webdriver.Firefox()
    click_second_num = InteractingWithElements(driver)
    click_second_num.click_seconds("45")

    calculator_buttons_click = InteractingWithElements(driver)
    calculator_buttons_click.calculator_buttons("7")
    calculator_buttons_click.calculator_buttons("+")
    calculator_buttons_click.calculator_buttons("8")
    calculator_buttons_click.calculator_buttons("=")

    result_text = InteractingWithElements(driver)
    to_be = result_text.result_output_field("15")
    as_is = "15"

    assert to_be == as_is

    driver.quit()
