
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_ActionBar(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.menuActionBarTabs = (By.XPATH,"//android.widget.TextView[@text='Action Bar Tabs']")