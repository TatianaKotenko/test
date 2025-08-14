from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)


driver.get(" http://uitestingplayground.com/classattr")

sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-test").click()
sleep(5)
