from  selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

user_ele=driver.find_element_by_name("userName")

print(user_ele.is_displayed())     # returns true/false based of element status
print(user_ele.is_enabled())



pwd_ele=driver.find_element_by_name("password")

print(pwd_ele.is_displayed())     # returns true/false based of element status
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")


driver.find_element_by_name("login").click()


roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())  # print status of radio button roundtrip

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print(onetrip_radio.is_selected())  # print status of radio button roundtrip

