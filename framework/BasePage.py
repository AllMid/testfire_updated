from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import abc


#creating a base class in base page
class BasePage(abc.ABC):                     

    #initialization of the web driver and the URL of the web resource
    def __init__(self, pagename, uniq_elem_locator):
        self.pagename = pagename
        self.uniq_elem_loc = uniq_elem_locator        
                   



    #search for a specific element of a web resource by locator
    def find_element(self, browser, locator,time=10):
        return WebDriverWait(browser,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    #search for the absence of a certain element of a web resource by locator
    def find_missing_element(self, browser, locator,time=10):
        return WebDriverWait(browser,time).until_not(EC.presence_of_element_located(locator), message=f"the element by the locator {locator} is present")

    #search for several specific elements of a web resource by locator
    def find_elements(self, browser, locator,time=10):
        return WebDriverWait(browser,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")


    
    #creates a string alert_txt, where it is indicated that alert_no (missing), 
    #then a search is performed and, if alert is found, the string changes to allert_yes
    def find_element_alert(self, browser):
            return WebDriverWait(browser, 3).until_not(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear')

        