
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_App(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.menuActionBar = (By.XPATH,"//android.widget.TextView[@text='Action Bar']")