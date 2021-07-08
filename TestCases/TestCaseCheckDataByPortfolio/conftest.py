import pytest
from selenium import webdriver
from PageObjects.page_checkDataByPortfolio import TestCheckDataByPortfolio
from PageObjects.page_index import PageIndex
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin

driver = None
@pytest.fixture(scope='class')
def for_checkDataByPortfolio_class():
    global driver
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl = PageLogin(driver)
    pi = PageIndex(driver)
    pl.login_success(cd.login_username, cd.login_password)
    pi.enter_pageDoubleMenu(cd.menuName[4]['NameMenuLeve1'], cd.menuName[4]['NameMenuLeve2'])

    cdp = TestCheckDataByPortfolio(driver)
    yield(cdp)
    driver.quit()





