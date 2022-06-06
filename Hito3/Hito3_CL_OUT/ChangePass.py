from multiprocessing.connection import wait
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Driver

driver = Driver.driver

def Change(password):
    newpass = '!123_ABCDE_FGHIXZ'
    time.sleep(3)
    password_key = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/fieldset/p[1]/span/input")
    password_key.send_keys(password)
    time.sleep(2)
    Name_key = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/p[1]/input")
    Name_key.send_keys('UDP')
    time.sleep(2)
    LastName_key = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/p[2]/input")
    LastName_key.send_keys('Criptografia')
    time.sleep(2)
    password_key_new = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/fieldset/p[2]/span/input")
    password_key_new.send_keys(newpass)
    time.sleep(2)
    password_key_new_conf = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/fieldset/p[3]/span/input")
    password_key_new_conf.send_keys(newpass)
    time.sleep(2)
    driver.save_screenshot("ChangePass/"+"sc"+".png")
    submit = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/div/div/div/div/form/p[5]/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("ChangePass/"+"sc_f"+".png")
    time.sleep(3)

    return newpass