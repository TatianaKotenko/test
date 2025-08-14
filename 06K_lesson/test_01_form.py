from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)

from time import sleep
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.implicitly_wait(10)

search_box = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
search_box.send_keys("Иван")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
search_box.send_keys("Петров")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
search_box.send_keys("Ленина, 55-3")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
search_box.send_keys("test@skypro.com")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
search_box.send_keys("+7985899998787")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
search_box.send_keys("")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
search_box.send_keys("Москва")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
search_box.send_keys("россия")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
search_box.send_keys("QA")

search_box = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
search_box.send_keys("SkyPro")


submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3')
submit.send_keys(Keys.END)

WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3')))
submit.click()

zip_code = driver.find_element(By.ID, "zip-code").get_attribute("class")
assert "alert-danger" in zip_code

poles = ["first-name", "last-name", "e-mail", "phone", "city", "country", "job-position", "company"]

for pole in poles:
    pole_class = driver.find_element(By.ID, pole).get_attribute("class")
    assert "alert-success" in pole_class

driver.quit()
