from selenium import webdriver
import time

emailElt = "email"
passwordElt = "password"
loginButton = '//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button'
loginErrorMessage = '//*[@id="root"]/main/div[2]/div/div/div/form/span'
chrome = 'C:\Program Files\ChromeDriver\chromedriver'
link = "https://www.d3a.io/login"

def login_page_attributes(context):
    context.emailElt = context.driver.find_element_by_id(emailElt)
    context.passwordElt = context.driver.find_element_by_id(passwordElt)
    context.loginButton = context.driver.find_element_by_xpath(loginButton)

def open_browser(context):
    context.driver = webdriver.Chrome(chrome)
    context.driver.maximize_window()

def open_login_page(context):
    context.driver.get(link)
    time.sleep(1)

def enter_credentials(context, email, password):
    login_page_attributes(context)
    context.emailElt.send_keys(email)
    context.passwordElt.send_keys(password)

def click_login_button(context):
    login_page_attributes(context)
    context.loginButton.click()
    time.sleep(1)

def login_error_message(context):
    return context.driver.find_element_by_xpath(loginErrorMessage).text

def login_steps(context, email, password):
    open_browser(context)
    open_login_page(context)
    login_page_attributes(context)
    enter_credentials(context, email, password)
    click_login_button(context)
