from framework.BrowserFactory import BrowserFactory

class Browser(object):

    def browser(options):
        driver = BrowserFactory.browserfactory(options)
        return driver
    
        #switching to an initialized URL using an initialized web driver
    def go_to_site(base_url):
        return Browser.browser.get(base_url)