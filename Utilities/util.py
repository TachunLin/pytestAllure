
import time
import traceback
import random, string
import Utilities.custom_logger as cl
import logging
from traceback import print_stack
import datetime
import os

import pytest
import allure
from allure.constants import AttachmentType
from helpers import ensure_dir
# from Utilities.custom_logger import customLogger
# import Utilities.custom_logger as cl

# log = cl.customLogger(logging.INFO)

class Util(object):

    logging.getLogger().setLevel(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            logging.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        logging.info("Actual Text From Application Web UI --> :: " + actualText)
        logging.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            logging.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            logging.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        logging.info("Actual Text From Application Web UI --> :: " + actualText)
        logging.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            logging.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            logging.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True


    def verifyCheckPoint(self, driver, actual, expectation, request, log):


        if (actual == expectation):
            with pytest.allure.step('Pass~ Actual result: {0} match expectation: {1}'.format(actual, expectation)):
                # cl.customLogger(logging.INFO).info('Pass~ Actual result: {0} match expectation: {1}'.format(actual, expectation))
                log.info('Pass~ Actual result: {0} match expectation: {1}'.format(actual, expectation))
                # logging.info('Pass~ Actual result: {0} match expectation: {1}'.format(actual, expectation))

        else:
            with pytest.allure.step('Mismatched!! Actual result: {0} <-> expectation: {1}'.format(actual, expectation)):
                allure.attach('Assertion error screenshot', open(Util.saveAssertScreenShot(Util(), driver, request.node.name), 'rb').read(), type=AttachmentType.PNG)
                # cl.customLogger(logging.INFO).error('Mismatched!! Actual result: {0} <-> expectation: {1}'.format(actual, expectation))
                log.error('Mismatched!! Actual result: {0} <-> expectation: {1}'.format(actual, expectation))
                assert 0, 'Mismatched!! Actual result: {0} <-> expectation: {1}'.format(actual, expectation)


    def saveExeScreenShot(self, driver, testcaseName):

        current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%S"))
        ensure_dir("Screenshot")
        result_dir = ensure_dir(os.path.join("Screenshot", current_day))
        # result_dir = os.path.join(os.path.dirname(__file__), "Screenshot", current_day)

        # print(result_dir)

        # ensure_dir(result_dir)
        result_dir_test_run = result_dir

        Execution_screen_shot_dir = os.path.join(result_dir_test_run, "Execution")
        ensure_dir(Execution_screen_shot_dir)
        # print(Execution_screen_shot_dir)

        ExeImagePath = os.path.join(Execution_screen_shot_dir, current_day + '_' + testcaseName + ".png")
        driver.save_screenshot(ExeImagePath)

        # print(ExeImagePath)

        return ExeImagePath


    def saveAssertScreenShot(self, driver, testcaseName):

        current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%S"))
        ensure_dir("Screenshot")
        result_dir = ensure_dir(os.path.join("Screenshot", current_day))
        # result_dir = os.path.join(os.path.dirname(__file__), "Screenshot", current_day)

        # print(result_dir)

        # ensure_dir(result_dir)
        result_dir_test_run = result_dir

        Execution_screen_shot_dir = os.path.join(result_dir_test_run, "Assertion")
        ensure_dir(Execution_screen_shot_dir)
        # print(Execution_screen_shot_dir)

        ExeImagePath = os.path.join(Execution_screen_shot_dir, current_day + '_' + testcaseName + ".png")
        driver.save_screenshot(ExeImagePath)

        # print(ExeImagePath)

        return ExeImagePath