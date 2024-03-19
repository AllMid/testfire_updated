from .pages.LoginPage import Login_page
from .pages.MainPage import Main_page
from framework.Browser import Browser

#the test goes to the site, enters a username in the username field, enters an sql injection in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_sql_injections_passwd(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    Browser.go_to_site(Login_page.base_url)
    auth_page.enter_username("admin")
    auth_page.enter_password("' or 1=1--+")
    auth_page.click_on_the_login_button()
    assert auth_page.find_missing_element(Main_page.LOCATOR_TEXT_CONGRATULATIONS) is False

#the test goes to the site, enters an sql injection in the username field, enters a password in the password field,
#clicks the Login button and checks whether the transition to the user's web page has occurred or not
def test_sql_injections_uid(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    Browser.go_to_site(Login_page.base_url)
    auth_page.enter_username("admin' or 1=1--+")
    auth_page.enter_password("passwd")
    auth_page.click_on_the_login_button()
    assert auth_page.find_missing_element(Main_page.LOCATOR_TEXT_CONGRATULATIONS) is False

#the test goes to the site, enters an sql injection in the search bar, clicks on the Go button and checks the address of the web page
def test_sql_injections_search(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON)
    Browser.go_to_site(Login_page.base_url)
    auth_page.enter_search("' or 1=1--+")
    auth_page.click_on_the_search_button()
    assert auth_page.find_missing_element(Main_page.LOCATOR_TEXT_CONGRATULATIONS)