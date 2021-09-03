from behave import *
from selenium import webdriver
import time


@given('the user launches Chrome Browser')
def open_browser(context):
    context.driver=webdriver.Chrome("C:\Program Files\ChromeDriver\chromedriver")

@when('the user opens D3a login page')
def open_login_page(context):
    context.driver.get("https://www.d3a.io/login")
    time.sleep(1)

@when('the user enters username "{email}" and password "{password}"')
def enter_credentials(context, email, password):
    context.driver.find_element_by_id("email").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(password)

@when('the user clicks the Login Button')
def click_login_button(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(1)

@then('the home page opens')
def assert_login_successful(context):
    text = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]//header/h1').text
    assert text == "Home"
    print("***Login Successful - Home page is open***")

    context.driver.close()

def login_steps(context, email, password):
    open_browser(context)
    open_login_page(context)
    enter_credentials(context, email, password)
    click_login_button(context)