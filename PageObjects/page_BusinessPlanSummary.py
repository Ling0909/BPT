from Common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from PageLocators.locators_BusinessPlanSummary import LocatorsBusinessPlanv as lb
import time



main_window=''
class PageBusinessPlanSummary(BasePage):

    def create_businessPlanSummy(self,data):
        self.data = data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_businessPlan).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.find_element(*lb.menu_businessSummary).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_portfolioSummaryCreate).click()  # 点击创建portfolio summary
        time.sleep(2)
        ej1 = self.driver.find_element(*lb.ele_iframe4)
        self.driver.switch_to.frame(ej1)
        # 填写弹框信息
        self.driver.find_element(*lb.select_summaryCountryGroup).click()  # 选择country group
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  # allure generate
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element(*lb.select_summaryProductGroup).click()  # 选择Product Group
        self.driver.find_element(*lb.select_summarySave).click()  # 点击保存
        time.sleep(20)
        self.driver.switch_to.alert.accept()#确认
        time.sleep(5)
        #点击plan summary提交按钮
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_summarySave).click()
        time.sleep(5)
        main_window = self.driver.current_window_handle
        #在弹窗中点击submit按钮
        self.driver.switch_to.default_content()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Submit' in self.driver.title:
                break
        #弹框提交按钮
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(*lb.button_summarySave1).click()
        time.sleep(10)
    def create_businessPlanSummy1(self,data):
        self.data = data
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        time.sleep(2)
        bpt0 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_businessSummary).click()  # 点击country plan summary
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_portfolioSummaryCreate).click()  # 点击创建portfolio summary
        time.sleep(2)
        ej1 = self.driver.find_element(*lb.ele_iframe4)
        self.driver.switch_to.frame(ej1)
        # 填写弹框信息
        self.driver.find_element(*lb.select_summaryCountryGroup).click()  # 选择country group
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  # allure generate
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="{}"]'.format(self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element(*lb.select_summaryProductGroup).click()  # 选择Product Group
        self.driver.find_element(*lb.select_summarySave).click()  # 点击保存
        time.sleep(20)
        self.driver.switch_to.alert.accept()#确认
        time.sleep(5)
        #点击plan summary提交按钮
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_summarySave).click()
        time.sleep(5)
        main_window = self.driver.current_window_handle
        #在弹窗中点击submit按钮
        self.driver.switch_to.default_content()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Submit' in self.driver.title:
                break
        #弹框提交按钮
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(*lb.button_summarySave1).click()
        time.sleep(10)


    def businessPlanSummyApprove(self):
        #进入审批页面
        self.driver.switch_to.window(main_window)
        time.sleep(10)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        bpt4 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt4).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_submtiCountryPlan).click()  # 点击country plan summary
        time.sleep(6)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(2)
        self.driver.find_element(*lb.button_approvesearch).click()  # 点击search按钮
        time.sleep(5)
        self.driver.find_element(*lb.ele_table).click()  #进入详情页
        time.sleep(5)
        self.driver.find_element(*lb.button_reject).click()  # 进入详情页
        time.sleep(3)
        self.driver.switch_to.default_content()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Regject' in self.driver.title:
                break
        # 弹框提交按钮
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(*lb.buttonreject_approvesearch).click()
        time.sleep(7)
        self.driver.switch_to.alert.accept()#确认
        self.driver.switch_to.window(main_window)
        time.sleep(10)

    def delete_businessPlanSummy(self):
        #删除summary
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        bpt3 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt3).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_businessSummary).click()  # 点击country plan summary
        time.sleep(10)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(2)
        self.driver.find_element(*lb.button_approvesearch1).click()  # 点击search按钮
        time.sleep(5)
        self.driver.find_element(*lb.select_summaryCountryGroup1).click()
        time.sleep(1)
        self.driver.find_element(*lb.ele_summaryCountry1).click() #国家
        time.sleep(1)
        self.driver.find_element(*lb.select_summaryPlanCycle1).click()  #Plan Cycle
        time.sleep(1)
        self.driver.find_element(*lb.button_apps1).click()  # 点击search按钮
        time.sleep(5)
        self.driver.find_element(*lb.ele_tabledelete1).click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(5)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(8)

    def search_businessPlan(self):
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        bpt3 = self.driver.find_element(*lb.ele_bpt)
        self.ac.move_to_element(bpt3).perform()  # 悬浮于BPT
        time.sleep(2)
        self.driver.find_element(*lb.menu_countryPlan).click()  # 点击country plan summary
        time.sleep(10)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(2)
        self.driver.find_element(*lb.button_approvesearch2).click()  # 点击search按钮
        time.sleep(5)
        self.driver.find_element(*lb.select_summaryCountryGroup2).click()
        time.sleep(1)
        self.driver.find_element(*lb.ele_summaryCountry2).click()  # 国家
        time.sleep(1)
        self.driver.find_element(*lb.select_summaryPlanCycle2).click()  # Plan Cycle
        time.sleep(1)
        self.driver.find_element(*lb.button_apps2).click()  # 点击search按钮
        time.sleep(10)




