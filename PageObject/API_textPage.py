
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_Texts(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.textView = (By.XPATH,"//android.widget.TextView[@text='TextView']")