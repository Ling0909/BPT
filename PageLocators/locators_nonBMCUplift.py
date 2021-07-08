from selenium.webdriver.common.by import By
class LocatorsNonBMCUplift:
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')  # 定位iframe
    select_policyType = (By.XPATH, '//select[@id="ddlPolicyType"]')  # 定位policyType筛选框
    select_productGroup = (By.XPATH, '//select[@id="ddlProductGroup"]')  # 定位productGroup筛选框
    button_search = (By.XPATH, '//input[@id="btnSearch"]')  # 定位search按钮
    # 定位加载好数据后，第一条数据的policy值
    load_ok = (By.XPATH, '//section[@id="borderBox"]//tbody[@id="search-tbody"][1]//td[1]')
    # 定位第一个界面的export按钮
    button_export = (By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$ctl00"]')

    ele_iframe_export = (By.XPATH, '//iframe[contains(@name,"OpenartDialog")]')  # 弹框后，定位iframe
    # 定位弹框后的export按钮
    button_export_in_frame = (By.XPATH, '//input[@name="ctl00$ContentPlaceHolder1$btnExport"]')
    aui_close = (By.XPATH, '//a[@class="aui_close"]')  # 定位弹框上的关闭按钮
    # 定位Country Adjustment %字段平均值
    ele_CountryAdjustment = (By.XPATH, '//span[text()="Country Adjustment %"]/../..//input[1]')
    eles_CountryAdjustment_months = (By.XPATH, '//span[text()="Country Adjustment %"]/../../../..//div[@class="input-group-addon"]')
    eles_CountryAdjustment_mouthsValues = (By.XPATH, '//span[text()="Country Adjustment %"]/../../../..//div[@class="col-xs-2"]/div/input')  # 定位Country Adjustment %字段各月份值
    # 定位PCA %字段平均值
    ele_PCA =(By.XPATH,'//span[text()="PCA %"]/../..//input')
    # eles_PCA_months = (By.XPATH, '//span[text()="PCA %"]/../../../..//div[@class="input-group-addon"]')
    eles_PCA_mouthsValues=(By.XPATH,'//span[text()="PCA %"]/../../../..//div[@class="col-xs-2"]/div/input')  # 定位Country Adjustment %字段各月份值
    # 定位Add Policy按钮
    button_AddPolicy = (By.XPATH, '//input[@value="Add Policy"]')
    button_import = (By.XPATH, '//input[@value="Import"]')

    input_File_Upload = (By.ID, 'FileUpload1')  # iframe框中的文件名输入框

    button_import_in_iframe = (By.ID, 'btnImport')