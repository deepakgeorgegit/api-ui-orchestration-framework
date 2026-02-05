from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.ID,"dashboard")
    LOGOUT_BUTTON = (By.ID,"logout") 


    def is_loaded(self):
        return self.is_visible(self.DASHBOARD_HEADER) 
 
    def logout(self): 
        self.click(self.LOGOUT_BUTTON)

    def wait_for_item(self, title):
        item_locator = (By.XPATH, f"//div[text()='{title}']")
        self.wait.until(EC.visibility_of_element_located(item_locator))

    def is_item_visible(self, title):
        item_locator = (By.XPATH, f"//div[text()='{title}']")
        return self.is_visible(item_locator)