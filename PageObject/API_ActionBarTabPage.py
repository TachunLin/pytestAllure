

from selenium.webdriver.common.by import By
from Common.appiumCommonBase import AppiumCommon


class API_ActionBarTab(AppiumCommon):

    def __init__(self,driver):

        self.driver = driver
        self.AddNewTab = (By.ID,'com.example.android.apis:id/btn_add_tab')
        self.ResolveLastTab = (By.ID, 'com.example.android.apis:id/btn_remove_tab')
        self.ToggleTabMode = (By.ID, 'com.example.android.apis:id/btn_toggle_tabs')
        self.RemoveAllTabs = (By.ID, 'com.example.android.apis:id/btn_remove_all_tabs')
        self.TabViews = (By.CLASS_NAME, 'android.app.ActionBar$Tab')