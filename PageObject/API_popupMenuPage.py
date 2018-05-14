
from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_PopupMenus(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.widgetButtons = (By.CLASS_NAME,"android.widget.Button")
        self.popupMenuItems = (By.ID,"android:id/title")
