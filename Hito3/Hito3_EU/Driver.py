from selenium import webdriver

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options)
#driver = webdriver.Chrome(executable_path=r"/home/informatica/Downloads/chromedriver_linux64/chromedriver")