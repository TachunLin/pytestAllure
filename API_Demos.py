# -*- coding: utf-8 -*-
import os
import pytest

from appium import webdriver

from time import sleep
import subprocess
from subprocess import Popen
import allure
import logging
import Utilities.custom_logger as cl
from allure.constants import AttachmentType
from Utilities.util import Util
from Utilities.dataReader import reader
import traceback
from traceback import print_stack
import yaml

from PageObject.API_mainPage import API_Main
from PageObject.API_appPage import API_App
from PageObject.API_ActionBarPage import API_ActionBar
from PageObject.API_ActionBarTabPage import API_ActionBarTab
from PageObject.API_viewsPage import API_Views
from PageObject.API_textPage import API_Texts
from PageObject.API_textViewPage import API_TextView
from PageObject.API_popupMenuPage import API_PopupMenus

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'

# Set global log for all test suite
log = cl.customLogger(logging.INFO)


@allure.feature('API Demo Test')
class TestSimpleAndroid():
    # log = logging.getLogger().setLevel(logging.INFO)

    @pytest.fixture(scope="module")
    def driver(self, request, device_logger, device):
        p = subprocess.Popen('ttab -w "/usr/local/bin/appium '
                             '--address 127.0.0.1 --chromedriver-port 9516 --bootstrap-port 4725 --no-reset '
                             '--local-timezone"', shell=True, stdin=subprocess.PIPE)

        sleep(10)

        allure.environment(Device='Android emulator', Version='Android 6.0', Type='Demo')

        # calling_request = request._pyfuncitem.name

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, reader.cap_reader(reader(), device))

        driver.implicitly_wait(10)

        driver.close_app()

        def fin():
            # take_screenhot_and_logcat(driver, device_logger, calling_request)
            driver.remove_app('com.example.android.apis')
            driver.quit()
            os.system('./script/stopAppium.sh')

        request.addfinalizer(fin)
        return driver

    @pytest.yield_fixture()
    def setUp(self, driver, request):
        driver.launch_app()
        yield

        allure.attach('Test completed screenshot',
                      open(Util.saveExeScreenShot(Util(), driver, request.node.name), 'rb').read(),
                      type=AttachmentType.PNG)

        driver.close_app()

    def logReport(self, message):
        with pytest.allure.step(message):
            log.info(message)

    @allure.story('Add action bar check')
    def test_01ActionBarTab(self, driver, setUp, request):

        mainMenu = API_Main(driver)
        appMenu = API_App(driver)
        actionBarMenu = API_ActionBar(driver)
        actionBarTab = API_ActionBarTab(driver)

        with pytest.allure.step('Click App'):
            self.logReport('Click App')
            menuApp = mainMenu.locateElement(mainMenu.menuApp, driver, request)
            menuApp.click()

        with pytest.allure.step('Click Action'):
            self.logReport('Click Action')
            menuActionBar = appMenu.locateElement(appMenu.menuActionBar, driver, request)
            menuActionBar.click()

        with pytest.allure.step('Click Action Bar Tab'):
            self.logReport('Click Action Bar Tab')
            menuActionBarTab = actionBarMenu.locateElement(actionBarMenu.menuActionBarTabs, driver, request)
            menuActionBarTab.click()

        with pytest.allure.step('Click Add New Tab 3 times'):
            self.logReport('Click Add New Tab 3 times')
            addNewTabButton = actionBarTab.locateElement(actionBarTab.AddNewTab, driver, request)
            for i in range(3):
                sleep(1)
                addNewTabButton.click()

        with pytest.allure.step('Click Toggle Tab Mode'):
            self.logReport('Click Toggle Tab Mode')
            toggleTabMode = actionBarTab.locateElement(actionBarTab.ToggleTabMode, driver, request)
            toggleTabMode.click()

        with pytest.allure.step('Verify 3 tabs toggle'):
            self.logReport('Verify 3 tabs toggle')
            tabViews = actionBarTab.locateMutipleElements(actionBarTab.TabViews, driver, request)
            Util.verifyCheckPoint(Util(), driver, len(tabViews), 3, request, log)

    @allure.story('Text on text view check')
    def test_02TextView(self, driver, setUp, request):

        mainMenu = API_Main(driver)
        viewMenu = API_Views(driver)
        textMenu = API_Texts(driver)
        textViewMenu = API_TextView(driver)

        with pytest.allure.step('Click Views'):

            # Scroll to 'Views' text
            driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Views"))')

            self.logReport('Click Views')
            menuViews = mainMenu.locateElement(mainMenu.menuViews, driver, request)
            menuViews.click()

        with pytest.allure.step('Click Views'):

            # Scroll to 'Text' text
            driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Text"))')

            self.logReport('Click Views')
            menuText = viewMenu.locateElement(viewMenu.menuText, driver, request)
            menuText.click()

        with pytest.allure.step('Click TextView'):
            self.logReport('Click TextView')
            menuTextView = textMenu.locateElement(textMenu.textView, driver, request)
            menuTextView.click()

        with pytest.allure.step('Verify 4 text types exists'):
            self.logReport('Verify small text')
            smallText = textViewMenu.locateElement(textViewMenu.smallText, driver, request)
            Util.verifyCheckPoint(Util(), driver, smallText.text, "Small", request, log)

            self.logReport('Verify medium text')
            mediumText = textViewMenu.locateElement(textViewMenu.mediumText, driver, request)
            Util.verifyCheckPoint(Util(), driver, mediumText.text, "Medium", request, log)

            self.logReport('Verify large text')
            largeText = textViewMenu.locateElement(textViewMenu.largeText, driver, request)
            Util.verifyCheckPoint(Util(), driver, largeText.text, "Large", request, log)

            self.logReport('Verify selectable text')
            selectableText = textViewMenu.locateElement(textViewMenu.selectableText, driver, request)
            Util.verifyCheckPoint(Util(), driver, selectableText.text, "NotSelectable", request, log)


    @allure.story('Popup menu items check')
    def test_03PopupMenu(self, driver, setUp, request):

        mainMenu = API_Main(driver)
        viewMenu = API_Views(driver)
        popupMenu = API_PopupMenus(driver)

        with pytest.allure.step('Click Views'):
            # Scroll to 'Views' text
            driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Views"))')

            self.logReport('Click Views')
            menuViews = mainMenu.locateElement(mainMenu.menuViews, driver, request)
            menuViews.click()

        with pytest.allure.step('Click Popup Menu'):
            # Scroll to 'Views' text
            driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Popup Menu"))')

            self.logReport('Click Popup Menu')
            menuPopup = viewMenu.locateElement(viewMenu.menuPopup, driver, request)
            menuPopup.click()

        with pytest.allure.step('Click Make a popup button'):
            self.logReport('Click Make a popup button')
            widgetButtons = popupMenu.locateMutipleElements(popupMenu.widgetButtons, driver, request)
            makePopup = widgetButtons[0]
            makePopup.click()

        with pytest.allure.step('Click Popup menus exists'):
            self.logReport('Click Popup menus exists')
            popupItems = popupMenu.locateMutipleElements(popupMenu.popupMenuItems, driver, request)

            self.logReport('Verify search text')
            searchPopup = popupItems[0]
            Util.verifyCheckPoint(Util(), driver, searchPopup.text, "Search", request, log)

            self.logReport('Verify Add text')
            addPopup = popupItems[1]
            Util.verifyCheckPoint(Util(), driver, addPopup.text, "Add", request, log)

            self.logReport('Verify Edit text')
            editPopup = popupItems[2]
            Util.verifyCheckPoint(Util(), driver, editPopup.text, "Edit", request, log)









