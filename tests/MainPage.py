from ..framework.BasePage import BasePage
from selenium.webdriver.common.by import By

class Google_main_page(BasePage): 
    #localization of the search bar by id in the code of a web resource
    LOCATOR_GOOGLE_TEXT_CONGRATULATIONS = (By.XPATH, "//*[@id='_ctl0__ctl0_Content_Main_promo']/table/tbody/tr[1]/td/h2")