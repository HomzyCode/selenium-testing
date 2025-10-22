from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Use full path to chromedriver (works for Apple Silicon)
service = Service(executable_path="/opt/homebrew/bin/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()
