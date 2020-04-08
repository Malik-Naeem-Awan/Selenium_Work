from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# Working with the Radio Buttons

status = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()


print(status)

driver.find_element_by_id('RESULT_CheckBox-8_0').click()

status = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()


print(status)




