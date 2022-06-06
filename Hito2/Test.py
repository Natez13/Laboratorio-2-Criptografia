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
driver.get("https://www.probenefit.cl")
driver.save_screenshot("SC/"+"sc0.png")
time.sleep(2)
to_user = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[2]/header/div/div/div[3]/nav/ul/li[5]/div/a/span")
to_user.click()
for i in range(17):
    time.sleep(4)
    user = driver.find_element(By.XPATH, value="/html/body/div/div/div/div/main/article/div/div/div[2]/div[1]/form/div[1]/input")
    user.send_keys((data_json['Users_1'][i]['user']))
    time.sleep(1)
    password = driver.find_element(By.XPATH, value="/html/body/div/div/div/div/main/article/div/div/div[2]/div[1]/form/div[2]/input")
    password.send_keys((data_json['Users_1'][i]['pass']))
    driver.save_screenshot("SC/"+"sc"+str(i+1)+".png")
    time.sleep(2)
    submit = driver.find_element(By.XPATH, value="/html/body/div/div/div/div/main/article/div/div/div[2]/div[1]/form/div[4]/input")
    submit.click()
    time.sleep(2)
    driver.save_screenshot("SC/"+"sc_f"+str(i+1)+".png")
    time.sleep(4)

#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
#time.sleep(10)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
