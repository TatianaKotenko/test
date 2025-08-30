from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


path = r'C:/Users/tatti/Desktop/Driver/msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)

driver.get(" http://uitestingplayground.com/dynamicid")
sleep(3)
search_box = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]").click()

sleep(5)
