from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)
print(driver.title)

driver.back()

print(driver.title)
driver.forward()

print(driver.title)