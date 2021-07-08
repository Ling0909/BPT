from selenium.webdriver.common.by import By

COLLAPSE_CV_ICON = 'collapseCVIcon'


class LocatorsPortfolioPlanPage:
    ele_iframe=(By.XPATH,'//iframe[@id="ifContent"]')
    input_portfolioNo=(By.XPATH,'//input[@id="txtPortfolioNo"]')#定位PortfolioNo输入搜索框
    list_results_portfolio=(By.XPATH,'//tbody[@id="search-tbody"]/tr/td[2]')
    input_country=(By.ID,'txtCountry')#定位country输入条件框
    #在下拉列表的输入框中输入country信息
    input_country_in_list=(By.ID,'txtCountrytreeKey')
    ele_geo_in_list=(By.ID,'txtCountrytreeId_1_span')#定位下拉框中的GEO值
    ele_region_in_list=(By.ID,'txtCountrytreeId_2_span')#定位下拉框中的regionName值
    ele_subRegion_in_list=(By.ID,'txtCountrytreeId_3_span')#定位下拉框中的subRegion的值
    button_search=(By.XPATH,'//input[@id="btnSearch"]')#定位search按钮
    #定位搜索结果中的portfolioNo
    ele_portfolio=(By.XPATH,'//tbody[@id="search-tbody"]//td[13]/a[@title="Delete"]/../../td[2]')
    #定位搜索结果中的country
    countryValue_on_portfolioList=(By.XPATH,'//tbody[@id="search-tbody"]//td[3]')
    #定位搜索 结果中的plan_cycle
    planCycle_on_portfolioList=(By.XPATH, '//tbody[@id="search-tbody"]/tr/td[5]')
    # ele_title_product=(By.XPATH,'//span[text()="Product" and @class="ag-header-group-text"]')#定位product标题
    ele_product_title_result=(By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[2]')  # 定位lineCode搜索结果中的第一条数据的lineCode或productfamiliy，用来双击进入详情页
    # list_results=(By.XPATH,'//div[@class="ag-pinned-left-cols-viewport"]//div[@row-id="0"]//div[@col-id="ck"]')#定位lineCode list列表中第一个选中框，用来判断列表是否加载出来
    ele_title_secondLine=(By.XPATH,'//div[@class="ag-pinned-left-header"]/div[2]/div[2]//span[@class="ag-header-cell-text"]')
    #在product界面定位lineCode筛选输入框
    ele_lineCode_OK = (By.XPATH, '//div[@class="ag-pinned-left-cols-container"]//div[@col-id="Line Code"][1]')
    input_product_lineCode=(By.XPATH,'//div[@class="ag-pinned-left-header"]/div[3]/div[2]//input')
    eles_lineCode=(By.XPATH,'//div[@col-id="Line Code"]')#定位搜索结果中的lineCode值

    #定位baseinfo界面信息
    ele_country=(By.XPATH, '//span[text()="Country"]/../..//input')#定位country
    ele_load_img = (By.XPATH, '//div[@id="splash" and @style=""]')
    ele_load_img_disappear=(By.XPATH, '//div[@id="splash" and @style="display: none;"]')
    ele_AP_RTM=(By.ID,'ddlAPRTM')#定位GEO为AP时，AP_RTM元素
    ele_productGroup=(By.ID,'ContentPlaceHolder1_txtProductGroup')
    ele_productCategory=(By.ID,'ContentPlaceHolder1_txtCategory')
    ele_productSeries=(By.ID,'txtProductSeriesName1')
    ele_productFamily=(By.ID,'txtProductFamilyName1')
    ele_PN=(By.ID,'ContentPlaceHolder1_txtPN')

    button_packUp=(By.ID, 'collapseCVIcon')#定位Configurator模块的展开/收起按钮
    ele_ChannelPrice=(By.ID,'ContentPlaceHolder1_txtCPriceUSD')  # 定位Channel Price($)值
    button_Calculate = (By.XPATH, '//input[@value="Calculate"]')  # 定位Calculate按钮

    #定位Cost & Funding界面信息
    #定位GEO Funding(Others) 1 ($)各项值
    ele_FundingOthers1=(By.XPATH,'//span[text()="GEO Funding(Others) 1 ($)"]/../..//input')#定位GEO Funding(Others) 1 ($)平均值
    eles_FundingOthers1_months=(By.XPATH,'//span[text()="GEO Funding(Others) 1 ($)"]/../..//input/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_FundingOthers1_mouthsValues=(By.XPATH,'//span[text()="GEO Funding(Others) 1 ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    #国家为Brazil时，定位GEO Funding(Others) ($)各项值
    ele_FundingOthers1_Brazil = (By.XPATH, '//span[text()="GEO Funding(Others) ($)"]/../..//input')  # 定位GEO Funding(Others) 1 ($)平均值
    eles_FundingOthers1_Brazil_months = (By.XPATH,'//span[text()="GEO Funding(Others) ($)"]/../..//input/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_FundingOthers1_Brazil_mouthsValues = (By.XPATH, '//span[text()="GEO Funding(Others) ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')

    #定位GEO Funding(Others) 2 ($)各项值
    ele_FundingOthers2=(By.ID,'txtGEOFundingOthersSecond')  # 定位GEO Funding(Others) 2 ($)平均值
    eles_FundingOthers2_months=(By.XPATH,'//input[@id="txtGEOFundingOthersSecond"]/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_FundingOthers2_mouthsValues=(By.XPATH,'//input[@id="txtGEOFundingOthersSecond"]/../../../div[@class="col-xs-2"]//input')
    # 定位GEO Funding(Others) 3 ($)各项值
    ele_FundingOthers3=(By.ID,'txtGEOFundingOthersThird')  # 定位GEO Funding(Others) 3 ($)平均值
    eles_FundingOthers3_months=(By.XPATH,'//input[@id="txtGEOFundingOthersThird"]/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_FundingOthers3_mouthsValues=(By.XPATH,'//input[@id="txtGEOFundingOthersThird"]/../../../div[@class="col-xs-2"]//input')
    # 定位GEO Funding(Others) 4 ($)各项值
    ele_FundingOthers4=(By.ID,'txtGEOFundingOthersForth')  # 定位GEO Funding(Others) 4 ($)平均值
    eles_FundingOthers4_months=(By.XPATH,'//input[@id="txtGEOFundingOthersForth"]/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_FundingOthers4_mouthsValues=(By.XPATH,'//input[@id="txtGEOFundingOthersForth"]/../../../div[@class="col-xs-2"]//input')
    # 定位Funding 1 (CPU)($)各项值
    ele_Funding1_CPU=(By.XPATH,'//span[text()="Funding 1 (CPU)($)"]/../..//input')  # 定位Funding 1 (CPU)($)平均值
    eles_Funding1_CPU_months=(By.XPATH,'//span[text()="Funding 1 (CPU)($)"]/../../../..//div[@class="col-xs-2"]/div/div')
    eles_Funding1_CPU_mouthsValues=(By.XPATH,'//span[text()="Funding 1 (CPU)($)"]/../../../..//div[@class="col-xs-2"]/div/input')
    # 定位Funding 2 (HDD)($)各项值
    ele_Funding2_HDD_SSHD_SSD=(By.XPATH,'//span[text()="Funding 2 (HDD)($)"]/../..//input')  # 定位Funding 1 (CPU)($)平均值
    eles_Funding2_HDD_SSHD_SSD_months=(By.XPATH,'//span[text()="Funding 2 (HDD)($)"]/../../../..//div[@class="col-xs-2"]/div/div')
    eles_Funding2_HDD_SSHD_SSD_mouthsValues=(By.XPATH,'//span[text()="Funding 2 (HDD)($)"]/../../../..//div[@class="col-xs-2"]/div/input')
    # 定位Funding 3 (Others)($)各项值
    ele_Funding3_Others=(By.XPATH,'//span[text()="Funding 3 (Others)($)"]/../..//input')  # 定位Funding 1 (CPU)($)平均值
    eles_Funding3_Others_months=(By.XPATH,'//span[text()="Funding 3 (Others)($)"]/../../../..//div[@class="col-xs-2"]/div/div')
    eles_Funding3_Others_mouthsValues=(By.XPATH,'//span[text()="Funding 3 (Others)($)"]/../../../..//div[@class="col-xs-2"]/div/input')
    #定位AP Cost Credit ($)各项值
    ele_APCostCredit=(By.XPATH, '//span[text()="AP Cost Credit ($)"]/../..//input')  # 定位AP Cost Credit ($)平均值
    eles_APCostCredit_months=(By.XPATH,'//span[text()="AP Cost Credit ($)"]/../..//input/../../../div[@class="col-xs-2"]//div[@class="input-group-addon"]')
    eles_APCostCredit_mouthsValues=(By.XPATH,'//span[text()="AP Cost Credit ($)"]/../..//input/../../../div[@class="col-xs-2"]//input')
    #定位Country Adjustment %各项值
    ele_CountryAdjustment=(By.XPATH, '//span[text()="Country Adjustment %"]/../..//input[1]') # 定位Country Adjustment %平均值
    eles_CountryAdjustment_months=(By.XPATH, '//span[text()="Country Adjustment %"]/../../../..//div[@class="input-group-addon"]')
    eles_CountryAdjustment_mouthsValues=(By.XPATH, '//span[text()="Country Adjustment %"]/../../../..//div[@class="col-xs-2"]/div/input')
    # 国家是Brazil时，定位Country Adjustment %各项值
    ele_CountryAdjustment_Brazil = (By.XPATH, '//span[text()="Country Adjustment (%)"]/../..//input[1]')  # 定位Country Adjustment %平均值
    eles_CountryAdjustment_Brazil_months = (By.XPATH, '//span[text()="Country Adjustment (%)"]/../../../..//div[@class="input-group-addon"]')
    eles_CountryAdjustment_Brazil_mouthsValues = (By.XPATH, '//span[text()="Country Adjustment (%)"]/../../../..//div[@class="col-xs-2"]//input')

    # 定位non-BMC Uplift (%)各项值
    ele_NonBMCUplift = (By.XPATH, '//span[text()="non-BMC Uplift (%)"]/../..//input[1]')  # 定位non-BMC Uplift (%)平均值
    eles_NonBMCUplift_months = (By.XPATH, '//span[text()="non-BMC Uplift (%)"]/../../../..//div[@class="input-group-addon"]')
    eles_NonBMCUplift_mouthsValues = (By.XPATH, '//span[text()="non-BMC Uplift (%)"]/../../../..//div[@class="col-xs-2"]/div/input')
    # 定位PN Assessment ($)各项值
    ele_PNAssessment = (By.XPATH, '//span[text()="PN Assessment ($)"]/../..//input[1]')  # 定位PN Assessment ($)平均值
    eles_PNAssessment_months = (By.XPATH, '//span[text()="PN Assessment ($)"]/../../../..//div[@class="input-group-addon"]')
    eles_PNAssessment_mouthsValues = (By.XPATH, '//span[text()="PN Assessment ($)"]/../../../..//div[@class="col-xs-2"]/div/input')
    # 定位Country Adjustment ($)各项值
    ele_CountryAdjustment2 = (By.XPATH, '//span[text()="Country Adjustment ($)"]/../..//input[1]')  # 定位Country Adjustment ($)平均值
    eles_CountryAdjustment2_months = (By.XPATH, '//span[text()="Country Adjustment ($)"]/../../../..//div[@class="input-group-addon"]')
    eles_CountryAdjustment2_mouthsValues = (By.XPATH, '//span[text()="Country Adjustment ($)"]/../../../..//div[@class="col-xs-2"]/div/input')

    #添加portfolio数据时，需要的元素
    input_portfolioname=(By.ID,'txtPortfolioName')
    button_del= (By.XPATH,'//tbody[@id="search-tbody"]//td[13]//a[@title="Delete"]')  #搜索结果中，定位符合条件的数据的删除按钮，来确定是否需要继续添加数据
    button_create=(By.ID,'ContentPlaceHolder1_btnCreate')#定位界面的create按钮
    ele_iframe_pop=(By.XPATH,'//iframe[contains(@name,"OpenartDialog")]')#定位弹窗层的iframe元素
    input_country_pop=(By.ID,'txtCountry')#定位弹窗上的country输入框
    input_search_country_pop=(By.ID,'txtCountrytreeKey')#在点击country框后，在下拉列表中定位search条件输入框
    select_product_group_pop=(By.ID,'ddlProductGroup')#定位弹窗上的Product Group筛选框
    select_plan_cycle_pop=(By.ID, 'ddlQuarter')#定位弹窗上的Plan Cycle筛选框
    input_portfolioName_pop=(By.ID,'ContentPlaceHolder1_txtPortfolioName')#定位弹窗上的Portfolio Name输入框
    button_create_pop=(By.ID,'ContentPlaceHolder1_btnCreate')#定位弹窗上的Next按钮

    #添加lineCode
    button_add_lineCode=(By.XPATH,'//button[@title="Add Data"]') #定位lineCode页面的添加“+”按钮
    button_add_from_MTM=(By.LINK_TEXT,'Select From MTM')#定位点击添加按钮后，下拉框中的Select From MTM按钮
    ele_check_box=(By.XPATH,'//tbody[@id="search-tbody"]/tr[1]//input')#定位Select From MTM List区域的第一个可选框
    button_sava=(By.ID,'ContentPlaceHolder1_btnSave')#定位Select From MTM界面的sava按钮
    ele_lineCode_baseInfo=(By.ID,'ContentPlaceHolder1_txtLineCode')
    #删除portfolioNo
    button_del_ok=(By.XPATH,'//button[@class="confirm" and contains(@style,"box-shadow: rgba")]')