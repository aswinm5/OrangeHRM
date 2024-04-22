from datetime import datetime

from behave import *
from selenium import webdriver
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage


@given(u'i launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'i open the URL')
def step_impl(context):
    try:
        context.driver.get(TestData.URL)
        context.loginpage = LoginPage(context.driver)
        context.dashboardpage = DashboardPage(context.driver)
    except:
        context.driver.close()
        assert False, "Test Failed! : while opening the url"


@then(u'i should see the Login Page')
def step_impl(context):
    try:
        context.loginpage.validate_login_page()
    except:
        context.driver.close()
        assert False, " Test Failed! : Login page not displayed"


@then(u'i should see the orange HRM Logo displayed')
def step_impl(context):
    try:
        context.loginpage.validate_logo()
    except:
        context.driver.close()
        assert False, " Test Failed! : Logo not displayed"


@then(u'i should see the default Username : Admin and password : admin123 displayed')
def step_impl(context):
    try:
        context.loginpage.validate_admin_cred()
    except:
        context.driver.close()
        assert False, " Test Failed! : Admin credentials not displayed"


@then(u'i should see the Login Button')
def step_impl(context):
    try:
        context.loginpage.validate_loginbtn()
    except:
        context.driver.close()
        assert False, " Test Failed! : login button not displayed"


@then(u'i enter the Username "{user}" and Password "{pwd}"')
def step_impl(context, user, pwd):
    try:
        context.loginpage.enter_username(user)
        context.loginpage.enter_password(pwd)
    except:
        context.driver.close()
        assert False, " Test Failed! : cannot enter on the username or password"


@then(u'i click on login button')
def step_impl(context):
    try:
        context.loginpage.enter_login()
    except:
        context.driver.close()
        assert False, " Test Failed! : Cannot click on login"


@then(u'i should be logged in successfully to the dashboard')
def step_impl(context):
    try:
        context.dashboardpage.validate_dashboard()
    except:
        context.driver.close()
        assert False, " Test Failed! : Dashboard not found"


@then(u'i should see the Invalid Credentials message')
def step_impl(context):
    try:
        context.loginpage.validate_invalid_cred()
    except:
        context.driver.close()
        assert False, " Test Failed! : Dashboard not found"
