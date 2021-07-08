import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex
from PageObjects.page_PolicyList import PagePolicyList
from PageObjects.page_portfolioPlan import PagePortfolioPlan
from TestDatas.datas_policyList import DatasPolicyList as dpl
from Common.datas_stor import DatasStor

@pytest.fixture(scope='class')
@pytest.mark.usefixtures('add_portfolio_session')
def for_policyList_class(add_portfolio_session):
    driver=add_portfolio_session[0]
    pi=PageIndex(driver)
    ppl=PagePolicyList(driver)
    ppp = PagePortfolioPlan(driver)
    pi.enter_main_menu(cd.menuName[0]['MainMenu'])
    pi.enter_pageDoubleMenu(cd.menuName[0]['NameMenuLeve1'], cd.menuName[0]['NameMenuLeve2'])
    # ppl.add_policyList_Datas(dpl.datas_GEOFundingOthers1['import_file_path'])
    ppl.download_policyList(dpl.datas_GEOFundingOthers1['policyType'])
    datas_portfolio_all=add_portfolio_session[1]
    datas_GEOFundingOthers1=[]
    datas_region_isLAS=[]
    for data in datas_portfolio_all:
        if data['CostFundingDataName']=='datas_GEOFundingOthers1':
            datas_GEOFundingOthers1.append(data)
        elif data['CostFundingDataName']=='datas_region_isLAS':
            datas_region_isLAS.append(data)
    setattr(DatasStor,'datas_GEOFundingOthers1',datas_GEOFundingOthers1)
    setattr(DatasStor, 'datas_region_isLAS', datas_region_isLAS)
    yield(ppl,ppp)
    # driver.quit()
@pytest.fixture()
@pytest.mark.usefixtures('add_portfolio_session')
def for_policyList_function(add_portfolio_session):
    driver=add_portfolio_session[0]
    PageIndex(driver).enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'],cd.menuName[1]['NameMenuLeve2'])