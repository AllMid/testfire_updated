from selenium import webdriver

class BrowserFactory(object):
    def browserfactory(options):
        if options == 'Chrome':
            return webdriver.Chrome()
        elif options == 'Edge':
            return webdriver.Edge()
        elif options == 'Firefox':
            return webdriver.Firefox()
        elif options == 'Safari':
            return webdriver.Safari()
        