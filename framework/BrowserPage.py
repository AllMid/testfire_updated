from framework.BrowserFactory import BrowserFactory
from framework.Singleton import Singleton

class BrowserPage(metaclass=Singleton):

    def browserpage(self, options):
        driver = BrowserFactory.browserfactory(options)
        return driver
    
    #switching to an initialized URL using an initialized web driver
    def go_to_site(self, browser, url_address):
        return browser.get(url_address)