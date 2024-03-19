import Singleton
import BrowserFactory

class Browser(Singleton):
    def browser(options):
        driver = BrowserFactory(options)
        return driver