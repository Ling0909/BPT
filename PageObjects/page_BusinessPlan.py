from selenium.webdriver.common.keys import Keys

from Common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from PageLocators.locators_BusinessPlan import LocatorsBusinessPlan as lb
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


main_window=''
class PageBusinessPlan(BasePage):


    def create_businessPlan(self,data):
        self.data=data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_businessPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.find_element(*lb.menu_countryPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2), 'ele_iframe2')
        time.sleep(2)
        self.driver.find_element(*lb.button_createPortfolio).click()  # 点击创建portfolio
        time.sleep(5)
        ej = self.driver.find_element(*lb.ele_iframe3)
        self.driver.switch_to.frame(ej)
        # 填写弹框信息
        self.driver.find_element(*lb.select_countryGroup).click()  # 选择country group
        time.sleep(2)

        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  #填入国家
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddl_ProductGroup"]//option[text()="{}"]'.format(self.data['ProductGroup'])).click()  # 选择Product Group
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddl_Quarter"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="{}"]'.format(self.data['PortfolioType'])).click()  # 选择Portfolio Type
        self.driver.find_element(*lb.ele_portfolioName).click()
        time.sleep(2)
        self.driver.find_element(*lb.ele_portfolioName).send_keys(self.data['PortfolioName'])  # 填写Portfolio
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_next).click()  # 点击下一步
        time.sleep(15)
    def create_businessPlan1(self,data):
        self.data=data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_countryPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2), 'ele_iframe2')
        time.sleep(2)
        self.driver.find_element(*lb.button_createPortfolio).click()  # 点击创建portfolio
        time.sleep(5)
        ej = self.driver.find_element(*lb.ele_iframe3)
        self.driver.switch_to.frame(ej)
        # 填写弹框信息
        self.driver.find_element(*lb.select_countryGroup).click()  # 选择country group
        time.sleep(2)

        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  #填入国家
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddl_ProductGroup"]//option[text()="{}"]'.format(self.data['ProductGroup'])).click()  # 选择Product Group
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddl_Quarter"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="{}"]'.format(self.data['PortfolioType'])).click()  # 选择Portfolio Type
        self.driver.find_element(*lb.ele_portfolioName).click()
        time.sleep(2)
        self.driver.find_element(*lb.ele_portfolioName).send_keys(self.data['PortfolioName'])  # 填写Portfolio
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_next).click()  # 点击下一步
        time.sleep(15)
    def create_businessPlan_UnitedStates_ofAmerica_NB(self,data):
        self.data=data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_businessPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.find_element(*lb.menu_countryPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2), 'ele_iframe2')
        time.sleep(2)
        self.driver.find_element(*lb.button_createPortfolio).click()  # 点击创建portfolio
        time.sleep(5)
        ej = self.driver.find_element(*lb.ele_iframe3)
        self.driver.switch_to.frame(ej)
        # 填写弹框信息
        self.driver.find_element(*lb.select_countryGroup).click()  # 选择country group
        time.sleep(2)

        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  #填入国家
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-id="ContentPlaceHolder1_ddlCustomer"]').click()
        time.sleep(3)#选择customer
        self.driver.find_element_by_xpath('//*[@id="div_Customer"]/div/div/div/ul/li[1]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-id="ContentPlaceHolder1_ddlCustomer"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlCampaign"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="{}"]'.format(self.data['PortfolioType'])).click()  # 选择Portfolio Type
        time.sleep(3)
        self.driver.find_element(*lb.ele_portfolioName).click()
        time.sleep(2)
        self.driver.find_element(*lb.ele_portfolioName).send_keys(self.data['PortfolioName'])  # 填写Portfolio
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_next).click()  # 点击下一步
        time.sleep(15)
    def create_businessPlan_UnitedStates_ofAmerica_NB1(self,data):
        self.data=data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_countryPlan).click()  # 点击country plan summary
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2), 'ele_iframe2')
        time.sleep(2)
        self.driver.find_element(*lb.button_createPortfolio).click()  # 点击创建portfolio
        time.sleep(5)
        ej = self.driver.find_element(*lb.ele_iframe3)
        self.driver.switch_to.frame(ej)
        # 填写弹框信息
        self.driver.find_element(*lb.select_countryGroup).click()  # 选择country group
        time.sleep(2)

        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  #填入国家
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-id="ContentPlaceHolder1_ddlCustomer"]').click()
        time.sleep(3)#选择customer
        self.driver.find_element_by_xpath('//*[@id="div_Customer"]/div/div/div/ul/li[1]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-id="ContentPlaceHolder1_ddlCustomer"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlCampaign"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="{}"]'.format(self.data['PortfolioType'])).click()  # 选择Portfolio Type
        time.sleep(3)
        self.driver.find_element(*lb.ele_portfolioName).click()
        time.sleep(2)
        self.driver.find_element(*lb.ele_portfolioName).send_keys(self.data['PortfolioName'])  # 填写Portfolio
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_next).click()  # 点击下一步
        time.sleep(15)

    def create_businessPlanMtm(self,data):
        self.data=data
        # 选择MTM弹窗item
        main_window = self.driver.current_window_handle
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_mtm).click()
        time.sleep(10)
        # 切换到弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'MTM' in self.driver.title:
                break
        # 点击搜索指定pn（PAG50049TW）
        self.driver.find_element(*lb.button_mtmSearch).click()
        time.sleep(15)
        self.driver.find_element_by_id('ContentPlaceHolder1_txtPN').click()
        time.sleep(1)
        self.driver.find_element_by_id('ContentPlaceHolder1_txtPN').send_keys(self.data['PN'])
        time.sleep(1)
        self.driver.find_element(*lb.button_mtmSearch).click()
        time.sleep(15)
        # 选择item
        self.driver.find_element(*lb.ele_mtmItem).click()
        # 保存并关闭弹窗
        self.driver.find_element(*lb.button_mtmSaveClose).click()
        time.sleep(20)
    def create_businessPlanMtm_american(self,data):
        self.data=data
        # 选择MTM弹窗item
        main_window = self.driver.current_window_handle
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_mtm).click()
        time.sleep(10)
        # 切换到弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'MTM' in self.driver.title:
                break
        # 点击搜索指定pn（PAG50049TW）
        self.driver.find_element(*lb.button_mtmSearch1).click()
        time.sleep(15)
        self.driver.find_element_by_id('ContentPlaceHolder1_txtPN').click()
        time.sleep(1)
        self.driver.find_element_by_id('ContentPlaceHolder1_txtPN').send_keys(self.data['PN'])
        time.sleep(1)
        self.driver.find_element(*lb.button_mtmSearch1).click()
        time.sleep(20)
        # 选择item
        self.driver.find_element(*lb.ele_mtmItem).click()
        # 保存并关闭弹窗
        self.driver.find_element(*lb.button_mtmSaveClose).click()
        time.sleep(20)

    #調試時使用
    def selectPortfolioNo(self):
        self.ac = ActionChains(self.driver)
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2), 'ele_iframe2')
        search_btn = self.driver.find_element(*lb.search_btn)
        self.ac.move_to_element(search_btn).perform()
        time.sleep(1)
        #选择一条portfolioNO并点击
        self.driver.find_element_by_xpath('//a[text()="LU_20210310_004_TW"]').click()


    def edit_portfolioItem(self):
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(5)
        self.driver.find_elements(*lb.check_item).pop(0).click()
        time.sleep(5)
        # 进入编辑页面
        self.driver.find_element(*lb.button_mtmEdit).click()
        time.sleep(20)
        # 切换到编辑item弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Add' in self.driver.title:
                break
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe5))

        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txtDistributorBuyingPriceUSD0'))
        time.sleep(3)
        self.driver.find_element(*lb.carrying_case).click()
        time.sleep(1)
        self.driver.find_element(*lb.carrying_case).send_keys('100')
        time.sleep(1)
        self.driver.find_element(*lb.distributor_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.distributor_ele).send_keys('90')
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).send_keys('80')
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).send_keys('5')
        time.sleep(1)
        self.driver.find_element(*lb.volume2_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume2_auto).click()
        time.sleep(3)
        self.driver.find_element(*lb.buying_price1).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price1).send_keys('2')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_auto).click()
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txttrWWFunding_0'))
        time.sleep(3)
        self.driver.find_element(*lb.retail_rebates).click()
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates).send_keys('100')
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates2).click()
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates2).send_keys('5')
        time.sleep(1)
        # 点击计算按钮
        self.driver.find_element(*lb.calc).click()
        time.sleep(15)
        # 点击保存并关闭按钮
        self.driver.find_element(*lb.sa).click()
        time.sleep(10)
    def edit_portfolioItem_Germany(self):
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(5)
        self.driver.find_elements(*lb.check_item).pop(0).click()
        time.sleep(5)
        # 进入编辑页面
        self.driver.find_element(*lb.button_mtmEdit).click()
        time.sleep(20)
        # 切换到编辑item弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Add' in self.driver.title:
                break
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe5))

        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txtDistributorBuyingPriceUSD0'))
        time.sleep(3)
        self.driver.find_element(*lb.distributor_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.distributor_ele).send_keys('90')
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).send_keys('80')
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).send_keys('4')
        time.sleep(1)
        self.driver.find_element(*lb.volume2_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume2_ele).send_keys('5')
        time.sleep(3)
        self.driver.find_element(*lb.volume3_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume3_ele).send_keys('6')
        time.sleep(3)
        self.driver.find_element(*lb.buying_price1).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price1).send_keys('7')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).send_keys('8')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price3).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price3).send_keys('9')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txttrWWFunding_0'))
        time.sleep(3)
        self.driver.find_element(*lb.retail_rebates).click()
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates).send_keys('100')
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates2).click()
        time.sleep(1)
        self.driver.find_element(*lb.retail_rebates2).send_keys('5')
        time.sleep(1)
        # 点击计算按钮
        self.driver.find_element(*lb.calc).click()
        time.sleep(15)
        # 点击保存并关闭按钮
        self.driver.find_element(*lb.sa).click()
        time.sleep(10)
    def edit_portfolioItem_UnitedStates_ofAmerica_NB(self):
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(5)
        self.driver.find_elements(*lb.check_item).pop(0).click()
        time.sleep(5)
        # 进入编辑页面
        self.driver.find_element(*lb.button_mtmEdit).click()
        time.sleep(20)
        # 切换到编辑item弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Add' in self.driver.title:
                break
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe5))

        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txtDistributorBuyingPriceUSD0'))
        time.sleep(3)
        self.driver.find_element(*lb.distributor_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.distributor_ele).send_keys('90')
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.reseller_ele).send_keys('80')
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume1_ele).send_keys('1')
        time.sleep(1)
        self.driver.find_element(*lb.volume2_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume2_ele).send_keys('2')
        time.sleep(3)
        self.driver.find_element(*lb.volume3_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume3_ele).send_keys('3')
        time.sleep(3)
        self.driver.find_element(*lb.volume4_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume4_ele).send_keys('4')
        time.sleep(1)
        self.driver.find_element(*lb.volume5_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume5_ele).send_keys('5')
        time.sleep(3)
        self.driver.find_element(*lb.volume6_ele).click()
        time.sleep(1)
        self.driver.find_element(*lb.volume6_ele).send_keys('6')
        time.sleep(3)
        self.driver.find_element(*lb.buying_price1).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price1).send_keys('6')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).send_keys('5')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price3).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price3).send_keys('4')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price4).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price4).send_keys('3')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price5).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price5).send_keys('2')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price6).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_price6).send_keys('1')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",self.driver.find_element_by_id('ContentPlaceHolder2_txttrWWFunding_0'))
        time.sleep(3)
        self.driver.find_element(*lb.american1).click()
        time.sleep(1)
        self.driver.find_element(*lb.american1).send_keys('100')
        time.sleep(1)
        self.driver.find_element(*lb.american2).click()
        time.sleep(1)
        self.driver.find_element(*lb.american2).send_keys('100')
        time.sleep(1)
        self.driver.find_element(*lb.american3).click()
        time.sleep(1)
        self.driver.find_element(*lb.american3).send_keys('50')
        time.sleep(1)
        self.driver.find_element(*lb.american4).click()
        time.sleep(1)
        self.driver.find_element(*lb.american4).send_keys('10')
        time.sleep(1)
        self.driver.find_element(*lb.american5).click()
        time.sleep(1)
        self.driver.find_element(*lb.american5).send_keys('11')
        time.sleep(1)
        self.driver.find_element(*lb.american6).click()
        time.sleep(1)
        self.driver.find_element(*lb.american6).send_keys('12')
        time.sleep(1)
        # 点击计算按钮
        self.driver.find_element(*lb.calc).click()
        time.sleep(15)
        # 点击保存并关闭按钮
        self.driver.find_element(*lb.sa).click()
        time.sleep(10)

    # 下载customer模板上传customer模板
    def customer(self):
        # 下载
        self.ac = ActionChains(self.driver)
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(8)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        # item前面复选框
        self.driver.find_elements(*lb.check_item).pop(0).click()
        time.sleep(5)
        self.driver.find_element(*lb.downloadaddcustomer).click()
        time.sleep(8)

        # 上传
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.uploadcustomer).click()
        time.sleep(1)

        file_new1 = self.get_latest_fileName()
        time.sleep(5)
        self.write_excel(file_new1, "AddCustomer", 2, 5, 1215856839)
        time.sleep(3)
        self.write_excel(file_new1, "AddCustomer", 2, 7, 1213565968)
        time.sleep(3)
        self.write_excel(file_new1, "AddCustomer", 2, 10, 1)
        time.sleep(3)
        self.write_excel(file_new1, "AddCustomer", 2, 11, 2)
        time.sleep(3)
        self.write_excel(file_new1, "AddCustomer", 2, 12, 3)
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export2 ))  # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.tuploadcustomer).send_keys(file_new1)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.tright_uploadcustomer).click()
        time.sleep(10)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(25)

    # 下载或上传mtm
    def volume_mtm(self):
        # 下载
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.window(main_window)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.volume1_addmtm).click()
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export3))
        time.sleep(3)
        self.driver.find_element(*lb.downloadaddmtm).click()
        time.sleep(10)


        file_new2 = self.get_latest_fileName()
        time.sleep(5)
        pn='PAG50051TW'
        self.write_excel(file_new2, "MTM PN List", 2, 1,pn)
        time.sleep(10)
       # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.tuploadmtm).send_keys(file_new2)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.tright_uploadmtm).click()
        time.sleep(10)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(25)
    def volume_mtm1(self):
        # 下载
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.window(main_window)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.volume1_addmtm).click()
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export3))
        time.sleep(3)
        self.driver.find_element(*lb.downloadaddmtm).click()
        time.sleep(10)


        file_new2 = self.get_latest_fileName()
        time.sleep(5)
        pn='PAG50051TW'
        self.write_excel(file_new2, "MTM PN List", 2, 1,pn)
        time.sleep(10)
        self.write_excel(file_new2, "MTM PN List", 2, 2,pn)
        time.sleep(10)
       # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.tuploadmtm).send_keys(file_new2)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.tright_uploadmtm).click()
        time.sleep(10)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(25)


    #Copy Portfolio Item
    def copy_portfolioItem(self):
        doc = 'Copy Portfolio Item'
        time.sleep(8)
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        # 选择一条Item数据
        self.driver.find_element(*lb.firstItem_checkbox).click()
        self.click_element(lb.copyItem_btn)
        time.sleep(10)#点击copy按钮

    def showlog_Item(self):
        doc = 'Portfolio Item Log'
        time.sleep(10)
        # 选择一条Item数据
        self.driver.find_element(*lb.firstItem_checkbox).click()

        self.click_element(lb.logItem_btn)  # 点击log按钮
        time.sleep(3)
        # 切换到编辑item弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'PortfolioItemLog' in self.driver.title:
                break
        self.driver.close()
        time.sleep(10)

    # Delete Portfolio Item
    def delete_portfolioItem(self):
        doc = 'Delete Portfolio Item'
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(1)
        self.click_element(lb.deleteItem_btn)  # 点击delete按钮
        time.sleep(5)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(5)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(5)

    def uploadDownload_Item(self):
        # 下载及上传volume***********************************************************************
        # 下载
        self.ac = ActionChains(self.driver)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        time.sleep(5)
        download_download = self.driver.find_element(*lb.dowload_button)
        self.ac.move_to_element(download_download).perform()
        self.driver.find_element(*lb.dowload_button1).click()
        time.sleep(10)

        #上传
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        self.driver.find_element(*lb.upload_button).click()
        time.sleep(1)

        file_new=self.get_latest_fileName()
        time.sleep(5)
        self.write_excel(file_new,"Portfolio", 14, 178, 999)
        time.sleep(3)
        self.write_excel(file_new, "Portfolio", 14, 210, 999)
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export1))  # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.input_File_Upload).send_keys(file_new)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.upload_button_tankuang).click()
        time.sleep(10)

    def uploadDownload_Item1(self):
        # 下载及上传volume***********************************************************************
        # 下载
        self.ac = ActionChains(self.driver)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        time.sleep(5)
        download_download = self.driver.find_element(*lb.dowload_button)
        self.ac.move_to_element(download_download).perform()
        self.driver.find_element(*lb.dowload_button1).click()
        time.sleep(10)

        # 上传
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        self.driver.find_element(*lb.upload_button).click()
        time.sleep(1)

        file_new = self.get_latest_fileName()
        # time.sleep(5)
        # self.write_excel(file_new, "Portfolio", 14, 178, 999)
        # time.sleep(3)
        # self.write_excel(file_new, "Portfolio", 14, 210, 999)
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export1))  # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.input_File_Upload).send_keys(file_new)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.upload_button_tankuang).click()
        time.sleep(20)











