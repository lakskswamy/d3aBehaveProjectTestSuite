from behave import *
from selenium import webdriver

from d3aloginsteps import login_steps

import time

@given('the user logs in')
def login_successful(context):
   # context.driver = webdriver.Chrome("C:\Program Files\ChromeDriver\chromedriver")
   # context.driver.get("https://www.d3a.io/login")
   # context.driver.find_element_by_id("email").send_keys("laks.kswamy@gmail.com")
   # context.driver.find_element_by_id("password").send_keys("11-Feb-1995")
   # context.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button').click()
   # time.sleep(2)
   login_steps(context, "laks.kswamy@gmail.com", "11-Feb-1995")

@when('the user clicks on second icon from top on the left hand side')
def project_page(context):
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button').click()
    time.sleep(2)

@when('the user clicks on new project icon')
def click_new_project(context):
    context.driver.find_element_by_xpath('// *[ @ id = "root"] / div / div[2] / header / div[3] / button[2]').click()
    time.sleep(2)

@when('the user enters name "{name}" and description "{description}"')
def enter_project_details(context, name, description):
    context.driver.find_element_by_id("input-field-name").send_keys(name)
    context.driver.find_element_by_id("textarea-field-nameTextArea").send_keys(description)
    time.sleep(2)

@when('the user clicks on Add button')
def add_project(context):
    context.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button').click()
    time.sleep(2)

@then('a project is created')
def project_creation_validation(context):
    context.driver.get("https://www.d3a.io/projects")
    time.sleep(1)
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

    #Remove created project
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[2]/div/button').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[3]/button[2]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/button[2]').click()
    time.sleep(1)
    print("sampleName Project is Deleted")

    context.driver.close()
