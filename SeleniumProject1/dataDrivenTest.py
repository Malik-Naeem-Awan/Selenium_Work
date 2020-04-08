from selenium import webdriver
import XLUtils
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path = "C://login1.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    print(driver.title)
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element_by_link_text("Home").click()