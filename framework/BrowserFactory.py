from selenium import webdriver

class BrowserFactory(object):
    def browserfactory(options):
        if options == 'Chrome':
            driver = webdriver.Chrome()
        elif options == 'Edge':
            driver = webdriver.Edge()
        elif options == 'Firefox':
            driver = webdriver.Firefox()
        elif options == 'Safari':
            driver = webdriver.Safari()
        return driver