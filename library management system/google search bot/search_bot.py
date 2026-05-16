from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait 2 seconds
time.sleep(2)

# Find Google Search Box
search_box = driver.find_element(By.NAME, "q")

# Type Search Keyword
search_box.send_keys("South Africa vs Australia latest news")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait for Results
time.sleep(3)

# Click First Search Result
first_result = driver.find_element(By.TAG_NAME, "h3")
first_result.click()

 