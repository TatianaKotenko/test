from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InteractingWithElements:
    def __init__(self, driver):
        """
        Конструктор класса InteractingWithElements.

        :param driver: driver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Открытие страницы калькулятора {website}")
    def click_seconds_site(self, website: str) -> None:
        """
        Открывает страницу вебсайта калькулятора.
        Устанавливает максимальный размер окна.
        """
        self._driver.get(website)
        self._driver.maximize_window()

    @allure.step("Установка задержки {delay_text} секунд")
    def delay_in(self, delay_text: str) -> None:
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay_text: int — время задержки в секундах.
        """
        # Добавляем +10 секунд к задержке для надежности
        delay_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(delay_text)

    @allure.step("Нажатие кнопки '{button}'")
    def calculator_buttons(self, button: str) -> None:
        """
        Нажимает на кнопку калькулятора.

        :param button: str — текст на кнопке, которую нужно нажать.
        """
        self._driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Ожидание результата '{res}'")
    def result_output_field(self, res: str) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param res: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.
        """
        # Добавляем +60 секунд к задержке для надежности
        WebDriverWait(self._driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), res))

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        result = self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text

        return result
