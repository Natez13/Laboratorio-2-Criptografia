from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Lost(email):
    time.sleep(3)
    driver.save_screenshot("LostPass/"+"sc"+".png")
    user = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/form/p[2]/input")
    user.send_keys(email)
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/form/p[3]/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("LostPass/"+"sc_f"+".png")
    time.sleep(3)