# Import the selenium library
from selenium import webdriver

# Specify the path to the Chrome driver (change it according to your system)
driver_path = "C:/Users/username/Downloads/chromedriver.exe"

# Create a driver object
driver = webdriver.Chrome(driver_path)

# Use the driver to open a web page
driver.get("https://www.example.com