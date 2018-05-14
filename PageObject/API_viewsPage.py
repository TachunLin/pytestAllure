
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_Views(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.menuText = (By.XPATH,"//android.widget.TextView[@text='Text']")
        self.menuPopup = (By.XPATH,"//android.widget.TextView[@text='Popup Menu']")