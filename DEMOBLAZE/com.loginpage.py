from selenium import webdriver
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.demoblaze.com")

# Optional: maximize window
driver.maximize_window()

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
