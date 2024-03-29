from selenium import webdriver
import logging

class BrowserFactory(object):
    def browser_change(browser_type):
        logging.info(f'the {browser_type} browser is selected')
        if browser_type == 'Chrome':
            return webdriver.Chrome()
        elif browser_type == 'Edge':
            return webdriver.Edge()
        elif browser_type == 'Firefox':
            return webdriver.Firefox()
        elif browser_type == 'Safari':
            return webdriver.Safari()
        