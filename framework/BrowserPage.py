from framework.BrowserFactory import BrowserFactory

class BrowserPage(object):

    def browserpage(options):
        driver = BrowserFactory.browserfactory(options)
        return driver
    
        