from multiprocessing.connection import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver
import Login
import string

driver = Driver.driver
password = '!123_ABCDE_FGHI'
try: 

    print("Go to Selenium")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    print("Go to Web")
    
    #navigate to browserstack.com
    driver.get("https://crashcomics.es/es/")
    print("In Web")
    mail = "detavav333@musezoo.com"
    print("MAIL: ",mail)
    to_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    to_account.click()
    Login.Login(password,mail)
    for i in range(100):
        Login.Login2(password)
    #time.sleep(2)

finally:
    driver.close()
    driver.quit()
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser

print("Test Execution Successfully Completed!")
