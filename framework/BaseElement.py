from framework.Browser import Browser


class BaseElement(object):

    def elem_click(browser, locator):
        Browser.find_element(browser, locator).click()

 
class Elem_button(BaseElement): 
    pass


class Elem_label(BaseElement):
    def elem_send_word(browser, locator, word):
        Browser.find_element(browser, locator).send_keys(word)

    def elem_clean(browser, locator):
        Browser.find_element(browser, locator).clear()    

    