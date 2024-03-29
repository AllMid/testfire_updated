import pytest

from framework.Browser import Browser
from tests.variables import browser_type

#creating a fixture to use in different files
@pytest.fixture(scope="function")
#using chrome as a web driver, setting up to ignore certificate errors and closing the driver after it stops working
def browser():
    driver = Browser()
    driver = driver.browserpage(browser_type, Browser.driver_variable)
    yield driver
    driver.quit()

