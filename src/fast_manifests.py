######################################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import keyboard


# For protect web to auto close
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

PATH = (r"C:\Program Files\Google\Chrome\Application\chrome.exe")
service = Service(executable_path=PATH) 


driver = webdriver.Chrome(options = option, service=service)

driver.get("https://wms-th.luxola.com")



#######################################################

