import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex
from PageObjects.page_fundingManagement import PageFundingManagement
from PageObjects.page_portfolioPlan import PagePortfolioPlan
from TestDatas.datas_fundingManagement import DatasFundingManagement as dfm

driver=None
@pytest.fixture(scope='class')
def for_policyList_class():
    global driver
    driver=webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl=PageLogin(driver)
    pi=PageIndex(driver)
    pfm=PageFundingManagement(driver)
    ppp = PagePortfolioPlan(driver)
    pl.login_success(cd.login_username,cd.login_password)
    pi.enter_main_menu(cd.menuName[2]['MainMenu'])
    pi.enter_pageSingleMenu(cd.menuName[2]['NameMenuLeve1'])
    # pfm.add_fundingManagement_Datas(dfm.datas_Funding2_HDD_SSHD_SSD['import_file_path'])
    pfm.download_policyTemplate(dfm.datas_Funding2_HDD_SSHD_SSD['policyType'])
    pi.enter_main_menu(cd.menuName[1]['MainMenu'])
    yield(pfm,ppp)
    driver.quit()



@pytest.fixture()
def for_policyList_function():
    PageIndex(driver).enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'],cd.menuName[1]['NameMenuLeve2'])
    # yield
    # driver.refresh()
