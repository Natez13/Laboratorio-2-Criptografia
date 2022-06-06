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

def Recover():
    newpass = '!123_ABCDE_FGHIXZG'
    time.sleep(1)
    password_key = driver.find_element(By.XPATH, value="/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/form/p[2]/span/input")
    password_key.send_keys(newpass)
    time.sleep(1)
    password_key_new = driver.find_element(By.XPATH, value="/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/form/p[3]/span/input")
    password_key_new.send_keys(newpass)
    driver.save_screenshot("RecoverPass/"+"sc"+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/form/p[4]/button")
    submit.click()
    time.sleep(1)
    driver.save_screenshot("RecoverPass/"+"sc_f"+".png")
    time.sleep(2)

    return newpass
