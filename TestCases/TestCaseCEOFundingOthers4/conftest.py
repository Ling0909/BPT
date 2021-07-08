import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex
from PageObjects.page_PolicyList import PagePolicyList
from PageObjects.page_portfolioPlan import PagePortfolioPlan
from TestDatas.datas_policyList import DatasPolicyList as dpl

driver=None
@pytest.fixture(scope='class')
def for_policyList_class():
    global driver
    driver=webdriver.Chrome()
    driver.get(cd.login_url)
    pl=PageLogin(driver)
    pi=PageIndex(driver)
    ppl=PagePolicyList(driver)
    ppp = PagePortfolioPlan(driver)
    pl.login_success(cd.login_username,cd.login_password)
    pi.enter_main_menu(cd.menuName[0]['MainMenu'])
    pi.enter_pageDoubleMenu(cd.menuName[0]['NameMenuLeve1'],cd.menuName[0]['NameMenuLeve2'])
    # ppl.add_policyList_Datas(dpl.datas_GEOFundingOthers4['import_file_path'])
    ppl.download_policyList(dpl.datas_GEOFundingOthers4['policyType'])
    yield(ppl,ppp)
    driver.quit()



@pytest.fixture()
def for_policyList_function():
    # PageIndex(driver).enter_main_menu(cd.menuName[0]['MainMenu'])
    PageIndex(driver).enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'],cd.menuName[1]['NameMenuLeve2'])
    # yield
    # driver.refresh()
