from ast import For
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

    wait = WebDriverWait(driver, 10)
    mail = "23j84d@mail.org"
    print("Go to Selenium")
    driver.maximize_window()
    print("Go to Web")
    print("Mail: ",mail)

    #navigate to browserstack.com
    driver.get("https://redsale.cl/")
    print("In Web")


    #Login
    to_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/section[3]/div/div/div[4]/div/div/div/div/div/a")))
    to_account.click()
    
    for i in range(100):
        Login.Login(password,mail)
     

finally:
    driver.close()
    driver.quit()
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser

print("Test Execution Successfully Completed!")
