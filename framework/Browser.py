from BrowserFactory import BrowserFactory

class Browser(object):

    def browser(options):
        driver = BrowserFactory(options)
        return driver
    
        #switching to an initialized URL using an initialized web driver
    def go_to_site(base_url):
        return Browser.driver.get(base_url)