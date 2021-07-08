from selenium.webdriver import ActionChains

from Common.base_page import BasePage, time
from PageLocators.locators_CheckSummaryReportData import LocatorsBusinessPlan as dp

main_window = ''
summaryDataDict = {}
class TestCheckData(BasePage):
    def navigateToSummaryPage(self):
        doc = '导航到Plan Summary页面'
        try:
            # 导航到Business Plan Summary页面
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe2))
            # 输入Country, Plan Cycle
            self.wait_eleVisible(dp.searchBtn_ele, 30)
            self.ac = ActionChains(self.driver)
            search = self.driver.find_element(*dp.searchBtn_ele)
            self.ac.move_to_element(search).perform()  # 悬浮于Search
            self.log.logger_info(doc+"成功")
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    def navigateToSummaryPage1(self):
        doc = '根据输入的Country, Plan Cycle search summary数据'
        try:
            self.driver.switch_to.default_content()
            self.ac = ActionChains(self.driver)
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe1))
            time.sleep(2)
            bpt0 = self.driver.find_element(*dp.ele_bpt)
            self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
            time.sleep(3)
            self.driver.find_element(*dp.menu_businessSummary).click()  # 点击country plan summary
            time.sleep(3)

            # 导航到Business Plan Summary页面
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe2))
            # 输入Country, Plan Cycle
            self.wait_eleVisible(dp.searchBtn_ele, 30)
            self.ac = ActionChains(self.driver)
            search = self.driver.find_element(*dp.searchBtn_ele)
            self.ac.move_to_element(search).perform()  # 悬浮于Search
            self.log.logger_info(doc + "成功")
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    def SearchData_SummaryPage_Tablet(self,data):
        self.data = data
        doc = '点击Plan Summary No'
        try:
            # 选择Region/Country
            self.wait_eleVisible(dp.country, wait_times=30, doc=doc)
            self.click_element(dp.country)
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[text()="{}"]'.format(data['Region/Country'])).click() # 选择Country值
            # 选择Plan Cycle
            time.sleep(3)
            self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="{}"]'.format(data['Plan Cycle'])).click()
            time.sleep(3)
            # 点击Search 按钮
            self.wait_eleVisible(dp.searchBtn_ele, wait_times=30, doc=doc)
            self.click_element(dp.searchBtn_ele)
            time.sleep(5)

            # 点击Plan Summary No
            self.wait_eleVisible(dp.planSummaryNo_ele2, wait_times=30, doc=doc)
            self.click_element(dp.planSummaryNo_ele2)
            self.log.logger_info(doc + "成功")
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # Summary页面Search数据
    def SearchData_SummaryPage(self,data):
        self.data = data
        doc = '点击Plan Summary NO'
        try:
            # 选择Region/Country
            self.wait_eleVisible(dp.country, wait_times=30, doc=doc)
            self.click_element(dp.country)
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[text()="{}"]'.format(data['Region/Country'])).click() # 选择Country值
            # 选择Plan Cycle
            time.sleep(3)
            self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="{}"]'.format(data['Plan Cycle'])).click()
            time.sleep(3)
            # 点击Search 按钮
            self.wait_eleVisible(dp.searchBtn_ele, wait_times=30, doc=doc)
            self.click_element(dp.searchBtn_ele)
            time.sleep(3)

            # 点击Plan Summary No
            self.wait_eleVisible(dp.planSummaryNo_ele, wait_times=30, doc=doc)
            self.click_element(dp.planSummaryNo_ele)
            self.log.logger_info(doc + "成功")
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise



    # 导航到Portfolio Plan页面
    def navigateToPortfolioPage(self):
        doc = '导航到Portfolio Plan页面'
        try:
            self.log.logger_info(doc)
            self.ac = ActionChains(self.driver)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe1))
            time.sleep(2)
            bpt0 = self.driver.find_element(*dp.ele_bpt)
            self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
            time.sleep(3)
            self.driver.find_element(*dp.menu_countryPlan).click()  # 点击menu_countryPlan
            time.sleep(3)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe2))
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # Portfolio Plan页面获取数据
    def get_OneProductGroup_portfolioData(self, TabletPlanNo):
        doc = '获取Portfolio Plan页面的数据'
        try:
            self.log.logger_info(doc)
            time.sleep(5)
            # 根据plan summary页面获取的portfolio No号 search数据
            self.input_text(dp.portfolioNo_input, TabletPlanNo)
            time.sleep(3)
            # 点击search的数据，查找数据
            self.click_element(dp.search_ele)
            time.sleep(5)
            # 点击Portfolio No进入Portfolio Item页面
            self.click_element(dp.portfolioNo1)
            time.sleep(20)
            # 在Portfolio Item页面，获取Total, Volume, Net BMC GP($)的值'
            self.wait_eleVisible(dp.portfolioItem, wait_times=120, doc=doc)
            TotalVolume = float(self.get_text(dp.totalVolume_ele).replace(',', ''))
            time.sleep(3)
            TotalNetBMCGP = float(self.get_text(dp.totalNetRevenue_ele).replace(',', ''))
            portfolioDataDict = {}
            portfolioDataDict['TotalVolume'] = TotalVolume  # 将lineCode放到字典里
            portfolioDataDict['TotalNetBMCGP'] = TotalNetBMCGP

            return portfolioDataDict

        except:
            self.log.logger_error(doc + "失败！！！")
        # 截图
        self.save_screenshot(doc)
        raise

    def navigateToPortfolioListCommentsPage(self):
        doc = '导航到PortfolioListComments页面，获取每个产品组对应的Portfolio No'
        try:
            # 进入Plan Summary Details页面，点击Portfolio & Approval Log
            time.sleep(5)
            # 切换窗口
            main_window = self.driver.current_window_handle
            self.wait_eleVisible(dp.portfolioApprovalLog_ele, wait_times=30, doc=doc)
            self.click_element(dp.portfolioApprovalLog_ele)

            # 切换到弹出窗口
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'PortfolioListCommentsPage' in self.driver.title:
                    break
            # 获取每个产品组对应的Portfolio No
            time.sleep(5)
            NBPlanNo = self.get_text(dp.NBPlan_ele).split( )
            # TDTPlanNo = self.get_text(dp.TDTPlan_ele)
            # TabletPlanNo = self.get_text(dp.TablePlan_ele)
            # OptionPlanNo = self.get_text(dp.OptionPlan_ele)
            print('---------',NBPlanNo)  # ['LU_20201210_036_TW_V0', 'LU_20201120_018_TW_V0', 'LU_20201120_016_TW_V0']

            for planNo in NBPlanNo:
                NBPlanNo[NBPlanNo.index(planNo)] = NBPlanNo
                planNo = planNo[0:planNo.rindex("_")]
                print('***********', planNo)
                summaryDataDict['planNo'] = planNo

            # TDTPlanNo = TDTPlanNo[0:TDTPlanNo.rindex("_")]
            # TabletPlanNo = TabletPlanNo[0:TabletPlanNo.rindex("_")]
            # OptionPlanNo = OptionPlanNo[0:OptionPlanNo.rindex("_")]
            self.driver.close()

            # TDTsummaryDataDict['TDTPlanNo'] = TDTPlanNo
            # TabletsummaryDataDict['TabletPlanNo'] = TabletPlanNo
            # OptionsummaryDataDict['OptionPlanNo'] = OptionPlanNo
            time.sleep(5)
            self.log.logger_info(doc + "成功")
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    def get_ProductGroup_summaryData(self, productGroup):
        doc = '获取每个产品组对应的数据'
        try:
            self.log.logger_info(doc)
            # 在Plan Summary Details页面，获取Financial Report tab下的每个产品组对应的数据
            self.driver.switch_to_window(main_window)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(*dp.ele_iframe2))
            # 获取Product Group对应的值
            CAs_ele= self.driver.find_element_by_xpath('//table[@id="tblProduct"]//tr[@id="{0}@{0}@Region Q Plan"]//td[2]'.format(productGroup))
            Net_BMC_GP_ele = self.driver.find_element_by_xpath('//table[@id="tblProduct"]//tr[@id="{0}@{0}@Region Q Plan"]//td[7]'.format(productGroup))
            print(CAs_ele.text, Net_BMC_GP_ele.text)
            CAs = float(CAs_ele.text).replace(',', '')
            Net_BMC_GP = float(Net_BMC_GP_ele.text).replace(',', '')

            print(CAs, Net_BMC_GP)

            summaryDataDict = {}['CAs'] = CAs  # 将CAs放到字典里
            summaryDataDict = {}['Net_BMC_GP'] = Net_BMC_GP

            # print(summaryDataDict)
            return summaryDataDict
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # Portfolio Plan页面获取数据
    def get_multiProductGroup_portfolioData(self,PlanNo):
        doc = 'Portfolio Plan页面获取多产品组数据'
        try:
            self.log.logger_info(doc)
            time.sleep(3)
            # 清空Potofolio No文本
            self.clear_element_text(dp.portfolioNo_input)
            # 根据plan summary页面获取的portfolio No号 search数据
            self.input_text(dp.portfolioNo_input, PlanNo)
            time.sleep(3)
            # 点击search的数据，查找数据
            self.click_element(dp.search_ele)
            time.sleep(5)
            # 点击Portfolio No进入Portfolio Item页面
            self.click_element(dp.portfolioNo1)
            time.sleep(20)
            # 在Portfolio Item页面，获取Total, Volume, Net BMC GP($)的值'
            self.wait_eleVisible(dp.portfolioItem, wait_times=60,doc=doc)
            TotalVolume = float(self.get_text(dp.totalVolume_ele).replace(',',''))
            time.sleep(3)
            TotalNetBMCGP = float(self.get_text(dp.totalNetRevenue_ele).replace(',',''))
            # print(PlanNo, TotalVolume, TotalNetBMCGP)

            # 点击Back按钮
            self.click_element(dp.backBtn_ele)
            time.sleep(3)

            portfolioDataDict = {}
            portfolioDataDict['TotalVolume'] = TotalVolume  # 将lineCode放到字典里
            portfolioDataDict['TotalNetBMCGP'] = TotalNetBMCGP


            return portfolioDataDict

        except:
            self.log.logger_error(doc + "失败！！！")
        # 截图
        self.save_screenshot(doc)
        raise


