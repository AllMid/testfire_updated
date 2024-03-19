import pytest

from framework.BrowserPage import BrowserPage

#creating a fixture to use in different files
@pytest.fixture(scope="function")
#using chrome as a web driver, setting up to ignore certificate errors and closing the driver after it stops working
def browser():
    options = 'Chrome'
    driver = BrowserPage.browserpage(options)
    yield driver
    driver.quit()

