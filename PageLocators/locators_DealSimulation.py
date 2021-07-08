from selenium.webdriver.common.by import By


class locatorsDealSimulator():
    # 创建Deal Simulation
    ele_iframe2 = (By.XPATH, '//iframe[@id="ifContent"]')  #切换二级iframe
    btnCreateDeal = (By.ID,'ContentPlaceHolder1_btnCreateDeal') #定位Create Deal按钮
    ele_iframe3 = (By.XPATH,'//iframe[contains(@src,"CreateDeal.aspx")]') #切换创建Create Deal弹框iframe
    select_DC_ele = (By.XPATH,'//select[@id="ContentPlaceHolder1_ddlShipRoute"]//option[text()="Direct"]') #定位DC
    select_Country_R_ele = (By.XPATH,'//select[@id="ddlRetailCountry"]//option[text()="Italy"]')  #定位Country(R)
    customer_ele = (By.XPATH,'//*[@id="spRetailCustomer"]/span/span/span')    #定位Customer
    # customer_select=(By.XPATH,'//span[text()="神腦國際企業股份有限公司/1213565968"]/parent::div[1]') #/parent::div[1]
    #customer_select = (By.XPATH,'//div[@id="_easyui_tree_1"]') #定位customer文本 _easyui_tree_51
    customer_select = (By.XPATH,'// span[text() = "ao.com/1214733711"][1]')
    btn_next_ele = (By.XPATH,'//button[text()="Next"]') #定位Next按钮

    # Select From MTM
    search_ele = (By.XPATH,'//input[@id="ContentPlaceHolder1_BtnSearch"]')
    mtm_btn_ele = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnSelectMTM"]')  #定位Select From MTM按钮
    input_pn_ele = (By.XPATH,'//input[@id="ContentPlaceHolder1_txtPN"]')    #定位MTM弹窗里PN輸入文本框
    search_btn = (By.XPATH,'//input[@id="ContentPlaceHolder1_btnSearch"]')  #定位MTM弹窗里search按钮
    mtmItem_ele = (By.XPATH,'//*[@id="ContentPlaceHolder1_rpMTMinfo_cbMTMID_0"]') #定位MTM弹窗里的复选框
    search_close_btn = (By.XPATH,'//input[@id="ContentPlaceHolder1_btnCreateNewLineup"]') #定位MTM弹窗里Save&Close按钮
    saveAndNext_btn = (By.XPATH, '//input[@id="ContentPlaceHolder1_btnSaveAndNext"]') #定位MTM弹窗里Save&Next按钮
    savingLoading = (By.XPATH, '//span[@id="loadedName"]')

    # Edit Deal Item
    Found_ele = (By.XPATH,'//*[@id="psearch"]')
    dealItem_checkbox = (By.XPATH,'//input[@class="ag-input-field-input ag-checkbox-input"]') #定位Deal Item前的checkbox
    firstItem_checkbox = (By.XPATH,'//*[@id="g_grid"]//div[@class="ag-pinned-left-cols-container"]/div[1]//span[1]//input[@class="ag-input-field-input ag-checkbox-input"]')
    view_ele = (By.XPATH, '//div[@class="ag-body-viewport ag-layout-normal ag-row-animation"]')
    mtmEdit_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnEdit"]') #定位Deal Item的Edit
    input_volumeCount_ele = (By.XPATH,'//input[@id="ContentPlaceHolder2_txtTotalVolume"]') #定位volume
    input_streetPrice_ele = (By.XPATH,'//input[@id="ContentPlaceHolder2_txtStreetPriceLC"]')
    select_mot_ele = (By.XPATH,'//select[@id="ContentPlaceHolder2_ddlMOT"]//option[text()="Air"]')  #MOT选择Air
    saveClose_btn = (By.XPATH,'//input[@id="ContentPlaceHolder2_btnSave"]')

    # Copy Deal Item
    search_btn2 = (By.XPATH, '//input[@id="ContentPlaceHolder1_BtnSearch"]')
    copyItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnCopy"]')

    # show log Deal Item
    logItem_btn = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnShwoLog"]')

    # Delete Deal Item
    deleteItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnDelete"]')

    # Submit Deal Item
    dealItem_submit = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnSubmit"]')  #定位Deal Item的submit按钮
    dealsubmit_btn = (By.XPATH,'//input[@id="ContentPlaceHolder1_btnSubmit"]') #定位提交窗口的submit按钮

    # Download Deal Item
    DownloadItem_btn = (By.XPATH,'//a[@id="ContentPlaceHolder2_btnDownload"]') #定位download按钮

    # Upload
    UploadItem_btn = (By.XPATH, '//a[@id="ContentPlaceHolder2_btnUpload"]')  # 定位upload按钮
    Uploadtext = (By.XPATH,'//input[@id="ContentPlaceHolder2_fpUpload"]') #定位upload时需要选择文件的文本框
    btnUpload = (By.XPATH,'//input[@id="ContentPlaceHolder2_btnUpload"]') #定位upload按钮