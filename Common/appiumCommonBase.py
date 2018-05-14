from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import requests
import logging
import Utilities.custom_logger as cl
from Utilities.util import Util
from allure.constants import AttachmentType
import allure
import pytest
import traceback
from traceback import print_stack
from selenium.common.exceptions import NoSuchElementException
import inspect
import os

class AppiumCommon(object):

    logging.getLogger().setLevel(logging.INFO)

    def __init__(self):
        #self.driver = driver
        self.driver.implicitly_wait(15)


    def send_key_with_Element(self,loc,value):
        self.locateElement(loc).click()
        self.locateElement(loc).clear()
        self.locateElement(loc).send_keys(value)

    def locateElement(self,loc, driver, request):
        try:
            # print(loc)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            # logging.info("Find {0} element".format(loc))
            return element
        except:
            # print("cannot find {0} element".format(loc))
            logging.error("Cannot find {0} element".format(loc))
            allure.attach("Cannot find {0} element".format(loc), open(Util.saveExeScreenShot(Util(), driver, request.node.name), 'rb').read(),type=AttachmentType.PNG)

            assert 0, "Cannot find {0} element".format(loc)
        return None


    def locateElementByName(self,loc, name):
        try:
            print(loc)
            logging.info(loc)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return element
        except:
            print("cannot find {0} element".format(loc))
            logging.error("cannot find {0} element".format(loc))
        return None


    def locateMutipleElements(self,loc, driver, request):
        # with pytest.raises(NoSuchElementException):
        try:
            # print(loc)
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(loc))
            # logging.info("Find elements of {0}".format(loc))
            return elements
        except Exception as e:
            errList = traceback.format_exception(None, e, e.__traceback__)

            logging.error("Cannot find {0} element".format(loc))
            allure.attach("Cannot find {0} element".format(loc),
                          open(Util.saveExeScreenShot(Util(), driver, request.node.name), 'rb').read(),
                          type=AttachmentType.PNG)
            assert 0, "Cannot find {0} element".format(loc)


    def locateangularElement(self,loc, driver, request):
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, loc)))
            return element
        except:
            print ("cannot find {0} element".format(loc))
            logging.error("cannot find {0} element".format(loc))
            allure.attach("cannot find {0} element".format(loc), open(Util.saveExeScreenShot(Util(), driver, request.node.name), 'rb').read(),
                          type=AttachmentType.PNG)
        return None

    def swipebetweenElements(self, driver, request, start_loc, end_loc, duration=500):

        startElement = self.locateElement(start_loc, driver, request)
        endElement = self.locateElement(end_loc, driver, request)

        start_elementX = startElement.location.get('x')
        start_elementY = startElement.location.get('y')

        end_elementX = endElement.location.get('x')
        end_elementY = endElement.location.get('y')

        self.driver.swipe(start_elementX, start_elementY, end_elementX, end_elementY, duration)



    def waitForElementInvisible(self,loc):
        #load-spinner
        try:
            element = WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loc))
            return True
        except:
            print ("cannot invisibility_of_element {0} element".format(loc))
        return False

    def waitForElementVisible(self,loc):
        #load-spinner
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of(loc))
            return True
        except:
            print ("cannot visibility_of_element {0} element".format(loc))
        return False

    def waitForElement(self,loc, timeout=10, pollingfreq=1):

        with pytest.allure.step('Waiting element in {0} seconds for every {1} second'.format(timeout, pollingfreq)):
            pass

        try:
            WebDriverWait(self.driver, timeout, pollingfreq).until(EC.element_to_be_clickable(loc))
            return True
        except:
            with pytest.allure.step('Waiting element in {0} seconds for every {1} second'.format(timeout, pollingfreq)):
                print ("cannot find element {0} to be clickable".format(loc))
        return False

    def isElementPresent(self, element):

        with pytest.allure.step('Checking whether element is present or not'):
            pass

        if element is not None:
            return True

        else:
            with pytest.allure.step('Cannot find such an element'):
                return False

    def click_with_Element(self, loc):
        self.locateElement(loc).click()

    def clickElementsBySendKey(self, loc, value):
        self.locateElement(loc).send_keys(value)

    def checkSourceHaveErrorOrNot(self):
        request = requests.get(self.currentUrl())
        return request.status_code == 404 or request.status_code == 500

    def selectElementByVisibleText(self, loc, value):
        selectElement = Select(self.locateElement(loc))
        selectElement.select_by_visible_text(value)

    def selectElementByValue(self, loc, value):
        selectElement = Select(self.locateElement(loc))
        selectElement.select_by_value(value)

    def moveToElement(self, element):
        hoverElement = ActionChains(self.driver).move_to_element(element)
        print("move")
        hoverElement.perform()

    def closeWindowAndSwitchBack(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def saveScreenShot(self, fileName):
        self.driver.save_screenshot(fileName)

    def backPage(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()

