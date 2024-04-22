from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Username_disp = (By.XPATH,"//label[normalize-space()='Username']")
    # pwd_disp = (By.XPATH, "//label[normalize-space()='Password']")
    TXT_Username = (By.XPATH, "//input[@placeholder='Username']")
    TXT_Password = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
    INVALID_CRED_MSG = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    OrangeHRM_logo = (By.XPATH, "//div[@class='orangehrm-login-branding']")
    Adm_username = (By.XPATH, "//p[normalize-space()='Username : Admin']")
    Adm_password = (By.XPATH, "//p[normalize-space()='Password : admin123']")
    Forget_password = (By.XPATH, "//div[@class='orangehrm-login-forgot']")
    Loginpage = (By.XPATH, "//h5[normalize-space()='Login']")

    # to access the instance of parent class constructor
    def __init__(self, driver):
        super().__init__(driver)

    # login visibility
    # def validate_username_displayed(self):
    # assert self.get_element_text(self.Username_disp) == "Username"
    # assert self.get_element_text(self.TXT_Password) == "Password"

    # login button visiblility
    def validate_loginbtn(self):
        self.verify_element_displayed(self.LOGIN_BTN)

    # enter both username and password
    def enter_login_credential(self, user, pwd):
        self.input_element(self.TXT_Username, user)
        self.input_element(self.TXT_Password, pwd)

    # entering only username
    def enter_username(self, user):
        self.input_element(self.TXT_Username, user)

    # entering only password
    def enter_password(self, pwd):
        self.input_element(self.TXT_Password, pwd)

    # clicking login button
    def enter_login(self):
        self.click_element(self.LOGIN_BTN)

    # validate title of page
    def validate_title(self):
        assert self.get_title() == "QubexEdu"

    # validate invalid credential
    def validate_invalid_cred(self):
        assert self.get_element_text(self.INVALID_CRED_MSG) == "Invalid credentials"

    # Validate Logo displayed
    def validate_logo(self):
        self.verify_element_displayed(self.OrangeHRM_logo)

    # validate default username and password displayed
    def validate_admin_cred(self):
        self.verify_element_displayed(self.Adm_username)
        assert self.get_element_text(self.Adm_username) == "Username : Admin"
        self.verify_element_displayed(self.Adm_password)
        assert self.get_element_text(self.Adm_password) == "Password : admin123"

    # validate forget password is present
    def validte_forget_password(self):
        self.verify_element_displayed(self.Forget_password)

    # validate login page is displayed
    def validate_login_page(self):
        self.verify_element_displayed(self.Loginpage)
