from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import BasePage

from Browser import Browser
class BaseElements(BasePage):
    #search for a specific element of a web resource by locator
    def find_element(locator,time=10):
        return WebDriverWait(Browser.driver,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    #search for the absence of a certain element of a web resource by locator
    def find_missing_element(locator,time=10):
        return WebDriverWait(Browser.driver,time).until_not(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    #search for several specific elements of a web resource by locator
    def find_elements(locator,time=10):
        return WebDriverWait(Browser.driver,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    
    #creates a string alert_txt, where it is indicated that alert_no (missing), 
    #then a search is performed and, if alert is found, the string changes to allert_yes
    def find_element_alert():
        return WebDriverWait(Browser.driver, 3).until_not(EC.alert_is_present(), 'Timed out waiting for confirmation popup to appear')
