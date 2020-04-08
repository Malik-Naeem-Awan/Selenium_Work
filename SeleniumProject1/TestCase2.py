import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the Page is : " + self.driver.title)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.get("https://bing.com/")
        print("Title of the Page is : " + self.driver.title)
        self.driver.close()

if __name__ =="__main__":
    unittest.main()
