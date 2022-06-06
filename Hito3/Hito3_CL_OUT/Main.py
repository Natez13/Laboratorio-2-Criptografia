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
newpass = '!123_ABCDE_FGHIXZG'
try:
    
    """
    wait = WebDriverWait(driver, 10)
    mail = Email.GenerteRandomEmail()
    print("Go to Selenium")
    driver.maximize_window()
    print("Go to Web")
    print("Mail: ",mail)

    #navigate to browserstack.com
    driver.get("https://neeks.cl/")
    print("In Web")

    #Registro
    to_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/header[1]/div[1]/div/div[2]/div/a[1]/span")))
    to_account.click()
    to_register =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/ul/li[2]/a")))
    to_register.click()
    Register.Registro(password,mail)
    print(Email.EmailList(mail))
    exit_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div/p[1]/a")))
    exit_account.click() 

    #Login
    Login.Login(password,mail)
    exit_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div/p[1]/a")))
    exit_account.click()

    #Reset Password
    Reset_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/form/p[3]/a")))
    Reset_account.click()
    Lost.Lost(mail)
    time.sleep(1)
    print(Email.EmailList(mail))
    
    #Change Password
    driver.get("https://neeks.cl/mi-cuenta/")
    time.sleep(1)
    Login.Login(newpass,mail)
    Change_Pass =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div/nav/ul/li[5]/a")))
    Change_Pass.click()
    time.sleep(1)
    ChangePass.Change(password)
    time.sleep(1)
    """
    #bjvy5t@bheps.com
    mail = "bjvy5t@bheps.com"
    mail_pass = Email.EmailList(mail)
    mail_pass_id = mail_pass[1]
    print(mail_pass_id)
    mail_id = mail_pass_id["id"]
    print(mail_id)
    all_mail = Email.ReadEMail(mail,mail_id)
    body = all_mail["body"]
    print(body)
    limit_down = body.find("https://click.pstmrk.it/2s/neeks.cl%2Fmi-cuenta%2Frecuperar-pass")
    limit_up = body.find("\" style=\"font-weight: normal; text-decoration: underline; color: #609758;\">\t\tHaz clic aquí para restablecer tu contraseña")
    url = body[limit_down:limit_up]
    print(url)
    driver.get(url)
    time.sleep(4)
finally:
    driver.close()
    driver.quit()
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser

print("Test Execution Successfully Completed!")
