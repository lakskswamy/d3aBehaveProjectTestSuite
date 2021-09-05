from behave import *
from selenium import webdriver
import time

def open_browser(context):
    context.driver=webdriver.Chrome("C:\Program Files\ChromeDriver\chromedriver")

def open_login_page(context):
    context.driver.get("https://www.d3a.io/login")
    time.sleep(1)

def enter_credentials(context, email, password):
    context.driver.find_element_by_id("email").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(password)

def click_login_button(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(1)

#def attributes(context):

 #   HomeIcon = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]//header/h1').text
  #  errorMessage = context.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/span').text

def login_steps(context, email, password):
    open_browser(context)
    open_login_page(context)
    enter_credentials(context, email, password)
    click_login_button(context)

def load_project_page_button(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button').click()
    time.sleep(2)

def click_new_project_icon(context):
    context.driver.find_element_by_xpath('// *[ @ id = "root"] / div / div[2] / header / div[3] / button[2]').click()
    time.sleep(2)

def enter_project_details(context,name,description):
    context.driver.find_element_by_id("input-field-name").send_keys(name)
    context.driver.find_element_by_id("textarea-field-nameTextArea").send_keys(description)
    time.sleep(2)

def add_project(context):
    context.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button').click()
    time.sleep(2)

def delete_project(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[2]/div/button').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[3]/button[2]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/button[2]').click()
    time.sleep(1)
    print("Test-Project is Deleted")

def load_project_page_url(context):
    context.driver.get("https://www.d3a.io/projects")
    time.sleep(1)

def create_project(context, name, description):
    load_project_page_button(context)
    time.sleep(1)
    click_new_project_icon(context)
    time.sleep(1)
    enter_project_details(context, name, description)
    time.sleep(1)
    add_project(context)
    time.sleep(1)

def select_project(context):
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]/span/span').click()
    time.sleep(2)

def click_new_simulation(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button').click()
    time.sleep(2)

def enter_simulation_details(context, sname, sdescription):
    context.driver.find_element_by_id("input-field-name").clear()
    context.driver.find_element_by_id("input-field-name").send_keys(sname)
    context.driver.find_element_by_id("textarea-field-description").send_keys(sdescription)

def click_next_button(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button').click()
    time.sleep(2)

def delete_simulation(context):
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/button').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/button[3]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/div/button[2]").click()
    time.sleep(1)
    print("Test-Simulation is Deleted")

