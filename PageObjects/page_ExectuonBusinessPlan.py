from Common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from PageLocators.locators_ExecutionBusinessPlan import ELocatorsExecutionBusinessPlan as lb
from selenium.webdriver.common.keys import Keys
import time

main_window=''
class ExectuonPageBusinessPlan(BasePage):
    def create_businessPlan(self):
        self.ac = ActionChains(self.driver)
        self.driver.switch_to_frame('ifsidebar')
        bpt = self.driver.find_element_by_xpath('//a[text()="Business Plannning Tool"]')
        self.ac.move_to_element(bpt).perform()  # 悬浮于BPT
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@tagid="CBT_EMEA_Execution_Plan"]').click()  # 点击business plan
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[text()="Exec Portfolio & Plan"]').click()  # 点击country plan
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.switch_iframe(self.driver.find_element(*lb.ele_iframe2),'ele_iframe2')
        time.sleep(2)
        self.driver.find_element(*lb.button_createPortfolio).click()  # 点击创建portfolio
        time.sleep(5)
        ej = self.driver.find_element(*lb.ele_iframe3)
        self.driver.switch_to.frame(ej)
        # 填写弹框信息
        self.driver.find_element(*lb.select_countryGroup).click()  # 选择country group
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(self.data['CountryGroup'])).click()  # 填入国家
        self.driver.find_element_by_xpath(
            '//select[@id="ContentPlaceHolder1_ddl_ProductGroup"]//option[text()="{}"]'.format(
                self.data['ProductGroup'])).click()  # 选择Product Group
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddl_Quarter"]//option[text()="{}"]'.format(
            self.data['PlanCycle'])).click()  # 选择Plan Cycle
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlchannelretail"]//option[text()="{}"]'.format(self.data['PortfolioType'])).click()  # 选择Portfolio Type
        self.driver.find_element(*lb.ele_portfolioName).click()
        time.sleep(2)
        self.driver.find_element(*lb.ele_portfolioName).send_keys(self.data['PortfolioName'])  # 填写Portfolio
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.button_next).click()  # 点击下一步
        time.sleep(10)
    def create_businessPlanMtm(self):
        # 选择MTM弹窗item
        main_window = self.driver.current_window_handle
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
        # 选择item
        self.driver.find_element(*lb.ele_mtmItem).click()
        # 保存并关闭弹窗
        self.driver.find_element(*lb.button_mtmSaveClose).click()
        time.sleep(15)

    def edit_portfolioItem(self):
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        # item前面复选框
        self.driver.find_elements(*lb.check_item).pop(0).click()
        # 进入编辑页面
        self.driver.find_element(*lb.button_mtmEdit).click()
        time.sleep(20)
        # 切换到编辑item弹出窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'Add' in self.driver.title:
                break
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe5))
        self.driver.execute_script('window.scrollTo(0, 1000)')
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
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0, 400)')
        time.sleep(3)
        self.driver.find_element(*lb.buying_price1).send_keys('2')
        time.sleep(1)
        self.driver.find_element(*lb.buying_price2).click()
        time.sleep(1)
        self.driver.find_element(*lb.buying_auto).click()
        time.sleep(1)
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
        time.sleep(10)
        # 点击保存并关闭按钮
        self.driver.find_element(*lb.sa).click()

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
        time.sleep(2)
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
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export2))  # 进入打开的弹窗界面的iframe
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
        pn = 'PAG50051TW'
        self.write_excel(file_new2, "MTM PN List", 2, 1, pn)
        time.sleep(10)
        # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.tuploadmtm).send_keys(file_new2)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.tright_uploadmtm).click()
        time.sleep(10)
        self.driver.switch_to.alert.accept()  # 确认
        time.sleep(25)

        # Copy Portfolio Item
    def copy_portfolioItem(self):
            doc = 'Copy Portfolio Item'
            time.sleep(8)
            self.driver.switch_to.window(main_window)
            self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
            # 选择一条Item数据
            self.driver.find_element(*lb.firstItem_checkbox).click()
            self.click_element(lb.copyItem_btn)  # 点击copy按钮

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

        # Delete Portfolio Item
    def delete_portfolioItem(self):
            doc = 'Delete Portfolio Item'
            time.sleep(8)
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
        self.bc = ActionChains(self.driver)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        time.sleep(5)
        download_download = self.driver.find_element(*lb.dowload_button)
        self.bc.move_to_element(download_download).perform()
        self.driver.find_element(*lb.dowload_button1).click()
        time.sleep(10)

        # 上传
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_dowload_button).click()
        self.driver.find_element(*lb.upload_button).click()
        time.sleep(1)

        file_new = self.get_latest_fileName()
        time.sleep(5)
        self.write_excel(file_new, "Portfolio", 14, 178, 999)
        time.sleep(3)
        self.write_excel(file_new, "Portfolio", 14, 210, 999)
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe_export1))  # 进入打开的弹窗界面的iframe
        # 选择本地Excel文件，并上传
        self.driver.find_element(*lb.input_File_Upload).send_keys(file_new)  # 点击选择文件按钮
        time.sleep(10)
        self.driver.find_element(*lb.upload_button_tankuang).click()
        time.sleep(10)
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.upload_button_refresh).click()
        time.sleep(10)


