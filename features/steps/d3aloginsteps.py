from behave import *
from selenium import webdriver
import time
from common import *

#from venv.common import *

@given('the user launches Chrome Browser')
def open_browser_call(context):
    open_browser(context)

@when('the user opens D3a login page')
def open_login_page_call(context):
    open_login_page(context)

@when('the user enters username "{email}" and password "{password}"')
def enter_credentials_call(context, email, password):
    enter_credentials(context, email, password)

@when('the user clicks the Login Button')
def click_login_button_call(context):
    click_login_button(context)
    time.sleep(3)

@then('the home page opens')
def assert_login_successful(context):
    HomeIcon = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]//header/h1').text
    assert HomeIcon == "Home"
    print("***Login Successful - Home page is open***")
    context.driver.close()

@then('the home page does not open')
def assert_login_unsuccessful(context):
    login_errorMessage = context.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/span').text
    assert login_errorMessage == "Please, enter valid credentials"
    print("***Login Not Successful - Home page is does not open***")
    context.driver.close()