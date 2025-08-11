from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
delay_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
delay_input.clear()
delay_input.send_keys("45")

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()

submit = driver.find_element(By.CSS_SELECTOR, 'span.btn.btn-outline-warning')
submit.send_keys(Keys.END)

waiter = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn.btn-outline-warning')))
submit.click()

#equals_button = WebDriverWait(driver, 20).until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn.btn-outline-warning")))
#
# equals_button.click()

#driver.find_element(By.XPATH, "//span[text()='span.btn.btn-outline-warning']").click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".skreen")))

element = WebDriverWait(driver, 60).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".skreen")), "15")
    
result = driver.find_element(By.CSS_SELECTOR, ".skreen").text
assert result =="15"

driver.quit()
