# pages/example_page.py
from selenium.webdriver.common.by import By
from pages.base import Basefunction
import time
class ExamplePage(Basefunction):
    
    def __init__(self,driver):
        super().__init__(driver)
        #self.driver=driver
    
    def search(self):
         elemto = self.driver.find_element(By.XPATH, '//button[text()="Login"]')
         self.clock(elemto)
         #elem = self.driver.find_element(By.XPATH, '//input[@id="mobile-search"]')
         #self.scrollmethod(elemto)
         time.sleep(5)
        #self.scrollmethod(elem)

    
