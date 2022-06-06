from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Lost(email):
    time.sleep(1)
    user = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/form/section/div/div/input")
    user.send_keys(email)
    driver.save_screenshot("LostPass/"+"sc"+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/form/section/div/button[1]")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("LostPass/"+"sc_f"+".png")
    time.sleep(2)