from .Pages.LoginPage import Login_page
from .Pages.MainPage import Main_page
from framework.Browser import Browser
import tests.variables

import pytest
import logging


#the test goes to the site, enters a username in the username field, enters an sql injection in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
@pytest.mark.parametrize("username,password", [("Admin", "' or 1=1--+"), ("admin' or 1=1--+", "passwd")])
def test_sql_injections_field(browser, username, password):
    logging.info(f'Start Test with {username} and {password} in form')
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    go_to_login_page = Browser()
    go_to_login_page.go_to_site(browser, tests.variables.base_url)
    auth_page.enter_username(username, browser)
    auth_page.enter_password(password, browser)
    auth_page.click_on_the_login_button(browser)
    logging.info(f'Finish Test with {username} and {password}')
    assert auth_page.find_missing_element(browser, Main_page.LOCATOR_TEXT_CONGRATULATIONS) is False
    

#the test goes to the site, enters an sql injection in the search bar, clicks on the Go button and checks the address of the web page
    
def test_sql_injections_search(browser):
    logging.info('Start Test with SQL_injection in search')
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    go_to_login_page = Browser()
    go_to_login_page.go_to_site(browser, tests.variables.base_url)
    auth_page.enter_search("' or 1=1--+", browser)
    auth_page.click_on_the_search_button(browser)
    logging.info('Finish Test with SQL_injection in search')
    assert auth_page.find_missing_element(browser, Main_page.LOCATOR_TEXT_CONGRATULATIONS)
    


@pytest.mark.parametrize("username,password", [("Admin", "<script>alert(123)</script>"), ("<script>alert(123)</script>", "passwd")])
def test_xss_injections_field(browser, username, password):
    logging.info(f'Start Test with {username} and {password} in form')
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    go_to_login_page = Browser()
    go_to_login_page.go_to_site(browser, tests.variables.base_url)
    auth_page.enter_username(username, browser)
    auth_page.enter_password(password, browser)
    auth_page.click_on_the_login_button(browser)
    logging.info(f'Finish Test with {username} and {password}')
    assert auth_page.find_element_alert(browser) is False
    

        #the test goes to the site, enters an xss injection in the search bar, 
        #clicks on the Go button and checks if there is an alert or not
def test_xss_injections_search(browser):
    logging.info('Start Test with XSS_Alert in search')
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    go_to_login_page = Browser()
    go_to_login_page.go_to_site(browser, tests.variables.base_url)
    auth_page.enter_search("<script>alert(123)</script>", browser)
    auth_page.click_on_the_search_button(browser)
    logging.info('Finish Test with XSS_Alert in search')
    assert auth_page.find_element_alert(browser) is False
    


    #selenium.common.exceptions.TimeoutException: