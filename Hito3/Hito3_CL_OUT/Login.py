from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Login(password,email):
    time.sleep(3)
    user = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/form/p[1]/input")
    user.send_keys(email)
    time.sleep(1)
    password_key = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/form/p[2]/span/input")
    password_key.send_keys(password)
    driver.save_screenshot("Login/"+"sc"+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/form/p[4]/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("Login/"+"sc_f"+".png")
    time.sleep(3)