from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://www.expedia.com/")

driver.find_element_by_id("tab-flight-tab-hp").click()
time.sleep(2)             # from python

driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)             # from python
driver.find_element_by_id("flight-destination-hp-flight").clear()
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")
driver.find_element_by_id("flight-departing-hp-flight").click()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/2020")
driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("18/10/2020")
time.sleep(2)             # from python

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

# Explicit waits
wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()

time.sleep(3)

driver.quit()
