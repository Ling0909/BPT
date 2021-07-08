from selenium.webdriver.common.by import By
class LocatorsUnitFunding:
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')
    input_portfolioNo = (By.XPATH, '//input[@id="txtPortfolioNo"]')  # 定位PortfolioNo输入搜索框
    list_results_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]/tr/td[2]')
    button_search = (By.XPATH, '//input[@id="btnSearch"]')  # 定位search按钮
    # 定位搜索结果中的portfolioNo
    ele_portfolio = (By.XPATH, '//tbody[@id="search-tbody"]//td[13]/a[@title="Delete"]/../../td[2]')
    # 定位搜索结果中的country
    countryValue_on_portfolioList = (By.XPATH, '//tbody[@id="search-tbody"]//td[3]')
    input_country = (By.ID, 'txtCountry')  # 定位country输入条件框
    # 在下拉列表的输入框中输入country信息
    input_country_in_list = (By.ID, 'txtCountrytreeKey')
    ele_geo_in_list = (By.ID, 'txtCountrytreeId_1_span')  # 定位下拉框中的GEO值
    ele_product_title_result = (By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[2]')  # 定位lineCode搜索结果中的第一条数据的lineCode或productfamiliy，用来双击进入详情页
    ele_title_secondLine = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[2]/div[2]//span[@class="ag-header-cell-text"]')
    # 在product界面定位lineCode筛选输入框
    input_product_lineCode = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[3]/div[2]//input')
    # 如果没有lineCode，在product界面定位PN筛选输入框
    input_product_PN = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[3]/div[3]//input')
    eles_lineCode = (By.XPATH, '//div[@col-id="Line Code"]')  # 定位搜索结果中的lineCode值
    eles_PN = (By.XPATH, '//div[@col-id="PN"]')  # 定位搜索结果中的PN值

    # 定位portfolio详情界面信息
    ele_country=(By.XPATH, '//span[text()="Country"]/../..//input')  # 定位country
    ele_load_img = (By.XPATH, '//div[@id="splash" and @style=""]')
    ele_load_img_disappear=(By.XPATH, '//div[@id="splash" and @style="display: none;"]')
    button_Calculate= (By.XPATH,'//input[@value="Calculate"]')  # 定位Calculate按钮

    # 定位Special Funding($)字段值
    ele_Special_Funding=(By.XPATH,'//span[text()="Special Funding($)"]/../..//input')
    # 定位GEO Funding(MOU) ($)字段平均值
    ele_GEO_FundingMOU=(By.XPATH,'//span[text()="GEO Funding(MOU) ($)"]/../..//input[1]')
    eles_GEO_FundingMOU_Month=(By.XPATH,'//span[text()="GEO Funding(MOU) ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')# 定位GEO Funding(MOU) ($)字段各月份值
    # 定位GEO Funding(Others) 1 ($)字段平均值
    ele_avg_GEO_FundingOthers1 = (By.XPATH,'//span[text()="GEO Funding(Others) 1 ($)"]/../..//input[1]')
    eles_GEO_FundingOthers1_Month = (By.XPATH, '//span[text()="GEO Funding(Others) 1 ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位GEO Funding(Others) 1 ($)字段各月份值
    # 定位GEO Funding(Others) 2 ($)字段平均值
    ele_avg_GEO_FundingOthers2 = (By.XPATH,'//span[text()="GEO Funding(Others) 2 ($)"]/../..//input[1]')
    eles_GEO_FundingOthers2_Month = (By.XPATH, '//span[text()="GEO Funding(Others) 2 ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位GEO Funding(Others) 2 ($)字段各月份值
    # 定位GEO Funding(Others) 3 ($)字段平均值
    ele_avg_GEO_FundingOthers3 = (By.XPATH,'//span[text()="GEO Funding(Others) 3 ($)"]/../..//input[1]')
    eles_GEO_FundingOthers3_Month = (By.XPATH,'//span[text()="GEO Funding(Others) 3 ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位GEO Funding(Others) 3 ($)字段各月份值
    # 定位GEO Funding(Others) 4 ($)字段平均值
    ele_avg_GEO_FundingOthers4 = (By.XPATH,'//span[text()="GEO Funding(Others) 4 ($)"]/../..//input[1]')
    eles_GEO_FundingOthers4_Month = (By.XPATH,'//span[text()="GEO Funding(Others) 4 ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位GEO Funding(Others) 4 ($)字段各月份值
    # 定位Funding 1 (CPU)($)字段平均值
    ele_avg_Funding1_CPU = (By.XPATH,'//span[text()="Funding 1 (CPU)($)"]/../..//input[1]')
    eles_Funding1_CPU_Month = (By.XPATH,'//span[text()="Funding 1 (CPU)($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位Funding 1 (CPU)($)字段各月份值
    # 定位Funding 2 (HDD)($)字段平均值
    ele_avg_Funding2_HDD_SSHD_SSD= (By.XPATH,'//span[text()="Funding 2 (HDD)($)"]/../..//input[1]')
    eles_Funding2_HDD_SSHD_SSD_Month= (By.XPATH,'//span[text()="Funding 2 (HDD)($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位Funding 2 (HDD)($)字段各月份值
    # 定位Funding 3 (Others)($)字段平均值
    ele_avg_Funding3_Others= (By.XPATH,'//span[text()="Funding 3 (Others)($)"]/../..//input[1]')
    eles_Funding3_Others_Month = (By.XPATH, '//span[text()="Funding 3 (Others)($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位Funding 3 (Others)($)字段各月份值
    # 定位WW Funding ($)字段平均值
    ele_avg_WW_Funding= (By.XPATH,'//span[text()="WW Funding ($)"]/../..//input[1]')
    eles_WW_Funding_Month=(By.XPATH, '//span[text()="WW Funding ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位WW Funding ($)字段各月份值
    # 定位Segment Funding ($)字段平均值
    ele_avg_SegmentFunding= (By.XPATH,'//span[text()="Segment Funding ($)"]/../..//input[1]')
    eles_SegmentFunding_Month = (By.XPATH, '//span[text()="Segment Funding ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')  # 定位Segment Funding ($)字段各月份值

    #定位Brazil国家的GEO Funding(Others) ($)字段平均值
    ele_avg_GEO_FundingOthers_Brazil=(By.XPATH,'//span[text()="GEO Funding(Others) ($)"]/../../input')
    eles_GEO_FundingOthers_Brazil_Month=(By.XPATH,'//span[text()="GEO Funding(Others) ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')

    # 定位Unit Funding ($)字段平均值
    ele_avg_UnitFunding= (By.XPATH, '//span[text()="Unit Funding ($)"]/../..//input')
    eles_UnitFunding_Month= (By.XPATH, '//span[text()="Unit Funding ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')  # 定位Unit Funding ($)字段各月份值
