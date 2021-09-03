from behave import *
from selenium import webdriver
#from d3aBehaveProjectTestSuite.venv.commons import loginpage

import time

@given('the user creates a project')
def create_project(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('// *[ @ id = "root"] / div / div[2] / header / div[3] / button[2]').click()
    time.sleep(2)
    context.driver.find_element_by_id("input-field-name").send_keys("smapleProjectName")
    context.driver.find_element_by_id("textarea-field-nameTextArea").send_keys("sampleProjectDescription")
    time.sleep(2)
    context.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button').click()
    time.sleep(2)

@when('the user selects on the project')
def select_project(context):
    context.driver.get("https://www.d3a.io/projects")
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]/span/span').click()
    time.sleep(2)

@when('the user clicks on new simulation button')
def click_new_simulation(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button').click()
    time.sleep(2)

@when('the user enters simulation name "{sname}" and description "{sdescription}"')
def enter_simulation_details(context, sname, sdescription):
    context.driver.find_element_by_id("input-field-name").clear()
    context.driver.find_element_by_id("input-field-name").send_keys(sname)
    context.driver.find_element_by_id("textarea-field-description").send_keys(sdescription)
    #time.sleep(1)

@when('the user clicks on Next button')
def click_next_button(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button').click()
    time.sleep(2)

@then('a new simulation is created')
def new_simulation_validation(context):
    modelling = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/h1').text
    assert modelling == "Modelling"
    print("***New simulation has been created - Landed on modelling page***")

@then('is visible on projects page under the project')
def new_simulation_visible_validation(context):
    time.sleep(2)
    select_project(context)
    newsimulation = context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p').text
    assert newsimulation == "sampleSimulationName"
    print(newsimulation + "***New simulation has been created - Visible on projects page***")

    # Remove created project
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[2]/div/button').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[3]/button[2]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/button[2]').click()
    time.sleep(1)
    print("sampleProjectName Project is Deleted")