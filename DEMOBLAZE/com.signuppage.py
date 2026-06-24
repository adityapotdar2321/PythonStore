from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.demoblaze.com")

# Optional: maximize window
driver.maximize_window()

# Wait for 5 seconds
time.sleep(5)

# Click on the "Sign up" button
driver.find_element(By.XPATH, "//a[@id='signin2']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='sign-username']").send_keys("aditya")
# Wait a bit to observe the modal
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='sign-password']").send_keys("Aditya2321!")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@onclick='register()']").click()
# Close the browser
driver.quit()
