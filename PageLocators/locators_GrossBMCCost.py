from selenium.webdriver.common.by import By
class LocatorsGrossBMCCost:
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
    ele_region_in_list = (By.ID, 'txtCountrytreeId_2_span')  # 定位下拉框中的regionName值
    ele_product_title_result = (By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[2]')  # 定位lineCode搜索结果中的第一条数据的lineCode或productfamiliy，用来双击进入详情页
    ele_title_secondLine = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[2]/div[2]//span[@class="ag-header-cell-text"]')
    # 在product界面定位lineCode筛选输入框
    input_product_lineCode = (By.XPATH, '//div[@class="ag-pinned-left-header"]/div[3]/div[2]//input')
    eles_lineCode = (By.XPATH, '//div[@col-id="Line Code"]')  # 定位搜索结果中的lineCode值

    # 定位portfolio详情界面信息
    ele_load_img=(By.XPATH, '//div[@id="splash" and @style=""]')
    ele_load_img_disappear = (By.XPATH, '//div[@id="splash" and @style="display: none;"]')
    ele_country=(By.XPATH, '//span[text()="Country"]/../..//input')  # 定位country
    ele_Sales_mode=(By.XPATH,'//div[contains(text(),"Sales mode")]/..//select//option[@selected="selected"]')
    button_Calculate= (By.XPATH,'//input[@value="Calculate"]')  # 定位Calculate按钮

    # 定位BMC Cost ($)字段各月份值
    eles_BMCCost_Month = (By.XPATH,'//h3[text()="Cost & Funding"]/../../../..//span[text()="BMC Cost ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')
    # 定位Freight Cost ($)字段各月份值
    eles_FreightCost_Month = (By.XPATH, '//span[text()="Freight Cost ($)"]/../..//input[1]/../../../div[@class="col-xs-2"]//input')
    # 定位PN Assessment ($)字段各月份值
    eles_PNAssessment_Month = (By.XPATH, '//span[text()="PN Assessment ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    # 定位Aggregate/Custom Duty ($)字段各月份值
    eles_AggregateCustomDuty_Month=(By.XPATH, '//span[text()="Aggregate/Custom Duty ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')


    # 定位Carry Case ($)字段值
    ele_CarryCase_Value = (By.XPATH, '//span[text()="Carry Case ($)"]/../..//input')
    # 定位Line Code ($)字段值
    ele_LineCode_Value = (By.XPATH, '//span[text()="Line Code ($)"]/../..//input')
    # 定位Insurance ($)字段值
    ele_Insurance_Value = (By.XPATH, '//span[text()="Insurance ($)"]/../..//input')
    # 定位Insurance ($)字段值
    ele_OEM_Value = (By.XPATH, '//span[text()="OEM ($)"]/../..//input')
    # 定位Geo real cost (BMC Adder)字段值
    ele_Geo_real_cost_Value = (By.XPATH, '//span[text()="Geo real cost (BMC Adder)"]/../..//input')
    # 定位ThinkVision Importer Label字段值
    ele_ThinkVisionImporterLabel_Value = (By.XPATH, '//span[text()="ThinkVision Importer Label"]/../..//input')
    # 定位Local Logistic Cost ($)字段值
    ele_LocalLogisticCost_Value = (By.XPATH, '//span[text()="Local Logistic Cost ($)"]/../..//input[1]')

    # 定位Gross BMC Cost ($)字段平均值
    ele_avg_GrossBMCCost= (By.XPATH, '//span[text()="Gross BMC Cost ($)"]/../..//input')
    eles_GrossBMCCost_Month= (By.XPATH, '//span[text()="Gross BMC Cost ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')  # 定位Unit Funding ($)字段各月份值
