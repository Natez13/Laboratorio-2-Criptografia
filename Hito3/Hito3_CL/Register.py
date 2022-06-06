from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Registro(email):
    time.sleep(2)
    user = driver.find_element(By.XPATH, value="/html/body/main/div/div[1]/div/div/section/div/div/div/div/div/div/div/div[2]/form/p[1]/input")
    user.send_keys(email)
    time.sleep(1)
    driver.save_screenshot("registro/"+"sc"+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/main/div/div[1]/div/div/section/div/div/div/div/div/div/div/div[2]/form/p[2]/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("registro/"+"sc_f"+".png")
    time.sleep(3)