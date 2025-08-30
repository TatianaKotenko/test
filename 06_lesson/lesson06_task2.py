from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)

waiter = WebDriverWait(driver, 20)
driver.get("http://uitestingplayground.com/textinput")

search_box = driver.find_element(By.CSS_SELECTOR, '[id="newButtonName"]')
search_box.send_keys("SkyPro")

waiter.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[id = "updatingButton"]')))
updatingButton = driver.find_element(By.CSS_SELECTOR, '[id="updatingButton"]')
updatingButton.click()

waiter = WebDriverWait(driver, 30)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[id = "updatingButton"]'), "SkyPro"))
txt = driver.find_element(By.CSS_SELECTOR, '[id ="updatingButton"]').text
print(txt)

driver.quit()
