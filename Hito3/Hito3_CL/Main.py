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

    wait = WebDriverWait(driver, 10)
    mail = Email.GenerteRandomEmail()
    print("Go to Selenium")
    driver.maximize_window()
    print("Go to Web")
    print("Mail: ",mail)

    #navigate to browserstack.com
    driver.get("https://redsale.cl/")
    print("In Web")

    #Registro
    to_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/section[3]/div/div/div[4]/div/div/div/div/div/a")))
    to_account.click()
    to_register =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/a")))
    to_register.click()
    Register.Registro(mail)
    print(Email.EmailList(mail))
    to_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/section[3]/div/div/div[4]/div/div/div/div/div/a")))
    to_account.click()
    exit_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/section/div/div/div[1]/div/div/div[2]/div/div/a")))
    exit_account.click() 
    time.sleep(2)
    #Login
    to_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/section[3]/div/div/div[4]/div/div/div/div/div/a")))
    to_account.click()
    #23j84d@1secmail.org
    mail_pass = Email.EmailList(mail)
    mail_pass_id = mail_pass[0]
    print(mail_pass_id)
    mail_id = mail_pass_id["id"]
    print(mail_id)
    all_mail = Email.ReadEMail(mail,mail_id)
    body = all_mail["body"]
    #print(body)
    limit_down = body.find("ente: <strong>")+14
    limit_up = body.find("</strong></p>")
    actual_pass = body[limit_down:limit_up]
    print(actual_pass)
    Login.Login(actual_pass,mail)

    #Change Password
    Change_Pass =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/nav/ul/li[5]/a")))
    Change_Pass.click()
    time.sleep(1)
    ChangePass.Change(actual_pass)
    time.sleep(1)
    exit_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/nav/ul/li[6]/a")))
    exit_account.click() 

    #Reset Password
    Reset_account =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div[1]/div/div/section/div/div/div[1]/div/div/div[4]/div/div/div/form/p[4]/a")))
    Reset_account.click()
    Lost.Lost(mail)
    time.sleep(1)
    print(Email.EmailList(mail))
    
    #Recover Password
    #23j84d@1secmail.org
    #mail = "23j84d@1secmail.org"
    mail_pass = Email.EmailList(mail)
    print(mail_pass)
    mail_pass_id = mail_pass[0]
    print(mail_pass_id)
    mail_id = mail_pass_id["id"]
    print(mail_id)
    all_mail = Email.ReadEMail(mail,mail_id)
    body = all_mail["body"]
    #print(body)
    limit_down = body.find('"link" href="')+13
    limit_up = body.find('" style="font-weight: normal; text-decoration: underline; color:')
    url = body[limit_down:limit_up]
    url = url.replace('amp;', '')
    print(url)
    driver.get(url)
    RecoverPass.Recover()

    
finally:
    driver.close()
    driver.quit()
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser

print("Test Execution Successfully Completed!")
