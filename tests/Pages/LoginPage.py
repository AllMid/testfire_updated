from framework.BasePage import BasePage
from framework.BaseElement import Elem_button, Elem_label

from selenium.webdriver.common.by import By
import logging

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
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '/html/body/table/tbody/tr/td/div/form/table/tbody/tr/td/input[@type="submit"]')

    LOCATOR_FAIL_TEXT = (By.XPATH, '/html/body/table/tbody/tr/td/div/p/span/text()')

    def get_pagename():
        return Login_page.pagename

    #entering in the "username" field
    def enter_username(word, browser):
        Elem_label.elem_click(browser, Login_page.LOCATOR_USERNAME_FIELD)
        Elem_label.elem_send_word(browser, Login_page.LOCATOR_USERNAME_FIELD, word)
        logging.info(f'entering a word{word} in the login field')
        
    #entering in the "password" field
    def enter_password(word, browser):
        Elem_label.elem_click(browser, Login_page.LOCATOR_PASSWORD_FIELD)
        Elem_label.elem_send_word(browser, Login_page.LOCATOR_PASSWORD_FIELD, word)
        logging.info(f'entering a word {word} in the password field')
   
    
    #entering in the "search" field
    def enter_search(word, browser):
        Elem_label.elem_click(browser, Login_page.LOCATOR_SEARCH_FIELD)
        Elem_label.elem_send_word(browser, Login_page.LOCATOR_SEARCH_FIELD, word)
        logging.info(f'entering a word {word} in the search field')


    #clicks on the "Login" button
    def click_on_the_login_button(browser, locator):
        Elem_button.elem_click(browser, locator)
        logging.info('click on the login button')

    #clicks on the "Go" button
    def click_on_the_search_button(browser):
        Elem_button.elem_click(browser, Login_page.LOCATOR_SEARCH_BUTTON)
        logging.info('click on the search button "Go"')

