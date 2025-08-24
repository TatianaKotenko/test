from selenium import webdriver
import allure
from InteractingWithElements import InteractingWithElements


@allure.title("Тестирование калькулятора")
@allure.description(
    "Тест проверяет корректность работу калькулятора с различными операциями."
    )
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_answer_calculator():
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера.
    :param website: str — адресная строка вебсайта калькулятора.
    :param delay_text: int — задержка в секундах для выполнения операции.
    :param button: str — значения для операции (число, +, -, x, ÷).
    :param res: str — ожидаемый результат операции.

    """
    driver = webdriver.Firefox()

    with allure.step("Открытие страницы калькулятора '{website}'"):
        click_second_num = InteractingWithElements(driver)
        click_second_num.click_seconds_site(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    with allure.step("Установка задержки {delay_text} секунд"):
        delay_in_second = InteractingWithElements(driver)
        delay_in_second.delay_in("45")

    with allure.step("Нажатие кнопки '{button}'"):
        calculator_buttons_click = InteractingWithElements(driver)
        calculator_buttons_click.calculator_buttons("7")
        calculator_buttons_click.calculator_buttons("+")
        calculator_buttons_click.calculator_buttons("8")
        calculator_buttons_click.calculator_buttons("=")

    with allure.step("Ожидание результата '{res}'"):
        result_text = InteractingWithElements(driver)
        result_text.result_output_field("15")

    with allure.step("Получение результата с экрана калькулятора"):
        to_be = result_text.get_result()
        as_is = "15"

    assert to_be == as_is, \
        (f"Ожидаемый результат: {to_be}, "
            f"получен: {as_is}")

    driver.quit()
