import pytest

from framework.Browser import Browser

#creating a fixture to use in different files
@pytest.fixture(scope="function")
#using chrome as a web driver, setting up to ignore certificate errors and closing the driver after it stops working
def browser1():
    base_url = 'https://testfire.net/login.jsp'
    options = 'Chrome'
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    driver = Browser(options)
    yield driver
    driver.quit()