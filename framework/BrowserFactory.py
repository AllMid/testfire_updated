from selenium import webdriver
import logging

class BrowserFactory(object):
    def browser_change(options):
        logging.info(f'the {options} browser is selected')
        if options == 'Chrome':
            return webdriver.Chrome()
        elif options == 'Edge':
            return webdriver.Edge()
        elif options == 'Firefox':
            return webdriver.Firefox()
        elif options == 'Safari':
            return webdriver.Safari()
        