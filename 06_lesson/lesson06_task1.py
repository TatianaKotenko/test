from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)

driver.implicitly_wait(30)
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

driver.quit()
