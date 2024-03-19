from framework.BasePage import BasePage
from selenium.webdriver.common.by import By


#creating a subclass, with BasePage as the parent
class Login_page(BasePage):
    
    base_url = 'https://testfire.net/login.jsp'

    #localization of the search bar by xpath in the code of a web resource
    LOCATOR_SEARCH_FIELD = (By.XPATH, '//*[@id="query"]')
    #localization of the search button by xpath in the code of a web resource
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "//*[@id='frmSearch']/table/tbody/tr[1]/td[2]/input[2]")
    #localization of the username input string by xpath in the code of a web resource
    LOCATOR_USERNAME_FIELD = (By.XPATH, '//*[@id="uid"]')
    #localization of the password input string by xpath in the code of a web resource
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="passw"]')
    #localization of the Login button by xpath in the code of a web resource
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/table/tbody/tr[3]/td[2]/input')

    LOCATOR_FAIL_TEXT = (By.XPATH, '//*[@id="_ctl0__ctl0_Content_Main_message"]')

    #entering in the "username" field
    def enter_username(self, word):
        search_field = self.find_element(Login_page.LOCATOR_USERNAME_FIELD)
        search_field.click()
        search_field.send_keys(word)
        
    #entering in the "password" field
    def enter_password(self, word):
        search_field = self.find_element(Login_page.LOCATOR_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(word)
   
    
    #entering in the "search" field
    def enter_search(self, word):
        search_field = self.find_element(Login_page.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)


    #clicks on the "Login" button
    def click_on_the_login_button(self):
        self.find_element(Login_page.LOCATOR_LOGIN_BUTTON,time=2).click()

    #clicks on the "Go" button
    def click_on_the_search_button(self):
        self.find_element(Login_page.LOCATOR_SEARCH_BUTTON).click()


