from selenium.webdriver.common.by import By

class LocatorsBusinessPlan:
    # 创建business plan
    ele_iframe1 = (By.ID, 'ifsidebar')  # 定位iframe
    ele_bpt = (By.XPATH, '//a[text()="Business Plannning Tool"]')  # 定位bpt
    menu_businessPlan = (By.XPATH, '//a[@tagid="CBT_EMEA_Business_Plan"]')  #定位一级菜单business plan
    menu_countryPlan = (By.XPATH, '//a[text()="Country Portfolio & Plan"]') #定位二级菜单country plan
    ele_iframe2 = (By.ID, 'ifContent')  #切换二级iframe
    button_createPortfolio = (By.XPATH, '//input[@id="btnCreatePortfolio"]')  #定位创建portfolio按钮
    ele_iframe3 = (By.XPATH, '//iframe[contains(@src,"CreatePortfolio.aspx?basetype=1&Name=Create Portfolio")]')  # 切换创建弹窗iframe
    select_countryGroup = (By.XPATH, '//div[@id ="ContentPlaceHolder1_upMain"]/div[1]/div/div/div/div/div/div[1]/div/span/span/span')  #选择country group下拉
    select_country = (By.XPATH, '//span[text()="Taiwan"]')  #选择country
    select_productGroup = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddl_ProductGroup"]//option[text()="Mobile Gaming"]') #选择Product Group
    select_planCycle = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddl_Quarter"]//option[text()="FY21/22Q1"]')  #选择Plan Cycle
    select_portfolioType = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="Channel"]')  #选择Portfolio Type
    ele_portfolioName = (By.ID, 'ContentPlaceHolder1_txt_PortfolioName') #填写Portfoli
    button_next = (By.XPATH, '//button[text()="Next"]')  #下一步按钮
    button_searchh= (By.XPATH, '//input[@id="ContentPlaceHolder1_BtnSearch"]')#浮动到search按钮
    select_portfolioNo = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[2]/td[1]')  # 点击portfolio no.进入详情页
    button_mtm = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnSelectMTM"]')  # 选择mtm按钮
    button_mtmSearch = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSearch1"]')
    button_mtmSearch1 = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSearch"]')
    #mtm弹窗中的search按钮
    ele_mtmItem = (By.XPATH, '//table[@id="tbMTMinfo"]/tbody/tr[2]/td[1]//input[1]') #mtm弹窗中的item
    button_mtmSaveClose = (By.XPATH, '//input[@value="Save & Close"]')  #mtm弹窗中的save&close按钮
    check_item  = (By.XPATH, '//div[@role="presentation"]/div[2]/input[@class="ag-input-field-input ag-checkbox-input"]') #item前面复选框
    button_mtmEdit = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnEdit"]')
    ele_iframe5 = (By.ID, 'myiframe1')
    button_mtmEdit = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnEdit"]')
    #弹框填写内容
    customer_ele=(By.XPATH, '//*[@id="spCountry"]/span/span/span')
    customer_select = (By.XPATH, '//button[text()="神腦國際企業股份有限公司/1213565968"]')
    business_partner_ele = (By.XPATH, '//*[@id="spCountry2"]/span/span/span')
    business_partner_select = (By.XPATH, '//button[text()="神腦國際企業股份有限公司/1213565968"]')
    carrying_case = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtCarryingCase"]')
    distributor_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtDistributorMargin"]')
    reseller_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtRetailerMarginPercent"]')
    volume1_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume0"]')
    volume2_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume1"]')
    volume3_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume2"]')
    volume4_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume3"]')
    volume5_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume4"]')
    volume6_ele = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTotalVolume5"]')
    volume2_auto = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnVolume0"]')
    buying_price1 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC0"]')
    buying_price2 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC1"]')
    buying_price3 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC2"]')
    buying_price4 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC3"]')
    buying_price5 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC4"]')
    buying_price6 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtStreetPriceLC5"]')
    buying_auto = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnStreetPrice0"]')
    retail_rebates= (By.XPATH, '//input[@id="ContentPlaceHolder2_txtRetailRebatesFixAmountLC"]')
    retail_rebates2 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtRetailRebatesPercent"]')
    special_funding =(By.XPATH, '//input[@id="ContentPlaceHolder2_txtSpecialFunding"]')
    american1=(By.XPATH, '//input[@id="ContentPlaceHolder2_txtRetailRebatesFixAmountLC"]')
    american2 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtSalesoutprovision"]')
    american3 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtPriceRisk"]')
    american4 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtDGFAccrual"]')
    american5 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtDEMOAllowance"]')
    american6 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtTechDataAccrual"]')
    american7 = (By.XPATH, '//input[@id="ContentPlaceHolder2_txtRetailRebatesPercent"]')

    #计算按钮
    calc = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnCalculateAll"]')
    #保存并关闭按钮
    sa = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnSave"]')

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
    button_approvesearch1 = (By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]')
    ele_tabledelete = (By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_gv"]/tbody/tr[2]/td[11]/a')

    #下载及上传相关

    upload_dowload_button= (By.XPATH, '//a[@title="Upload & DownLoad"]')
    dowload_button= (By.XPATH, '//a[@onclick="OnDropdown()"]')
    dowload_button1 = (By.XPATH, '//a[@title="Download"]')

    upload_button = (By.XPATH, '//a[@id="ContentPlaceHolder2_IbnUpload"]')
    ele_iframe_export1 = (By.XPATH, '//iframe[contains(@name,"OpenartDialog")]')
    input_File_Upload = (By.ID, 'ContentPlaceHolder2_fpUpload')
    upload_button_tankuang = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnUpload"]')
    upload_button_refresh = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnRefresh"]')
    #重新定位元素
    ele_iframecc = (By.ID, 'ifsidebar')  # 定位iframe

    #Copy Portfolio Item
    firstItem_checkbox = (By.XPATH,'//span[contains(text(),"0001_P")]/parent::span//input[@class="ag-input-field-input ag-checkbox-input"]')
    copyItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnCopy"]')
    logItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnShwoLog"]')
    deleteItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnDelete"]')


    search_btn = (By.XPATH,'//input[@id="ContentPlaceHolder1_BtnSearch"]')

    # 下载customer模板和上传customer模板
    downloadaddcustomer=(By.XPATH,'//a[@title="AddCustomerTemplate"]')
    uploadcustomer=(By.XPATH,'//a[@id="ContentPlaceHolder2_btnUploadAddCustomer"]')
    ele_iframe_export2 = (By.XPATH, '//iframe[contains(@name,"OpenartDialog")]')
    tuploadcustomer = (By.XPATH, '//input[@id="ContentPlaceHolder2_fpUpload"]')
    tright_uploadcustomer = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnUpload"]')

    # 下载或上传mtm
    volume1_addmtm = (By.XPATH, '//a[@title="UploadMTM"]')
    ele_iframe_export3 = (By.XPATH, '//iframe[contains(@name,"OpenartDialog")]')
    downloadaddmtm = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnDownloadTeamplate"]')
    tuploadmtm = (By.XPATH, '//input[@id="ContentPlaceHolder2_fpUpload"]')
    tright_uploadmtm= (By.XPATH, '//input[@id="ContentPlaceHolder2_btnUpload"]')