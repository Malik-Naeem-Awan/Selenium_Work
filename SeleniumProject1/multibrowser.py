from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)     # title of the page
print(driver.current_url)  # Return the current Url

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# driver.close() # close the browser