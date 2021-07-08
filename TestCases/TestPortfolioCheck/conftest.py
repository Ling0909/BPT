import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_PortfolioCheck import PagePortfolioCheck

driver = None
@pytest.fixture(scope='class')
def for_portfolioCheck_class():
    global driver
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl = PageLogin(driver)
    pl.login_success(cd.login_username, cd.login_password)
    pp=PagePortfolioCheck(driver)
    yield(pp)
    driver.quit()





