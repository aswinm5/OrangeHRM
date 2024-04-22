from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    TXT_Dashboard = (By.XPATH, "//aside[@class='oxd-sidepanel']//li[8]/a/span")

    # to access the instance of parent class constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Validate Dashboard
    def validate_dashboard(self):
        self.verify_element_displayed(self.TXT_Dashboard)
        assert self.get_element_text(self.TXT_Dashboard) == "Dashboard"
