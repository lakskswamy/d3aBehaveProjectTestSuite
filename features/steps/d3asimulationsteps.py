from behave import *
from selenium import webdriver
#from d3aBehaveProjectTestSuite.venv.commons import loginpage
from common import *
import time

@given('the user creates a project')
def create_project_call(context):
    create_project(context, "simproject", "simdescription")

@given('the user selects on the project')
def select_project_call(context):
    select_project(context)

@when('the user clicks on new simulation button')
def click_new_simulation_call(context):
    click_new_simulation(context)

@when('the user enters simulation name "{sname}" and description "{sdescription}"')
def enter_simulation_details_call(context, sname, sdescription):
    enter_simulation_details(context, sname, sdescription)

@when('the user clicks on Next button')
def click_next_button_call(context):
    click_next_button(context)

@then('a new simulation is created')
def new_simulation_validation(context):
    modelling = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/h1').text
    assert modelling == "Modelling"
    print("***New simulation has been created - Landed on modelling page***")

@then('is visible on projects page under the project')
def new_simulation_visible_validation(context):
    time.sleep(2)
    load_project_page_url(context)
    select_project(context)
    newsimulation = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p').text
    assert newsimulation == "sampleSimulationName"
    print(newsimulation + "***New simulation has been created - Visible on projects page***")
    time.sleep(1)
    delete_project(context)
    context.driver.close()

@given('the user selects an existing project')
def select_project_call(context):
    load_project_page_url(context)
    select_project(context)

@then('is visible on projects page under the existing project')
def new_simulation_visible_validation(context):
    time.sleep(2)
    load_project_page_url(context)
    select_project(context)
    newsimulation = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p').text
    assert newsimulation == "sampleSimulationName"
    print(newsimulation + "***New simulation has been created - Visible on projects page***")
    time.sleep(1)
    delete_simulation(context)
    context.driver.close()