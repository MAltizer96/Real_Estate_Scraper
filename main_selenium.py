import undetected_chromedriver as uc
from setuptools._distutils.version import LooseVersion

import helper_methods
import captcha_solver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

class Main_Selenium():
    driver = None
    currentSelectedElement = None
    def __init__(self):
        # service = Service(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=service)
        self.currentSelectedElement = None
        driver_path = ChromeDriverManager(driver_version="148.0.7778.217").install()
        options = uc.ChromeOptions()
        self.driver = uc.Chrome(options=options, driver_executable_path=driver_path)

    def open_webpage(self, url):
        self.driver.maximize_window()
        self.driver.get("Http://www.google.com")
        helper_methods.wait_time(helper_methods.get_short_random_delay())

        self.driver.get(url)

        helper_methods.wait_time(helper_methods.get_short_random_delay())

        captcha_solver.check_for_captcha(self.driver)

    def click_element_by_aria_label(self, elementname, offset=0):

        random_delay = helper_methods.get_short_random_delay()
        element = self.driver.find_element(
            By.XPATH, 
            f"//input[contains(@aria-label, '{elementname}')]"
        )
        if element is not None:
            helper_methods.move_mouse_to_element(element, y_offset=offset)

        helper_methods.click_element()

        self.currentSelectedElement = element
        print(f"Clicked element with label: {elementname}")
        helper_methods.wait_time(random_delay)

    def check_element_exists(self, value):
        captcha_solver.check_for_captcha(self.driver)
        try:
            self.driver.find_element(By.ID, value)
            return True
        except:
            return False
        
    def type_in_element(self,text):
        captcha_solver.check_for_captcha(self.driver)

        if self.currentSelectedElement is None:
            raise Exception("No element selected to type in.")

        random_delay = helper_methods.get_short_random_delay()
        #self.currentSelectedElement.send_keys(text)
        helper_methods.wait_time(random_delay)
 
        random_delay = helper_methods.get_short_random_delay()
        for char in text:
            random_delay = helper_methods.get_short_random_delay()
            self.currentSelectedElement.send_keys(char)
            helper_methods.wait_time(random_delay)
        self.currentSelectedElement.send_keys("\n")
        helper_methods.wait_time(random_delay)