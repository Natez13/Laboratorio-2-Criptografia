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

def Change(password):
    newpass = '!123_ABCDE_FGHIXZ'
    time.sleep(1)
    password_key = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/form/section/div[5]/div[1]/div/input")
    password_key.send_keys(password)
    time.sleep(1)
    password_key_new = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/form/section/div[6]/div[1]/div/input")
    password_key_new.send_keys(newpass)
    driver.save_screenshot("ChangePass/"+"sc"+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/form/footer/input")
    submit.submit()
    time.sleep(1)
    driver.save_screenshot("ChangePass/"+"sc_f"+".png")
    time.sleep(2)

    return newpass
