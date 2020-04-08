from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")


print("The Number of links in website: ", len(links))


for link in links:
    print(link.text)

# clicking on the link :

# driver.find_element(By.LINK_TEXT, "REGISTER").click()


driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()