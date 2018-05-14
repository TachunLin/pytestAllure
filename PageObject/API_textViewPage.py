
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_TextView(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.smallText = (By.ID,"com.example.android.apis:id/text_small")
        self.mediumText = (By.ID, "com.example.android.apis:id/text_medium")
        self.largeText = (By.ID, "com.example.android.apis:id/text_large")
        self.selectableText = (By.ID, "com.example.android.apis:id/text_selectable")