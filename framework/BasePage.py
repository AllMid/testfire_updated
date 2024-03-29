import abc


#creating a base class in base page
class BasePage(abc.ABC):                     

    #initialization of the web driver and the URL of the web resource
    def __init__(self, pagename, uniq_elem_locator):
        self.pagename = pagename
        self.uniq_elem_loc = uniq_elem_locator        

    @abc.abstractmethod             
    def get_pagename():
         pass

   