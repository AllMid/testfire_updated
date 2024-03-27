from framework.BasePage import BasePage

from selenium.webdriver.common.by import By


#creating a subclass, with BasePage as the parent
class Login_page(BasePage):
    
    

    #localization of the search bar by xpath in the code of a web resource
    LOCATOR_SEARCH_FIELD = (By.XPATH, "/html/body/div/form/table/tbody/tr/td/input[@type='text']")
    #localization of the search button by xpath in the code of a web resource
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "/html/body/div/form/table/tbody/tr/td/input[@type='submit']")
    #localization of the username input string by xpath in the code of a web resource
    LOCATOR_USERNAME_FIELD = (By.XPATH, "/html/body/table/tbody/tr/td/div/form/table/tbody/tr/td/input[@id='uid']")
    #localization of the password input string by xpath in the code of a web resource
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "/html/body/table/tbody/tr/td/div/form/table/tbody/tr/td/input[@id='passw']")
    #localization of the Login button by xpath in the code of a web resource
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '/html/body/table/tbody/tr/td/div/form/table/tbody/tr/td/input')

    LOCATOR_FAIL_TEXT = (By.XPATH, '/html/body/table/tbody/tr/td/div/p/span/text()')

    #entering in the "username" field
    def enter_username(self, word, browser):
        search_field = self.find_element(browser, Login_page.LOCATOR_USERNAME_FIELD)
        search_field.click()
        search_field.send_keys(word)
        
    #entering in the "password" field
    def enter_password(self, word, browser):
        search_field = self.find_element(browser, Login_page.LOCATOR_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(word)
   
    
    #entering in the "search" field
    def enter_search(self, word, browser):
        search_field = self.find_element(browser, Login_page.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)


    #clicks on the "Login" button
    def click_on_the_login_button(self, browser):
        self.find_element(browser, Login_page.LOCATOR_LOGIN_BUTTON,time=2).click()

    #clicks on the "Go" button
    def click_on_the_search_button(self, browser):
        self.find_element(browser, Login_page.LOCATOR_SEARCH_BUTTON).click()


