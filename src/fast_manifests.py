from selenium import webdriver
# from selenium.webdriver.common import Keys
# from selenium.webdriver.common import By


# For protect web to auto close
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = option)

driver.get("https://wms-th.luxola.com")