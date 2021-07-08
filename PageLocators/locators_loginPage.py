from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    input_username=(By.XPATH,'//input[@id="ctl06_txtLogonID"]')
    input_password=(By.XPATH,'//input[@id="ctl06_txtPassword"]')
    button_login=(By.XPATH,'//a[text()="Login"]')
