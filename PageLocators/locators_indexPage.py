from selenium.webdriver.common.by import By

class LocatorsIndexPage:
    button_switch = (By.XPATH, '//i[@class="fa fa-filter"]//parent::a') #定位switch按钮
    # 悬浮框未展开，定位Home的图像
    img_Home = (By.XPATH, '//div[@class="sidebar-mini"]//i[@class="left-icon1"]')
    eles_MenuLeve1_SMB=(By.XPATH,'//a[@tagid="CBT_EMEA_Business_Plan"]')#定位一级菜单
    eles_MenuLeve1_CPM=(By.XPATH,'//li[@name="appcode_CPM"]//label')#定位CPM下的以及菜单
    eles_MenuLeve1_executePlan = (By.XPATH, '//a[@tagid="CBT_EMEA_Execution_Plan"]')  # 定义Consumer下的一级菜单
    # eles_MenuLeve1_SMB = (By.XPATH, '//li[@name="appcode_SMB"]//label')  # 定位SMB下的一级菜单
    # eles_MenuLeve1_CPM = (By.XPATH, '//li[@name="appcode_CPM"]//label')  # 定位CPM下的以及菜单
    eles_MenuLeve2_SMB=(By.XPATH,'//ul[@id="demo39"]//a')#定位二级菜单
    #定位iframe窗口元素
    ele_iframe=(By.XPATH,'//iframe[@id="ifsidebar"]')
    # 悬浮框展开后，定位businessPlan按钮
    button_businessPlan = (By.XPATH, '//ul[@id="accordion"]//i[@class="left-icon39"]')
    # 定位展开列表上的Country Portfolio & Plan按钮
    button_countryPortolioPlan = (By.XPATH, '//ul[@id="demo39"]//a[text()="Country Portfolio & Plan"]')
