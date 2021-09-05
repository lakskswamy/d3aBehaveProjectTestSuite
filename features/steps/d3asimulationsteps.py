from behave import *
from features.pages.projectspage import *
import time
import pyautogui
import allure
from allure_commons.types import AttachmentType

@given('the user creates a project with Project Name as "{name}" and description as "{description}"')
def create_project_call(context, name, description):
    create_project(context, name, description)

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
    time.sleep(2)

@then('a new simulation is visible on projects page under the project')
def new_simulation_visible_validation(context):
    load_project_page_url(context)
    select_project(context)
    try:
        newSimulationName = new_simulation_validation(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if new_simulation_validation(context) == "sampleSimulationName":
        print("***New simulation has been created - Visible on projects page***")
        time.sleep(1)
        assert True, "Test Passed"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\new_simulation_visible_validation_new_project.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="new_simulation_visible_validation_new_project",attachment_type=AttachmentType.PNG)
        #delete_project(context)
        context.driver.close()

@given('the user selects an existing project')
def select_project_call(context):
    load_project_page_url(context)
    select_project(context)

@then('a new simulation is visible on projects page under the existing project')
def new_simulation_visible_validation(context):
    load_project_page_url(context)
    select_project(context)
    try:
        newSimulationName = new_simulation_validation(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if new_simulation_validation(context) == "SimulationNameExistingProj":
        print("***New simulation has been created - Visible on projects page***")
        time.sleep(1)
        assert True, "Test Passed"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\new_simulation_visible_validation_existing_project.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="new_simulation_visible_validation_existing_project", attachment_type=AttachmentType.PNG)
        delete_project(context)
        context.driver.close()