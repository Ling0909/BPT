from selenium.webdriver.common.by import By
class LocatorsPNAssessmentPage:
    select_policyType=(By.ID,'ddlPolicyType') #定位policyType筛选框
    select_productGroup=(By.ID,'ddlProductGroup') #定位productGroup筛选框
    select_Country= (By.ID, 'txtCountry')  # 定位productGroup筛选框
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