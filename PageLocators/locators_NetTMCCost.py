from selenium.webdriver.common.by import By
class LocatorsNetTMCCost:
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')
    input_portfolioNo = (By.XPATH, '//input[@id="txtPortfolioNo"]')  # 定位PortfolioNo输入搜索框
    list_results_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]/tr/td[2]')
    button_search = (By.XPATH, '//input[@id="btnSearch"]')  # 定位search按钮
    # 定位搜索结果中的portfolioNo
    ele_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]//td[13]/a[@title="Delete"]/../../td[2]')

    ele_product_title_result = (By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[2]')  # 定位lineCode搜索结果中的第一条数据的lineCode或productfamiliy，用来双击进入详情页
    ele_title_secondLine = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[2]/div[2]//span[@class="ag-header-cell-text"]')
    # 在product界面定位lineCode筛选输入框
    input_product_lineCode = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[3]/div[2]//input')
    eles_lineCode = (By.XPATH, '//div[@col-id="Line Code"]')  # 定位搜索结果中的lineCode值


    # 定位portfolio详情界面信息
    ele_load_img = (By.XPATH, '//div[@id="splash" and @style=""]')
    ele_load_img_disappear = (By.XPATH, '//div[@id="splash" and @style="display: none;"]')
    ele_country=(By.XPATH, '//span[text()="Country"]/../..//input')  # 定位country
    button_Calculate= (By.XPATH,'//input[@value="Calculate"]')  # 定位Calculate按钮

    # 定位Net BMC Cost ($)(inc freight / MOT)字段各月份值
    eles_Net_BMC_Cost_Month= (By.XPATH, '//span[text()="Net BMC Cost ($)(inc freight / MOT)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位non-BMC Uplift (%)字段各月份值
    eles_non_BMC_Uplift_Month = (By.XPATH,'//span[text()="non-BMC Uplift (%)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位Country Adjustment %字段各月份值
    eles_CountryAdjustment1_Month = (By.XPATH, '//span[text()="Country Adjustment %"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位Country Adjustment ($)字段各月份值
    eles_CountryAdjustment2_Month = (By.XPATH, '//span[text()="Country Adjustment ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位Warranty Cost($)字段各月份值
    eles_WarrantyCost_Month = (By.XPATH, '//span[text()="Warranty Cost($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位ADP($)字段各月份值
    eles_ADP_Month = (By.XPATH, '//span[text()="ADP($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位Geo real cost (TMC Adder) 字段各月份值
    eles_Geo_real_cost_Month=(By.XPATH, '//span[text()="Geo real cost (TMC Adder)"]/../..//input/../../../div[@class="col-xs-2"]//input')

    #定位Gross TMC Cost ($)字段平均值
    ele_avg_Net_TMC_Cost=(By.XPATH, '//span[text()="Net TMC Cost ($)"]/../..//input')
    eles_Net_TMC_Cost_Month = (By.XPATH,'//span[text()="Net TMC Cost ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')  # 定位BMC Cost w/ Fundings($)字段各月份值
