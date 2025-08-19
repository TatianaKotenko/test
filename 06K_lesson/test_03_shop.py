from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop():
    from selenium.webdriver.firefox.service import Service
    path = r'C:/Users/tatti/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe'
    service = Service(executable_path=path)
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    driver.get("https://www.saucedemo.com/")

    UserName = driver.find_element(By.CSS_SELECTOR, '[id="user-name"]')
    UserName.send_keys("standard_user")

    Password = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
    Password.send_keys("secret_sauce")

    equals_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login-button']")))
    equals_button = driver.find_element(By.CSS_SELECTOR, "[id='login-button']")
    equals_button.click()

    backpack = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-backpack']")))
    backpack = driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-backpack']")
    backpack.click()

    shirt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']")))
    shirt = driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bolt-t-shirt']")
    shirt.click()

    onesie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']")))
    onesie= driver.find_element(By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-onesie']")
    onesie.click()

    basket = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link")))
    basket = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    basket.click()

    checkout = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='checkout']")))
    checkout = driver.find_element(By.CSS_SELECTOR, "[id='checkout']")
    checkout.click()

    first_name = driver.find_element(By.CSS_SELECTOR, '[id="first-name"]')
    first_name.send_keys("Tatiana")

    last_name = driver.find_element(By.CSS_SELECTOR, '[id="last-name"]')
    last_name.send_keys("Kotenko")

    postal_codee = driver.find_element(By.CSS_SELECTOR, '[id="postal-code"]')
    postal_codee.send_keys("283036")

    contin = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='continue']")))
    contin = driver.find_element(By.CSS_SELECTOR, "[id='continue']")
    contin.click()

    text_prise = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    text_prise_value = float(text_prise.split("$")[1])

    assert text_prise_value == 58.29
    driver.quit()
