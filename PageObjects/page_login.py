from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.locators_loginPage import LocatorsLoginPage as llp

class PageLogin:
    def __init__(self,driver):
        self.driver=driver
    def login_success(self,username,password):#登录功能
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(llp.input_username))
        self.driver.find_element(*llp.input_username).send_keys(username)
        self.driver.find_element(*llp.input_password).send_keys(password)
        self.driver.find_element(*llp.button_login).click()
