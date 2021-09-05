from behave import *
from features.pages.loginpage import *
from features.pages.homepage import *
import pyautogui
import allure
from allure_commons.types import AttachmentType

@given('the user launches Chrome Browser')
def open_browser_call(context):
    open_browser(context)

@when('the user opens D3a login page url "https://www.d3a.io/login"')
def open_login_page_call(context):
    open_login_page(context)
    print(link + "  This is the URL")

@when('the user enters username "{email}" and password "{password}"')
def enter_credentials_call(context, email, password):
    enter_credentials(context, email, password)

@when('the user clicks the Login Button')
def click_login_button_call(context):
    click_login_button(context)
    time.sleep(3)

@then('the home page opens')
def assert_login_successful(context):
    try:
        home_icon = home_icon_validation(context)
    except:
        assert False, "Test Failed"
        context.driver.close()
    if home_icon_validation(context) == "Home":
        assert True, "Test Passed"
        print("***Login Successful - Home page is open***")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\assert_login_successful_homePage.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="assert_login_successful_homePage",attachment_type=AttachmentType.PNG)
        context.driver.close()

@then('the home page does not open with invalid username')
def assert_login_unsuccessful(context):
    try:
        error_Message = login_error_message(context)
    except:
        assert False, "Test Failed"
        context.driver.close()
    if login_error_message(context) == "Please, enter valid credentials":
        assert True, "Test Passed"
        print("***Login Not Successful - Home page is not open***")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\assert_login_unsuccessful_error_message_invalid_username.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="assert_login_unsuccessful_error_message_invalid_username",attachment_type=AttachmentType.PNG)
        context.driver.close()

@then('the home page does not open with invalid password')
def assert_login_unsuccessful(context):
    try:
        error_Message = login_error_message(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if login_error_message(context) == "Please, enter valid credentials":
        assert True, "Test Passed"
        print("***Login Not Successful - Home page is not open***")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\assert_login_unsuccessful_error_message_invalid_password.png')
        allure.attach(context.driver.get_screenshot_as_png(),name="assert_login_unsuccessful_error_message_invalid_password",attachment_type=AttachmentType.PNG)
        context.driver.close()