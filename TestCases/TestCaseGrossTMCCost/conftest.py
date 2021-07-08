import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex
from PageObjects.page_GrossTMCCost import PageGrossTMCCost

driver=None
@pytest.fixture(scope='class')
def for_policyList_class():
    global driver
    driver=webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl=PageLogin(driver)
    pi=PageIndex(driver)
    pgtc=PageGrossTMCCost(driver)
    pl.login_success(cd.login_username,cd.login_password)
    pi.enter_main_menu(cd.menuName[0]['MainMenu'])
    yield(pgtc,)
    driver.quit()



@pytest.fixture()
def for_policyList_function():
    PageIndex(driver).enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'],cd.menuName[1]['NameMenuLeve2'])
