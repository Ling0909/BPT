import pytest
from selenium import webdriver

from PageObjects.page_DealSimulation import PageDealSimulation
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex

'''
    Deal Simulation
'''
driver = None
@pytest.fixture(scope='class')
def for_dealSimulation_class():
    global driver
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl = PageLogin(driver)
    pi = PageIndex(driver)
    pl.login_success(cd.login_username, cd.login_password)
    pi.enter_pageDoubleMenu_executePlan(cd.menuName[9]['NameMenuLeve1'], cd.menuName[9]['NameMenuLeve2'])

    pd = PageDealSimulation(driver)
    yield(pd)
    driver.quit()

