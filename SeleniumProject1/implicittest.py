from  selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()
