import pytest
from selenium import webdriver
from PageObjects.page_ExectuonBusinessPlanSummary import PageBusinessPlanv
from TestDatas.common_datas import CommonDatas as cd
from PageObjects.page_login import PageLogin
from PageObjects.page_index import PageIndex

driver = None
@pytest.fixture(scope='class')
def for_executionPlansummary_class():
    global driver
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    pl = PageLogin(driver)
    pi = PageIndex(driver)
    pl.login_success(cd.login_username, cd.login_password)

    pv=PageBusinessPlanv(driver)
    yield(pv)
    driver.quit()





