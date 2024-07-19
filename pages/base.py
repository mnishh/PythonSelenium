class Basefunction():
    def __init__(self,driver):
        self.driver=driver
       
    def scrollmethod(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def clock(self,element):
        element.click()
        
        
        

