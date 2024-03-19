from framework.BrowserFactory import BrowserFactory

class Browser(object):

    def browser(options):
        driver1 = BrowserFactory.browserfactory(options)
        return driver1
    
        #switching to an initialized URL using an initialized web driver
    def go_to_site(base_url):
        return browser.driver.get(base_url)