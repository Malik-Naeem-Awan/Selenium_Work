from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)


driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")

driver.find_element_by_link_text("WebDriver").click()

time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
