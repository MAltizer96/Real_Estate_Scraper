import helper_methods
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Main_Selenium():
    driver = None
    currentSelectedElement = None
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.currentSelectedElement = None

    def open_webpage(self, url):

        self.driver.get(url)

        time.sleep(2) 

        self.driver.quit()

    def click_element(self,by, elementname):
        random_delay = 1 + (2 * time.random())
        element= self.driver.find_element(by, elementname)
        element.click()
        self.currentSelectedElement = element
        time.sleep(random_delay)

    def check_element_exists(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False
        
    def type_in_element(self,text):
        if self.currentSelectedElement is None:
            raise Exception("No element selected to type in.")
        
        random_delay = helper_methods.get_random_delay()

        self.currentSelectedElement.send_keys(text)
        time.sleep(random_delay)

        self.currentSelectedElement.send_keys("\n")
        time.sleep(random_delay)