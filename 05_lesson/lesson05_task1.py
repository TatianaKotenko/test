from time import sleep


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(" http://uitestingplayground.com/classattr")

sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-test").click()
sleep(5)
