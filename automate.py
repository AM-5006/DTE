from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
import json

# Get the credentials stored in json file
with open('token.json') as token:
    data = json.load(token)
    access_token = data["access_token"]
    page_id = data["page_id"]
    message = data["message"]

url = "http://127.0.0.1:5000"
driver = webdriver.Firefox()
driver.get(url)

# Find the form elements
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "exampleInputEmail1")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "exampleInputPassword1")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "exampleFormControlTextarea1")))
    access_token_input = driver.find_element(By.ID,"exampleInputEmail1")
    page_id_input = driver.find_element(By.ID,"exampleInputPassword1")
    message_input = driver.find_element(By.ID,"exampleFormControlTextarea1")

    # Fill in the form
    access_token_input.send_keys(access_token)
    page_id_input.send_keys(page_id)
    message_input.send_keys(message)
    
    # Submit the form
    submit_button = driver.find_element(By.ID,"submit")
    submit_button.click()

    # Go back to index page
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "back")))
    back_button = driver.find_element(By.ID,"back")
    back_button.click()
except Exception as e:
    print(e)
finally:
    driver.quit()

