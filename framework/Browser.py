from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

from framework.BrowserFactory import BrowserFactory
from framework.Singleton import Singleton

class Browser(metaclass=Singleton):

    driver_variable = None

    def browserpage(self, browser_type, driver_variable):
        logging.info(f'driver variable before startup = {driver_variable}')
        if driver_variable == None:
            driver = BrowserFactory.browser_change(browser_type)
            driver_variable = driver
            logging.info(f'driver variable after startup = {driver_variable}')
            return driver
    
    #switching to an initialized URL using an initialized web driver
    def go_to_site(browser, url_address):
        logging.info(f'going to the site by url {url_address}')
        return browser.get(url_address)
    
        #search for a specific element of a web resource by locator
    def find_element(browser, locator,time=10):
        return WebDriverWait(browser,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    #search for several specific elements of a web resource by locator
    def find_missing_element(browser, locator,time=10):
        try:
            WebDriverWait(browser,time).until(EC.presence_of_element_located(locator), message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            return True
        else:
            return False

    #creates a string alert_txt, where it is indicated that alert_no (missing), 
    #then a search is performed and, if alert is found, the string changes to allert_yes
    def find_missing_alert(browser):
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear')
        except TimeoutException:
            return True
        else:
            return False