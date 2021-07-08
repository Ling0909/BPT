from selenium.webdriver.common.by import By
class LocatorsFundingManagementPage:
    ele_iframe = (By.XPATH, '//iframe[@id="ifContent"]')  # 定位iframe
    ele_iframe_upload=(By.XPATH,'//iframe[contains(@name,"OpenartDialog")]')#定位数据导入成功后，
    select_policyType = (By.XPATH, '//label[text()="Policy Type"]/..//select[@id="type"]')  # 定位policyType筛选框
    button_search = (By.XPATH, '//button[text()="Search"]')  # 定位search按钮
    # 定位加载好数据后，第一条数据的policy值
    load_ok=(By.XPATH, '//div[@id="borderBox"]//tbody[@id="search-tbody"][1]//td[1]')
    # 定位第一个界面的DownloadPolicyTemplate按钮
    button_downLoad=(By.XPATH, '//button[text()="DownloadPolicyTemplate"]')

    #定位PleaseChoose按钮
    input_upLoadFile=(By.ID,'uploadfile')
    # 定位Upload按钮
    button_upLoad=(By.XPATH,'//button[text()="Upload"]')
    button_close_in_iframe=(By.XPATH,'//button[text()="Close"]')