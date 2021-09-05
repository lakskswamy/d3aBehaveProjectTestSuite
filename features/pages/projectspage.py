from features.pages.homepage import *

newProjectIcon = '// *[ @ id = "root"] / div / div[2] / header / div[3] / button[2]'
projectName = "input-field-name"
projectDescription = "textarea-field-nameTextArea"
addProject = '/html/body/div[5]/div/div/div[2]/button'
settingsButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[2]/div/button'
deleteButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[3]/button[2]/p'
imSureButton = '/html/body/div[7]/div/div/div[2]/div/button[2]'
projectsUrl = "https://www.d3a.io/projects"
existingProject = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]/span/span'
newSimulationButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/button'
sname = "input-field-name"
sdescription = "textarea-field-description"
nextButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/button'
newProjectName = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div/div[1]'
projectPageHeader = '//*[@id="root"]/div/div[2]/header/h1'
addButton = '/html/body/div[5]/div/div/div[2]/button'
newSimulation = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/p'
simSettingButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/button'
simDeleteButton = '//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/button[3]'
simImSureButton = "/html/body/div[11]/div/div/div[2]/div/button[2]"
projectErrorMessage = '/html/body/div[5]/div/div/div[2]/span'

def project_details(context):
    context.projectName = context.driver.find_element_by_id(projectName)
    context.projectDescription = context.driver.find_element_by_id(projectDescription)

def click_new_project_icon(context):
    context.driver.find_element_by_xpath(newProjectIcon).click()
    time.sleep(2)

def enter_project_details(context,name,description):
    project_details(context)
    context.projectName.send_keys(name)
    context.projectDescription.send_keys(description)
    time.sleep(2)

def add_project(context):
    context.driver.find_element_by_xpath(addProject).click()
    time.sleep(2)

def delete_project(context):
    context.driver.find_element_by_xpath(settingsButton).click()
    time.sleep(2)
    context.driver.find_element_by_xpath(deleteButton).click()
    time.sleep(2)
    context.driver.find_element_by_xpath(imSureButton).click()
    time.sleep(2)
    print("Test-Project is Deleted")

def load_project_page_url(context):
    context.driver.get(projectsUrl)
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
    context.driver.find_element_by_xpath(existingProject).click()
    time.sleep(2)

def click_new_simulation(context):
    context.driver.find_element_by_xpath(newSimulationButton).click()
    time.sleep(2)

def enter_simulation_attributes(context):
    context.sname = context.driver.find_element_by_id(sname)
    context.sdescription = context.driver.find_element_by_id(sdescription)

def enter_simulation_details(context, sname, sdescription):
    enter_simulation_attributes(context)
    context.sname.clear()
    context.sname.send_keys(sname)
    context.sdescription.send_keys(sdescription)

def click_next_button(context):
    context.driver.find_element_by_xpath(nextButton).click()
    time.sleep(2)

def delete_simulation(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(simSettingButton).click()
    time.sleep(1)
    context.driver.find_element_by_xpath(simDeleteButton).click()
    time.sleep(1)
    context.driver.find_element_by_xpath(simImSureButton).click()
    time.sleep(1)
    print("Test-Simulation is Deleted")

def new_project_name(context):
    return context.driver.find_element_by_xpath(newProjectName).text

def projects_page_headline(context):
    return context.driver.find_element_by_xpath(projectPageHeader).text

def return_add_button(context):
    return context.driver.find_element_by_xpath(addButton)

def project_error_message(context):
    return context.driver.find_element_by_xpath(projectErrorMessage).text

def new_simulation_validation(context):
    return context.driver.find_element_by_xpath(newSimulation).text