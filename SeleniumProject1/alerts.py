from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()


time.sleep(5)

# driver.switch_to_alert().accept()
driver.switch_to.alert().dismiss()




