from multiprocessing.connection import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
import Email
import Register
import Driver
import Login
import Lost
import ChangePass
import string
import RecoverPass
driver = Driver.driver
password = '!123_ABCDE_FGHI'
try: 

    print("Go to Selenium")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    print("Go to Web")
    
    #navigate to browserstack.com
    driver.get("https://crashcomics.es/es/")
    print("In Web")
    mail = Email.GenerteRandomEmail()
    print("MAIL: ",mail)
    to_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    to_account.click()
    
    
    # Registro
    print("Inciando Registro")
    to_register = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[1]/div/div/section/section/div/a")))
    to_register.click()
    Register.Registro(password,mail)
    print(Email.EmailList(mail))
    time.sleep(1)
    exit_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    exit_account.click() 
    print("Registro Exitoso")

    
    #Login
    print("Inciando Logueo")
    to_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    to_account.click()
    
    Login.Login(password,mail)
    time.sleep(2)
    exit_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    exit_account.click()
    print("Logueo Exitoso")

    

    #Change Password
    print("Cambiando Contraseña")
    to_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    to_account.click()
    Login.Login(password,mail)
    Change_Pass =wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[1]/div/div/section/section/div/div/a[1]")))
    Change_Pass.click()
    time.sleep(1)
    ChangePass.Change(password)
    time.sleep(1)
    exit_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/nav/div/ul/li[4]/a")))
    exit_account.click()
    print("Cambio Exitoso")


    #Reset Password
    print("Recuperacion de Contraseña")
    Reset_account = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[1]/div/div/section/section/section/form/section/div[3]/a")))
    Reset_account.click()
    Lost.Lost(mail)
    """
    time.sleep(1)
    mail_pass = Email.EmailList(mail)
    print(mail_pass)
    mail_pass_id = mail_pass[0]
    print(mail_pass_id)
    mail_id = mail_pass_id["id"]
    print(mail_id)
    all_mail = Email.ReadEMail(mail,mail_id)
    body = all_mail["body"]
    limit_down = body.find("https://crashcomics.es/es/recuperar-contraseña?")
    limit_up = body.find(" style=\"color:#337ff1\">https://crashcomics.es/es/recuperar-contraseña")-1
    url = body[limit_down:limit_up]
    print(url)
    driver.get(url)
    
    RecoverPass.Recover()
    """
    #time.sleep(2)

finally:
    driver.close()
    driver.quit()
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser

print("Test Execution Successfully Completed!")
