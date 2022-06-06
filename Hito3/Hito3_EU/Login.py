from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Driver.driver
wait = WebDriverWait(driver, 10)

def Login(password,email):
    
    user = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[1]/div[1]/input")
    user.send_keys(email)
    time.sleep(1)

    password_key = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[2]/div[1]/div/input")
    password_key.send_keys(password)
    driver.save_screenshot("Login/"+"sc"+".png")
    time.sleep(1)

    submit = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/footer/button")
    submit.click()
    time.sleep(1)
    driver.save_screenshot("Login/"+"sc_f"+".png")
    time.sleep(2)