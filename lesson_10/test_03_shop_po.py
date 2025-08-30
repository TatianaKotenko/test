from selenium import webdriver
import allure
from AutoraisPaige import AutoraisPage
from WarePaige import WarePaige
from CheckButton import CheckAndButton
from DataAmount import DataAmount


@allure.epic("интернет-магазин товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тестирование интернет-магазина товаров")
@allure.description(
    "Тест проверяет корректность работы интернет-магазина товаров с различными операциями."
    )
@allure.feature("интернет-магазин товаров")
def test_shoping():
    """
    Тест проверяет работу интернет-магазина товаров с различными операциями:
    1. вход на сайт интернет-магазина
        :param site: str — адресная строка вебсайта интернет-магазина товаров.

    2. авторизация на сайте интернет-магазина
        :param term1: str — имя пользователя для входа.
        :param term2: str — пароль пользователя для входf.
        :param clickay: id кнопки авторизации на сайте.

    3. добавление товаров в корзину и последующий переход
        :param product: id кнопки продукта, который необходимо добавить
        :param clickay: id кнопки перехода в корзину.

    4. переход к вводу данных для оплаты товара
        :param click_check: id кнопки перехода к вводу данных оплаты товара.

    5. ввод данных последующей оплаты товаров и просмотра суммы заказа
        :param first_name: Имя.
        :param last_name: Фамилия.
        :param last_name: Индекс.
        :param click_pass: id кнопки для переходак просмотру цены.
        :param summary_total: локатор кнопки для полученияобщей суммы корзины.
        :return: float — общая сумма к оплате, приведенная к дробному числу.

    :param driver: WebDriver — объект драйвера.
    """
    driver = webdriver.Firefox()

    with allure.step("Загрузка страницы сайта {site} с авторизацией"):
        entrance_and_authorization = AutoraisPage(driver)
        entrance_and_authorization.login_to_the_website(
            "https://www.saucedemo.com/"
            )

    with allure.step("Авторизация: ввод имени {term1}, пароля {term2}"):
        entrance_and_authorization = AutoraisPage(driver)
        entrance_and_authorization.fill_out_the_form(
            "standard_user", "secret_sauce")

    with allure.step("Нажатие кнопки {clickay} для авторизации на сайте"):
        entrance_and_authorization = AutoraisPage(driver)
        entrance_and_authorization.clickey('login-button')

    with allure.step("Нажатие кнопки {product} добавления товара в корзину"):
        products_and_shopping_car = WarePaige(driver)
        products_and_shopping_car.product_in_the_cart(
            'add-to-cart-sauce-labs-backpack'
            )
        products_and_shopping_car.product_in_the_cart(
            'add-to-cart-sauce-labs-bolt-t-shirt'
            )
        products_and_shopping_car.product_in_the_cart(
            'add-to-cart-sauce-labs-onesie'
            )

    with allure.step("Нажатие кнопки {clickay} для перехода в корзину"):
        products_and_shopping_car = WarePaige(driver)
        products_and_shopping_car.clickey_bag('a.shopping_cart_link')

    with allure.step(
        "Нажатие кнопки {click_check} перехода к вводу данных по оплате товара"
            ):
        click_wera_click = CheckAndButton(driver)
        click_wera_click.click_wera('checkout')

    with allure.step(
        "Ввод данных пользователя: имени {first_name}, фамилии {last_name}, индекса {postal_codee}"
            ):
        click_dsta = DataAmount(driver)
        click_dsta.pole_data_click("Tatiana", "Kotenko", "283036")

    with allure.step("Нажатие кнопки для просмотра цены {click_pass}"):
        click_dsta = DataAmount(driver)
        click_dsta.clickey_pass('continue')

    with allure.step("Получение общей суммы корзины в виде числа"):
        prise_data = DataAmount(driver)
        prise_data.prise_ware()

    assert prise_data.prise_ware() == 58.29, \
        (f"Ожидаемый результат: {58.29}, "
            f"получен: {prise_data.prise_ware()}")

    driver.quit()
