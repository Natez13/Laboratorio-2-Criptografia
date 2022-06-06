from re import I
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

with open("Data.json", "r") as read_file:
    data_json = json.load(read_file)
#maximize the window size
#user = json.loads(data_json)

#print(data_json)
print(data_json['Users_1'][0])

driver.maximize_window()
time.sleep(3)
#navigate to browserstack.com
driver.get("http://app.gestago.cl/admin/v1.1/#/login")
driver.save_screenshot("SC/"+"sc0.png")
time.sleep(2)
for i in range(2):
    time.sleep(4)
    user = driver.find_element(By.XPATH, value="/html/body/div/section/div/div/div[1]/md-input-container/input")
    user.send_keys((data_json['Users_3'][i]['user']))
    time.sleep(1)
    password = driver.find_element(By.XPATH, value="/html/body/div/section/div/div/div[2]/md-input-container/input")
    password.send_keys((data_json['Users_3'][i]['pass']))
    driver.save_screenshot("SC_2/"+"sc"+str(i+1)+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/div/section/div/div/div[4]/button")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("SC_2/"+"sc_f"+str(i+1)+".png")
    time.sleep(4)

#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")