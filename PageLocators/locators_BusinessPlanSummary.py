from selenium.webdriver.common.by import By

class LocatorsBusinessPlanv:
    #菜单元素相关
    ele_iframe1 = (By.ID, 'ifsidebar')  # 定位iframe
    ele_bpt = (By.XPATH, '//a[text()="Business Plannning Tool"]')  # 定位bpt
    menu_businessPlan = (By.XPATH, '//a[@tagid="CBT_EMEA_Business_Plan"]')  #定位一级菜单business plan
    menu_countryPlan = (By.XPATH, '//a[text()="Country Portfolio & Plan"]') #定位二级菜单country plan
    ele_iframe2 = (By.ID, 'ifContent')  #切换二级iframe
   # 创建business plan summary
    menu_businessSummary = (By.XPATH, '//a[text()="Business Plan Summary"]')  #选择business plan summary菜单元素
    button_portfolioSummaryCreate = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnCreate"]')  #创建portfolio summary按钮
    ele_iframe4 = (By.XPATH, '//iframe[contains(@name,"OpenID")]')  #切换创建弹窗中的ifram
    select_summaryCountryGroup = (By.XPATH, '//*[@id="spCountry"]/span/span/span')  #点击country group下拉框
    ele_summaryCountry= (By.XPATH, '//span[text()="Taiwan"]')  #选择country group下拉框中的国家
    select_summaryPlanCycle = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY21/22Q1"]')  #选择Plan Cycle
    select_summaryProductGroup = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddl_ProductGroup"]//option[text()="Mobile Gaming"]')#选择Product Group
    select_summarySave = (By.XPATH, '//input[@value="Save"]')#保存按钮
    button_summarySave = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSubmit"]')  # submit
    button_summarySave1 = (By.XPATH, '//button[@id="btnSave"]') #弹框提交按钮

    #进入审批页面审批plan
    menu_submtiCountryPlan = (By.XPATH, '//a[text()="Business Plan Approval"]')  # 定位二级菜单country plan  approval
    button_approvesearch = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]')
    ele_table = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gvApproveList"]/tbody/tr[2]/td[1]/a')
    button_reject = (By.XPATH, '//input[@id="btnReject"]')
    buttonreject_approvesearch = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSave"]')

    #删除summary
    select_summaryCountryGroup1 = (By.XPATH, '//*[@id="spCountry"]/span/span/span')  # 点击country group下拉框
    ele_summaryCountry1 = (By.XPATH, '//span[text()="Taiwan"]')  # 选择country group下拉框中的国家
    select_summaryPlanCycle1 = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY21/22Q1"]')
    button_approvesearch1 = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]')
    button_apps1 = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSearch"]')
    ele_tabledelete1 = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gv"]/tbody/tr[2]/td[11]/a')

    # 删除businessplan
    select_summaryCountryGroup2 = (By.XPATH, '//*[@id="spCountry"]/span/span/span')  # 点击country group下拉框
    ele_summaryCountry2 = (By.XPATH, '//span[text()="Taiwan"]')  # 选择country group下拉框中的国家
    select_summaryPlanCycle2 = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY21/22Q1"]')
    button_approvesearch2 = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]')
    button_apps2 = (By.XPATH, '//input[@id="ContentPlaceHolder1_BtnSearch"]')
    ele_tabledelete2 = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gv"]/tbody/tr[2]/td[11]/a')


    #重新定位元素
    ele_iframecc = (By.ID, 'ifsidebar')  # 定位iframe