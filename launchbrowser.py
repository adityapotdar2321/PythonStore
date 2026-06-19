from selenium import webdriver

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.boodmo.com")

# Optional: maximize window
driver.maximize_window()

# Close the browser after 5 seconds
import time
time.sleep(5)
driver.quit()

