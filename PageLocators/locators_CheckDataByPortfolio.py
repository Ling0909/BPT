from selenium.webdriver.common.by import By

class LocatorsBusinessPlan:
    # 菜单元素相关
    ele_iframe1 = (By.ID, 'ifsidebar')  # 定位iframe
    ele_bpt = (By.XPATH, '//a[text()="Business Plannning Tool"]')  # 定位bpt
    menu_businessPlan = (By.XPATH, '//a[@tagid="CBT_EMEA_Business_Plan"]')  # 定位一级菜单business plan
    menu_countryPlan = (By.XPATH, '//a[text()="Country Portfolio & Plan"]')
    menu_businessSummary = (By.XPATH, '//a[text()="Business Plan Summary"]')  # 定位二级菜单business plan summary
    ele_iframe2 = (By.ID, 'ifContent')  # 切换二级iframe
    # search business plan summary
    country = (By.XPATH, '//*[@id="spCountry"]/span/span/span') # 定位Country下拉框的三角符号
    select_country = (By.XPATH, '//span[text()="Ukraine"]')
    selectPlanCycle_ele = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY20/21Q4"]')  # 定位Plan Cycle筛选框
    searchBtn_ele = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSearch"]') # 定位Search按钮
    planSummaryNo_ele = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gv"]//tr[2]//td[1]/a')
    planSummaryNo_ele2 = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gv"]//tr[3]//td[1]/a') # 定位第二行的数据
    portfolioApprovalLog_ele = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnComments"]')

    NBPlan_ele = (By.XPATH, '//table[@class ="table table-bordered text-center"]//tr[2]//td[3]')
    TDTPlan_ele = (By.XPATH, '//table[@class ="table table-bordered text-center"]//tr[2]//td[4]')
    TablePlan_ele = (By.XPATH, '//table[@class ="table table-bordered text-center"]//tr[2]//td[5]')
    VisualPlan_ele = (By.XPATH, '//table[@class ="table table-bordered text-center"]//tr[2]//td[6]')
    OptionPlan_ele = (By.XPATH, '//table[@class ="table table-bordered text-center"]//tr[2]//td[7]')

    NB_CAs = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="NB@NB@Region Q Plan"]//td[2]')
    NB_Net_BMC_GP = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="NB@NB@Region Q Plan"]//td[7]')

    TDT_CAs = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="TDT/AIO@TDT/AIO@Region Q Plan"]//td[2]')
    TDT_Net_BMC_GP = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="TDT/AIO@TDT/AIO@Region Q Plan"]//td[7]')

    Tablet_CAs = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="Tablet@Tablet@Region Q Plan"]//td[2]')
    Tablet_Net_BMC_GP = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="Tablet@Tablet@Region Q Plan"]//td[7]')

    Option_CAs = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="Option@Option@Region Q Plan"]//td[2]')
    Option_Net_BMC_GP = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="Option@Option@Region Q Plan"]//td[7]')

    All_CAs = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="All@All@Region Q Plan"]//td[2]')
    All_Net_BMC_GP = (By.XPATH, '//table[@id="tblProduct"]//tr[@id="All@All@Region Q Plan"]//td[7]')

    # Country & Portfolio Plan页面
    portfolioNo_input = (By.ID, 'ContentPlaceHolder1_txt_PP_No')
    search_ele = (By.XPATH, '// input[ @ id = "ContentPlaceHolder1_BtnSearch"]')
    portfolioNo1 = (By.XPATH, '//a[@id="ContentPlaceHolder1_rpPortfolio_lbDetail_0"]')
    portfolioItem = (By.XPATH, '//button[@id="dropdown"]/h4')
    # 获取Portfolio Item数据
    totalVolume_ele = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalVolume"]')  # 定位totalVolume
    totalNetRevenue_ele = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalNetBMCGP"]')  # 定位totalNetRevenue
    backBtn_ele = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnCancel"]') # 定位Back按钮





