from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


path = r'C:/Users/tatti/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe'
service = Service(executable_path=path)
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Sky")
sleep(3)

search_box.clear()

search_box = driver.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Pro")
sleep(3)

driver.quit()
