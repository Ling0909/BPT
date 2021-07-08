from selenium.webdriver.common.by import By
class LocatorsPolicyListPage:
    select_policyType=(By.XPATH,'//select[@id="ddlPolicyType"]') #定位policyType筛选框
    select_productGroup=(By.XPATH,'//select[@id="ddlProductGroup"]') #定位productGroup筛选框
    button_search=(By.XPATH,'//input[@id="btnSearch"]') #定位search按钮
    # 定位加载好数据后，第一条数据的policy值
    load_ok=(By.XPATH,'//section[@id="borderBox"]//tbody[@id="search-tbody"][1]//td[1]')
    # 定位第一个界面的export按钮
    button_export=(By.XPATH,'//input[@name="ctl00$ContentPlaceHolder1$ctl00"]')
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')#定位iframe
    ele_iframe_export=(By.XPATH,'//iframe[contains(@name,"OpenartDialog")]')#弹框后，定位iframe
    # 定位弹框后的export按钮
    button_export_in_frame=(By.XPATH,'//input[@name="ctl00$ContentPlaceHolder1$btnExport"]')
    aui_close=(By.XPATH,'//a[@class="aui_close"]')#定位弹框上的关闭按钮
    #定位Add Policy按钮
    button_AddPolicy=(By.XPATH,'//input[@value="Add Policy"]')
    button_import =(By.XPATH,'//input[@value="Import"]')

    button_File_Upload=(By.ID,'FileUpload1')#iframe框中的上传文件按钮

    button_import_in_iframe=(By.ID,'btnImport')
    #添加数据弹框定位

    #Description定位
    # input_Description=(By.ID,'txtDescription')
    # select_GEO=(By.ID,'ContentPlaceHolder1_ddlGeo')
    # select_Region=(By.ID,'ddlRegion')
    # select_Country=(By.ID,'ddlCountry')
    # select_AP_RTM=(By.ID,'ddlAPRTM')
    # select_Product_Group=(By.ID,'ContentPlaceHolder1_ddlGroup')
    # select_Product_Category=(By.ID,'ddlProductCategory')
    # select_Product_Series=(By.ID,'ContentPlaceHolder1_ddlProductSeries')
    # select_Product_Family = (By.ID, 'ddlProductCategory')