from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Use full path to chromedriver (works for Apple Silicon)
driver = webdriver.Chrome()
driver.get("https://google.com")

# find search field, type, and enter
# will look for the element specified by the class name to access and interact
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("tech with tim" + Keys.ENTER)

# test test 

time.sleep(10)

driver.quit()