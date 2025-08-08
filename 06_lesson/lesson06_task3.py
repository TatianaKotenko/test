from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waiter = WebDriverWait(driver, 30) 

img = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape")))

img=driver.find_element(By.CSS_SELECTOR, '#award')
print(img.get_attribute("src"))

driver.quit()
