from selenium.webdriver.common.by import By
class LocatorsBMCCostWFundings:
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')
    input_portfolioNo = (By.XPATH, '//input[@id="txtPortfolioNo"]')  # 定位PortfolioNo输入搜索框
    list_results_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]/tr/td[2]')
    button_search = (By.XPATH, '//input[@id="btnSearch"]')  # 定位search按钮
    # 定位搜索结果中的portfolioNo
    ele_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]//td[13]/a[@title="Delete"]/../../td[2]')
    # 定位搜索结果中的country
    countryValue_on_portfolioList = (By.XPATH, '//tbody[@id="search-tbody"]//td[3]')
    input_country = (By.ID, 'txtCountry')  # 定位country输入条件框
    ele_product_title_result = (By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[2]')  # 定位lineCode搜索结果中的第一条数据的lineCode或productfamiliy，用来双击进入详情页
    # 在product界面定位lineCode筛选输入框
    input_product_lineCode = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[3]/div[2]//input')
    eles_lineCode = (By.XPATH, '//div[@col-id="Line Code"]')  # 定位搜索结果中的lineCode值

    # 定位portfolio详情界面信息
    ele_country=(By.XPATH, '//span[text()="Country"]/../..//input')  # 定位country
    ele_load_img = (By.XPATH, '//div[@id="splash" and @style=""]')
    ele_load_img_disappear=(By.XPATH, '//div[@id="splash" and @style="display: none;"]')
    button_Calculate= (By.XPATH,'//input[@value="Calculate"]')  # 定位Calculate按钮
    # 定位BMC Cost ($)字段各月份值
    eles_BMC_Cost_Month= (By.XPATH, '//h3[text()="Cost & Funding"]/../../../..//span[text()="BMC Cost ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')
    # 定位Unit Funding ($)字段各月份值
    eles_UnitFunding_Month = (By.XPATH,'//span[text()="Unit Funding ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    #定位BMC Cost w/ Fundings($)字段平均值
    ele_avg_BMC_Cost_w_Fundings=(By.XPATH, '//span[text()="BMC Cost w/ Fundings($)"]/../..//input')
    eles_BMC_Cost_w_Fundings_Month = (By.XPATH,'//span[text()="BMC Cost w/ Fundings($)"]/../..//input/../../../div[@class="col-xs-2"]//input')  # 定位BMC Cost w/ Fundings($)字段各月份值
