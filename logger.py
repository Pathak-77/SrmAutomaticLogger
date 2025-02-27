import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up WebDriver
service = Service(executable_path="msedgedriver.exe")

options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-errors') 

driver = webdriver.Edge(service=service, options=options)

# Open  portal
driver.get(os.getenv("url"))

time.sleep(2)  # Give time for the page to load

# Check network status
try:
    network_element = driver.find_element(By.CLASS_NAME, "usercheck_title_class")
    network_type = network_element.text.strip()
except Exception as e:
    print("Error finding network status:", e)
    driver.quit()
    exit()

# Login function
def login():
    try:
        login_button = driver.find_element(By.CLASS_NAME, "button")
        login_button.click()
        time.sleep(1)

        username = driver.find_element(By.ID, "LoginUserPassword_auth_username")
        username.clear()
        username.send_keys(os.getenv("id"))

        password = driver.find_element(By.ID, "LoginUserPassword_auth_password")
        password.clear()
        password.send_keys(os.getenv("pass") + Keys.ENTER)

        print("Login successful!")
    except Exception as e:
        print("Login failed:", e)

# Logout function
def logout():
    try:
        logout_button = driver.find_element(By.ID, "UserCheck_Logoff_Button")
        logout_button.click()
        print("Logged out successfully!")
    except Exception as e:
        print("Logout failed:", e)

# Decision based on network status
if "Network Access Login" in network_type:
   login()

elif "Network Access Granted" in network_type:
    logout()
    time.sleep(2)
    login()

# Wait before quitting
time.sleep(3)
driver.quit()
