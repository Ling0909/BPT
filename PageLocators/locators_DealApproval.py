from selenium.webdriver.common.by import By


class locatorsDealApproval():
    # 导航到Deal Approval页面
    ele_iframe2 = (By.ID, 'ifContent')  #切换二级iframe
    ele_iframe4 = (By.ID, 'ifsidebar')  #切换iframe
    bpt_ele = (By.XPATH,'//a[text()="Business Plannning Tool"]')  # 定位bpt
    menu_dealApproval = (By.XPATH, '//a[text()="Deal Approval"]')  # 选择Deal Approval菜单
    dealNo_ele = (By.ID,'ctl00_ContentPlaceHolder1_rpDealList_ctl01_lbDetail') #选择Deal No
    search_ele = (By.XPATH, '//input[@id="ContentPlaceHolder1_BtnSearch"]')
    dealItem_checkbox = (By.XPATH, '//input[@class="ag-input-field-input ag-checkbox-input"]')  # 定位Deal Item前的checkbox
    firstItem_checkbox = (By.XPATH,'//*[@id="g_grid"]//div[@class="ag-pinned-left-cols-container"]/div[1]//span[1]//input[@class="ag-input-field-input ag-checkbox-input"]')
    dealItem_reject = (By.ID,'ContentPlaceHolder2_btnReject') #点击Reject按钮
    dealReject_btn = (By.XPATH,'//input[@id="ContentPlaceHolder1_btnSave"]') #定位审批窗口的approval按钮
    reset_btn_ele = (By.XPATH,'//input[@id="ContentPlaceHolder1_BtnReset"]')
    return_btn_ele = (By.ID,'ContentPlaceHolder2_btnCancel') #定位返回按钮

    #Copy Deal Item
    dealno_ele = (By.XPATH, '//a[@id="ContentPlaceHolder1_rpDealList_lbDetail_0"]')
    copy_btn_ele = (By.XPATH, '//a[@id="ContentPlaceHolder1_rpDealList_lbCopy_0"]')
    #删除Deal Item
    menu_dealSimulation = (By.XPATH, '//a[text()="Deal Simulation"]')  # 选择Deal Simulation菜单
    delete_btn_ele = (By.ID,'ContentPlaceHolder1_rpDealList_lbDelete_0')
    dealSimulation1 = (By.XPATH,'//a[text()="Exec Portfolio & Plan"]')
    dealSimulation2 = (By.XPATH, '//a[text()="Deal Simulation"]')