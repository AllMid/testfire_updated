import logging

from framework.BrowserFactory import BrowserFactory
from framework.Singleton import Singleton

class Browser(metaclass=Singleton):

    driver_variable = None

    def browserpage(self, options, driver_variable):
        logging.info(f'driver variable before startup = {driver_variable}')
        if driver_variable == None:
            driver = BrowserFactory.browser_change(options)
            driver_variable = driver
            logging.info(f'driver variable after startup = {driver_variable}')
            return driver
    
    #switching to an initialized URL using an initialized web driver
    def go_to_site(self, browser, url_address):
        logging.info(f'going to the site by url{url_address}')
        return browser.get(url_address)