import pytest
from selenium import webdriver
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex
from PageObjects.page_PolicyList import PagePolicyList
from PageObjects.page_portfolioPlan import PagePortfolioPlan
from Common.datas_stor import DatasStor

@pytest.fixture(scope='session')
def add_portfolio_session():
    driver=webdriver.Chrome()
    driver.get(cd.login_url)
    pl=PageLogin(driver)
    pi=PageIndex(driver)
    ppp = PagePortfolioPlan(driver)
    pl.login_success(cd.login_username,cd.login_password)
    pi.enter_main_menu(cd.menuName[0]['MainMenu'])
    datas_portfolio = ppp.get_datas_excel()
    datas_portfolio_new = DatasStor.datas_portfolio_new
    for data in datas_portfolio:
        pi.enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'], cd.menuName[1]['NameMenuLeve2'])
        get_datas = ppp.add_portfolio_datas(data)
        datas_portfolio_new.append(get_datas)
    # setattr(DatasStor, 'datas_portfolio_new', datas_portfolio_new)
    yield(driver,datas_portfolio_new)
    pi.enter_pageDoubleMenu(cd.menuName[1]['NameMenuLeve1'], cd.menuName[1]['NameMenuLeve2'])
    for data in datas_portfolio:
        ppp.del_portfolio_datas(data)
    driver.quit()