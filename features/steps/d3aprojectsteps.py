from behave import *
from features.pages.projectspage import *
from features.pages.homepage import *
from features.pages.loginpage import *
import time
import pyautogui
import allure
from allure_commons.types import AttachmentType
from datetime import datetime

@given('the user logs in with username "{email}" and password "{password}"')
def successful_login(context, email, password):
   login_steps(context, email, password)

@when('the user clicks on second icon from top on the left hand side')
def load_project_page_button_call(context):
    load_project_page_button(context)

@when('the user clicks on new project icon')
def click_new_project_icon_call(context):
    click_new_project_icon(context)

@when('the user enters name "{name}" and description "{description}"')
def enter_project_details_call(context, name ,description):
    enter_project_details(context, name, description)

@when('the user clicks on Add button')
def add_project_call(context):
    add_project(context)

@when('the user navigates to https://www.d3a.io/projects')
def load_project_page_url_call(context):
    load_project_page_url(context)

@then('a new project is created')
def project_creation_validation(context):
    try:
        sampleprojectname = new_project_name(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if new_project_name(context) == "sampleName":
        print("Project is created")
        assert True, "Test Passed"
        time.sleep(1)

@then('is visible on projects page')
def project_visible_validation(context):
    try:
        projectPageheadline = projects_page_headline(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if projects_page_headline(context) == "Projects":
        print("Project is found on Projects Page")
        time.sleep(1)
        assert True, "Test Passed"
        myScreenshot = pyautogui.screenshot()
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\project_visible_validation_%s.png' % now)
        allure.attach(context.driver.get_screenshot_as_png(), name='project_visible_validation_%s.png' % now,attachment_type=AttachmentType.PNG)
        delete_project(context)
        context.driver.close()

@then('Add button for creation of project is not clickable')
def add_button_not_clickable(context):
    try:
        href_data = return_add_button(context).get_attribute('href')
    except:
        context.driver.close()
        assert False, "Test Failed"
    if href_data is None:
        is_clickable = False
        print("***Please enter name for the project***")
        assert True, "Test Passed"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\add_button_not_clickable.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="add_button_not_clickable",attachment_type=AttachmentType.PNG)
        context.driver.close()

@then('a new project is not created')
def project_not_created(context):
    try:
        projectpageErrorMessage = project_error_message(context)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if project_error_message(context) == "Project name already exists." :
        print("***Project Creation Not Successful***")
        assert True, "Test Passed"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\lakshmi krishnaswamy\screenshots\project_not_created_errorMessage.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="project_not_created_errorMessage",attachment_type=AttachmentType.PNG)
        context.driver.close()

