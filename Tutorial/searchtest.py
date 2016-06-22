# vim:fileencoding=utf-8

import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from glsdp import GLBaseTestCase
from glsdp import GLSupportUI
from glsdp import GLWait
from glsdp import GLHelper

class SearchOption(GLBaseTestCase,GLSupportUI,GLWait):
    baseUrl = "http://www.rec-global.com/search?searchword=&searchphrase=all"
    def glAfterSetUp(self):
        GLWait.whilePageLoaderIsVisible(self.driver)


    def testSearchOption(self):
        self.findElementAndPutText(self.driver,By.XPATH,".// *[ @ id = 'search-searchword']","QA engineer")
        self.clickOnInputTypeButtonWithText(self.driver,"Search")
"""
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ".//*[@id='blog-post-wrapper']/div[2]/div/div/div/dl/dt[1]/a")
            )
        )"""
if __name__ == "__main__":
                unittest.main()