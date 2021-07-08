from selenium.webdriver.common.by import By

class LocatorsPortfolioCheck:
    ele_iframe1 = (By.ID, 'ifsidebar')  # 定位iframe
    ele_bpt = (By.XPATH, '//a[text()="Business Plannning Tool"]')  # 定位bpt
    menu_businessPlan = (By.XPATH, '//a[@tagid="CBT_EMEA_Business_Plan"]')  #定位一级菜单business plan
    menu_countryPlan = (By.XPATH, '//a[text()="Country Portfolio & Plan"]') #定位二级菜单country plan
    ele_iframe2 = (By.ID, 'ifContent')  #切换二级iframe
    search = (By.XPATH, '//input[@id="ContentPlaceHolder1_BtnSearch"]')  #搜索按钮
    country=(By.XPATH, '//*[@id="spCountry"]/span/span/span')
    select_country = (By.XPATH, '//span[text()="Taiwan"]')
    select_productGroup = (
    By.XPATH, '//select[@id="ContentPlaceHolder1_ddlProductGroup"]//option[text()="Mobile Gaming"]')  # 选择Product Group
    select_planCycle = (
    By.XPATH, '//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY21/22Q1"]')  # 选择Plan Cycle
    table1=(By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[2]/td[1]')
    table2 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[3]/td[1]')
    table3 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[4]/td[1]')
    table4 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[5]/td[1]')
    table5 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[6]/td[1]')
    table6 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[7]/td[1]')
    table7 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[8]/td[1]')
    table8 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[9]/td[1]')
    table9 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[10]/td[1]')
    table10 = (By.XPATH, '//table[@class="table table-bordered text-center"]/tbody/tr[11]/td[1]')
    pc=(By.XPATH, '//a[@id="a_link2"]')
    Volume = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalVolume_PC"]')
    NetRevenue = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalNetRevenue_PC"]')
    NetBMCGP = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalNetBMCGP_PC"]')

    Volume1 = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalVolume"]')
    NetRevenue2 = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalNetRevenue"]')
    NetBMCGP3 = (By.XPATH, '//span[@id="ContentPlaceHolder2_lblTotalNetBMCGP"]')

    menu_track = (By.XPATH, '//a[@tagid="CBT_EMEA_Track_&_Measure"]')  # 定位一级菜单ww report
    menu_ww_report = (By.XPATH, '//a[text()="WW Report"]')  # 定位二级级菜单ww report

    country_ww = (By.XPATH, '//*[@id="spCountry"]/span/span/a')
    select_country_ww = (By.XPATH, '//span[text()="Taiwan"]')
    select_productGroup_ww = ( By.XPATH,'//*[@id="ContentPlaceHolder2_ddlProductGroup_img"]')  # 选择Product Group
    select_productGroup_ww1 = (By.XPATH,'//label[text()="Mobile Gaming"]')
    select_planCycle_ww = (By.XPATH, '//*[@id="ContentPlaceHolder2_ddl_Quarter_img"]')  # 选择Plan Cycle
    select_planCycle_ww1 = (By.XPATH, '//label[text()="FY21/22Q1"]')
    select_planCycle_ww2 = (By.XPATH, '//label[text()="FY20/21Q4"]')

    select_planType_ww= (By.XPATH, '//select[@id="ContentPlaceHolder2_ddl_PlanType"]//option[text()="Business Plan"]')
    select_portfolioType_ww = (By.XPATH, '//select[@id="ContentPlaceHolder2_ddlPortfolioType"]//option[text()="To be Approved"]')
    select_version_ww = (By.XPATH, '//select[@id="ContentPlaceHolder2_ddlVersion"]//option[text()="All"]')
    refresh_ww=( By.XPATH, '//input[@id="ContentPlaceHolder2_btnRefresh"]')
    download_ww = (By.XPATH, '//input[@id="ContentPlaceHolder2_btnDownload"]')
    downloads_ww = (By.XPATH, '//button[@class="confirm"]')
    download_tab_ww=(By.XPATH, '//a[text()="Download Report"]')
    download_tab_table = (By.XPATH, '//*[@id="tabFinancial"]/tbody/tr[1]/td[8]')
    download_tab_table1 = (By.XPATH, '//*[@id="tabFinancial"]/tbody/tr[1]/td[9]/a')

    select_page_ww = (By.XPATH, '//select[@id="ContentPlaceHolder2_ddlPageSize"]//option[text()="20"]')
    select_page_ww1= (By.XPATH, '//select[@id="ContentPlaceHolder2_ddlPageSize"]//option[text()="10"]')




