from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open browser
driver = webdriver.Chrome()

# Go to login page 
driver.get("https://www.fidelity.ca/login")

# Enter username
driver.find_element(By.ID, "username").send_keys("testuser")

# Enter password
driver.find_element(By.ID, "password").send_keys("password1234")

# Click login button
driver.find_element(By.ID, "login-button").click()

# Simple validation (example)
assert "dashboard" in driver.current_url

print("Test Passed")

driver.quit()
