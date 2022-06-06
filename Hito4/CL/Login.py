from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Login(password,email):
    time.sleep(2)
    user = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/section/div/div/div[1]/div/div/div[2]/div/form/div/div[1]/input")
    user.send_keys(email)
    time.sleep(1)
    password_key = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/section/div/div/div[1]/div/div/div[2]/div/form/div/div[2]/input")
    password_key.send_keys(password)
    time.sleep(1)
    submit = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/section/div/div/div[1]/div/div/div[2]/div/form/div/div[4]/button")
    submit.click()
    time.sleep(2)