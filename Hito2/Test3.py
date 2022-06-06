from re import I
import time
import json
from selenium.webdriver.common.by import By

from selenium import webdriver

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
#Usando Docker:
"""
#driver = webdriver.Remote(
#command_executor='http://localhost:4444/wd/hub',
#options=options)
"""
driver = webdriver.Chrome(executable_path=r"/chromedriver")


with open("Data.json", "r") as read_file:
    data_json = json.load(read_file)
#maximize the window size
#user = json.loads(data_json)

#print(data_json)
print(data_json['Users_1'][0])

driver.maximize_window()
time.sleep(3)
#navigate to browserstack.com
driver.get("https://db.inf.uct.cl/phpMyAdmin/")
driver.save_screenshot("SC/"+"sc0.png")
time.sleep(2)
time.sleep(4)
user = driver.find_element(By.XPATH, value="/html/body/div/div/form/fieldset[1]/div[1]/input")
user.send_keys((data_json['Users_2'][0]['user']))
time.sleep(1)
password = driver.find_element(By.XPATH, value="/html/body/div/div/form/fieldset[1]/div[2]/input")
password.send_keys((data_json['Users_2'][0]['pass']))
driver.save_screenshot("SC_3/"+"sc"+str(1)+".png")
time.sleep(2)
submit = driver.find_element(By.XPATH, value="/html/body/div/div/form/fieldset[2]/input[1]")
submit.click()
time.sleep(2)
driver.save_screenshot("SC_3/"+"sc_f"+str(1)+".png")
time.sleep(4)

#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
