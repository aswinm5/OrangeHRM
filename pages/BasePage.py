from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  # Set implicit wait for the entire WebDriver instance

    def click_element(self, by_locator):
        try:
            element = self.driver.find_element(*by_locator)
            element.click()
        except (InvalidSelectorException, TimeoutException) as e:
            print(f"Exception! Can't click on the element: {e}")

    def input_element(self, by_locator, text):
        try:
            element = self.driver.find_element(*by_locator)
            element.send_keys(text)
        except (InvalidSelectorException, TimeoutException) as e:
            print(f"Exception! Can't input text into the element: {e}")

    def get_element_text(self, by_locator):
        try:
            element = self.driver.find_element(*by_locator)
            return element.text
        except (InvalidSelectorException, TimeoutException) as e:
            print(f"Exception! Can't get text from the element: {e}")
            return ""

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        try:
            element = self.driver.find_element(*by_locator)
            return element.get_attribute(attribute_name)
        except (InvalidSelectorException, TimeoutException) as e:
            print(f"Exception! Can't get attribute from the element: {e}")
            return ""

    def verify_element_displayed(self, by_locator):
        try:
            element = self.driver.find_element(*by_locator)
            return element.is_displayed()
        except (InvalidSelectorException, TimeoutException) as e:
            print(f"Exception! Element not displayed: {e}")
            return False

    def select_from_dropdown(self, by_locator, visible_text):
        try:
            element = Select(self.driver.find_element(*by_locator))
            element.select_by_visible_text(visible_text)
            # return True, f"Selected '{visible_text}' from the dropdown successfully"
        except (InvalidSelectorException, TimeoutException, NoSuchElementException) as e:
            print(f"An error occurred while selecting from the dropdown: {e}")

# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_element(self, by_locator):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
#             element.click()
#         except (InvalidSelectorException, TimeoutException) as e:
#             print(f"Exception! Can't click on the element: {e}")
#
#     def input_element(self, by_locator, text):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
#             element.send_keys(text)
#         except (InvalidSelectorException, TimeoutException) as e:
#             print(f"Exception! Can't input text into the element: {e}")
#
#     def get_element_text(self, by_locator):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
#             return element.text
#         except (InvalidSelectorException, TimeoutException) as e:
#             print(f"Exception! Can't get text from the element: {e}")
#             return ""
#
#     def get_title(self):
#         return WebDriverWait(self.driver, 10).until(EC.title_is_present())
#
#     def get_element_attribute(self, by_locator, attribute_name):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
#             return element.get_attribute(attribute_name)
#         except (InvalidSelectorException, TimeoutException) as e:
#             print(f"Exception! Can't get attribute from the element: {e}")
#             return ""
#
#     def verify_element_displayed(self, by_locator):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
#             return element.is_displayed()
#         except (InvalidSelectorException, TimeoutException) as e:
#             print(f"Exception! Element not displayed: {e}")
#             return False
#
#     def select_from_dropdown(self, by_locator, visible_text):
#         try:
#             element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
#             select = Select(element)
#             select.select_by_visible_text(visible_text)
#         except (InvalidSelectorException, TimeoutException, NoSuchElementException) as e:
#             print(f"An error occurred while selecting from the dropdown: {e}")

            # return False, f"Dropdown selection failed for '{visible_text}'"


    # Add other methods as needed
