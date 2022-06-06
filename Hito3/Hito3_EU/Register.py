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
#
def Registro(password,email):

    Opc = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[1]/div[1]/label[1]/span")
    Opc.click()

    Name_key = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[2]/div[1]/input")
    Name_key.send_keys('UDP')

    LastName_key = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[3]/div[1]/input")
    LastName_key.send_keys('Criptografia')

    user = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[4]/div[1]/input")))
    user.send_keys(email)

    password_key = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[5]/div[1]/div/input")
    password_key.send_keys(password)
    driver.save_screenshot("registro/"+"sc"+".png")

    submit = driver.find_element(By.XPATH, value="/html/body/main/section/div[1]/div/div/section/section/section/form/footer/button")
    submit.click()

    driver.save_screenshot("registro/"+"sc_f"+".png")
    time.sleep(2)