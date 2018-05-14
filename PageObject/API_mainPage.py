
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_Main(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.menuApp = (By.XPATH,"//android.widget.TextView[@text='App']")
        self.menuViews = (By.XPATH,"//android.widget.TextView[@text='Views']")
