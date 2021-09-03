from behave import *
from selenium import webdriver
from common import *
#from selenium.webdriver.common.by import By

import time

@given('the user logs in')
def successful_login(context):
   login_steps(context, "laks.kswamy@gmail.com", "11-Feb-1995")

@when('the user clicks on second icon from top on the left hand side')
def load_project_page_button_call(context):
    load_project_page_button(context)

@when('the user clicks on new project icon')
def click_new_project_icon_call(context):
    click_new_project_icon(context)

@when('the user enters name "{name}" and description "{description}"')
def enter_project_details_call(context,name,description):
    enter_project_details(context, name, description)

@when('the user clicks on Add button')
def add_project_call(context):
    add_project(context)

@when('the user navigates to https://www.d3a.io/projects')
def load_project_page_url_call(context):
    load_project_page_url(context)

@then('a new project is created')
def project_creation_validation(context):
    load_project_page_url(context)
    projectName = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]').text
    print(projectName + " project is found")
    assert projectName == "sampleName"
    time.sleep(1)

@then('is visible on projects page')
def project_visible_validation(context):
    projectButton = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/h1').text
    projectName = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]').text
    print(projectButton + " page contains " + projectName)
    assert projectButton == "Projects"
    time.sleep(1)
    delete_project(context)
    context.driver.close()

@then('Add button for creation of project is not clickable')
def add_button_not_clickable(context):
    addbutton = context.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button')
    href_data = addbutton.get_attribute('href')
    if href_data is None:
        is_clickable = False
        print("***Please enter name for the project***")
        context.driver.close()

@then('a new project is not created')
def project_not_created(context):
    project_errorMessage = context.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/span').text
    assert project_errorMessage == "Project name already exists."
    print("***Project Creation Not Successful***")
    context.driver.close()

