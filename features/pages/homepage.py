import time

homeIcon = '//*[@id="root"]/div/div[2]//header/h1'
projectButton = '//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div[2]/div/div/button'

def home_page_attributes(context):
    context.projectButton = context.driver.find_element_by_xpath(projectButton)

def home_icon_validation(context):
    return context.driver.find_element_by_xpath(homeIcon).text

def load_project_page_button(context):
    home_page_attributes(context)
    context.projectButton.click()
    time.sleep(2)