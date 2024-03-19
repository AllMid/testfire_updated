from .Pages.LoginPage import Login_page

#the test goes to the site, enters a username in the username field, enters an xss injection in the password field,
#clicks the Login button and checks if there is an alert or not
def test_xss_injections_passwd(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON, browser)
    auth_page.go_to_site(Login_page.base_url)
    auth_page.enter_username("admin")
    auth_page.enter_password("<script>alert(123)</script>")
    auth_page.click_on_the_login_button()
    assert auth_page.find_element_alert() is False


#the test goes to the site, enters an xss injection in the username field, enters a password in the password field,
#clicks the Login button and checks if there is an alert or not
def test_xss_injections_uid(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON, browser)
    auth_page.go_to_site(Login_page.base_url)
    auth_page.enter_username("<script>alert(123)</script>")
    auth_page.enter_password("passwd")
    auth_page.click_on_the_login_button()
    assert auth_page.find_element_alert() is False


#the test goes to the site, enters an xss injection in the search bar, 
#clicks on the Go button and checks if there is an alert or not
def test_xss_injections_search(browser):
    auth_page = Login_page('login_page', Login_page.LOCATOR_LOGIN_BUTTON, browser)
    auth_page.go_to_site(Login_page.base_url)
    auth_page.enter_search("<script>alert(123)</script>")
    auth_page.click_on_the_search_button()
    assert auth_page.find_element_alert() is False
