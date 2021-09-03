from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage():
    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'password'),
        "login_button": (By.XPATH, '//*[@id="root"]/main/div[2]/div/div/div/form/div[3]/button')
    }

def __init__(self):
    self.driver = webdriver.Chrome("C:\Program Files\ChromeDriver\chromedriver"),

def login_page(self):
    self.base_url = "https://www.d3a.io/login"

def login(self, username="laks.kswamy@gmail.com", password="11-Feb-1995"):
    self.find_element(*self.locator_dictionary['email']).send_keys(username)
    self.find_element(*self.locator_dictionary['password']).send_keys(password)
    self.find_element(*self.locator_dictionary['login_button']).click()
