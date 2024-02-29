from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = 'https://demoqa.com/dynamic-properties'
driver.get(url)
color_change = driver.find_element(By.CSS_SELECTOR, "#colorChange")
val_css_property = color_change.value_of_css_property('color')
time.sleep(6)
color_change1 = driver.find_element(By.CSS_SELECTOR, "#colorChange")
val_css_property1 = color_change.value_of_css_property('color')


print(val_css_property)
print(val_css_property1)

driver.quit()
