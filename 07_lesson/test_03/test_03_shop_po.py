from selenium import webdriver
from AutoraisPaige import AutoraisPage
from WarePaige import WarePaige
from CheckButton import CheckAndButton
from DataAmount import DataAmount


def test_shoping():
    driver = webdriver.Firefox()
    entrance_and_authorization = AutoraisPage(driver)
    entrance_and_authorization.fill_out_the_form(
        "standard_user", "secret_sauce")

    products_and_shopping_car = WarePaige(driver)
    products_and_shopping_car.product_in_the_cart()

    click_wera_click = CheckAndButton(driver)
    click_wera_click.click_wera()

    click_dsta = DataAmount(driver)
    click_dsta.pole_data_click("Tatiana", "Kotenko", "283036")

    prise_data = DataAmount(driver)
    prise_data.prise_ware()

    assert prise_data.prise_ware() == 58.29

    driver.quit()
