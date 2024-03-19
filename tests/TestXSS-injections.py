from tests.LoginPages import Google_login_page

#the test goes to the site, enters a username in the username field, enters an xss injection in the password field,
#clicks the Login button and checks if there is an alert or not
def test_google_xss_injections_passwd(browser):
    google_auth_page = Google_login_page(browser)
    google_auth_page.go_to_site(Google_login_page.base_url)
    google_auth_page.enter_username("admin")
    google_auth_page.enter_password("<script>alert(123)</script>")
    google_auth_page.click_on_the_login_button()
    assert google_auth_page.find_element_alert() is False


#the test goes to the site, enters an xss injection in the username field, enters a password in the password field,
#clicks the Login button and checks if there is an alert or not
def test_google_xss_injections_uid(browser):
    google_auth_page = Google_login_page(browser)
    google_auth_page.go_to_site(Google_login_page.base_url)
    google_auth_page.enter_username("<script>alert(123)</script>")
    google_auth_page.enter_password("passwd")
    google_auth_page.click_on_the_login_button()
    assert google_auth_page.find_element_alert() is False


#the test goes to the site, enters an xss injection in the search bar, 
#clicks on the Go button and checks if there is an alert or not
def test_google_xss_injections_search(browser):
    google_auth_page = Google_login_page(browser)
    google_auth_page.go_to_site(Google_login_page.base_url)
    google_auth_page.enter_search("<script>alert(123)</script>")
    google_auth_page.click_on_the_search_button()
    assert google_auth_page.find_element_alert() is False
