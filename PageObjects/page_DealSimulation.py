import time

from selenium.webdriver import ActionChains

from Common.base_page import BasePage
from PageLocators.locators_DealSimulation import locatorsDealSimulator as ds

main_window =''
class PageDealSimulation(BasePage):
    '''
        导航到Deal Simulation页面
    '''
    #創建Deal plan
    def Create_DealPlan(self,data):
        self.data=data
        try:
            doc = 'Deal Simulation--> 创建Deal Plan'
            # self.ac = ActionChains(self.driver)
            # self.driver.switch_to_frame('ifsidebar')
            # bpt = self.driver.find_element_by_xpath('//a[text()="Business Plannning Tool"]')
            # self.ac.move_to_element(bpt).perform()  # 悬浮于BPT
            # time.sleep(5)
            # self.driver.find_element_by_xpath('//a[@tagid="CBT_EMEA_Execution_Plan"]').click()
            # time.sleep(3)
            # self.driver.find_element_by_xpath('//a[text()="Deal Simulation"]').click()
            # time.sleep(2)
            # self.driver.switch_to_default_content()
            self.driver.switch_to.frame(self.driver.find_element(*ds.ele_iframe2))
            self.wait_eleVisible(ds.btnCreateDeal, wait_times=10, doc=doc)
            self.click_element(ds.btnCreateDeal)  # 点击创建deal按钮
            self.switch_iframe(self.get_element(ds.ele_iframe3), doc)  # 切换创建Create Deal弹框iframe

            self.click_element(ds.select_DC_ele)  # 选择DC值
            time.sleep(2)
            self.driver.find_element_by_xpath('//select[@id="ddlRetailCountry"]//option[text()="{}"]'.format(data['CountryGroup'])).click()  # 选择Country值
            time.sleep(2)
            self.wait_eleVisible(ds.customer_ele, wait_times=30, doc=doc)
            self.click_element(ds.customer_ele)  # 选择/输入Customer
            time.sleep(6)
            self.wait_eleVisible(ds.customer_select, wait_times=50, doc=doc)
            self.click_element(ds.customer_select)  # 选择Customer
            time.sleep(1)
            self.driver.switch_to_default_content()
            self.switch_iframe(self.get_element(ds.ele_iframe2), doc)
            self.click_element(ds.btn_next_ele)  # 点击Next按钮
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    def clickSelectFromMTM(self):
        try:
            doc = 'Deal Simulation--> 上传MTM'
            # 点击Select From MTM
            main_window = self.driver.current_window_handle
            self.wait_eleVisible(ds.mtm_btn_ele, wait_times=30, doc=doc)
            self.click_element(ds.mtm_btn_ele)

            # 切换到弹出窗口
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'MTM' in self.driver.title:
                    break
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    def inputPNValue(self,data):
        try:
            doc = 'Deal Simulation--> 输入PN'
            # 輸入指定PN: PAG50060GA
            #self.input_text(ds.input_pn_ele, 'PAG50060GA', doc)
            self.wait_eleVisible(ds.input_pn_ele, wait_times=30, doc=doc)
            time.sleep(5)
            self.clear_element_text(ds.input_pn_ele,doc)
            time.sleep(2)
            self.input_text(ds.input_pn_ele, data['PN'], doc)
            # self.driver.find_element(*ds.input_pn_ele).send_keys(data['PN'])
            time.sleep(3)
            # 点击Search按钮
            self.wait_eleVisible(ds.search_btn, wait_times=60, doc=doc)
            self.click_element(ds.search_btn)
            time.sleep(10)
            self.wait_eleVisible(ds.mtmItem_ele, wait_times=30, doc=doc)
            # 选择item
            time.sleep(1)
            self.click_element(ds.mtmItem_ele)
            time.sleep(2)
            # 点击Save and Next按钮
            self.click_element(ds.saveAndNext_btn)
            time.sleep(15)  # save后会自动刷新页面，需要添加等待时间
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    def closeMTMWindow(self):
        try:
            doc = "关闭MTM窗口"
            self.driver.close()
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 调试时使用
    # def selectDealNo(self):
    #     self.driver.switch_to_default_content()
    #     self.switch_iframe(self.get_element(ds.ele_iframe2), 'ele_iframe2')
    #     self.ac = ActionChains(self.driver)
    #     search_btn2 = self.driver.find_element(*ds.search_btn2)
    #     self.ac.move_to_element(search_btn2).perform()
    #     time.sleep(1)
    #     # 选择一条DealNO并点击
    #     self.driver.find_element_by_xpath('//a[text()="LU_20210322_017_GB"]').click()

    #编辑Item
    def Edit_DealItem(self):
        try:
            doc = 'Deal Simulation--> 编辑Deal Item'
            time.sleep(20)  # 页面会自动刷新，需要添加等待时间
            self.driver.switch_to.window(main_window)
            self.driver.switch_to.frame(self.driver.find_element(*ds.ele_iframe2))
            self.wait_eleVisible(ds.view_ele, wait_times=30, doc=doc)
            # 选择一条Item数据
            self.driver.find_element(*ds.firstItem_checkbox).click()
            self.click_element(ds.mtmEdit_btn)  # 编辑Item
            time.sleep(8)
            # 切换到编辑item弹出窗口
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'AddNewLineForWW' in self.driver.title:
                    break

            self.driver.execute_script('window.scrollTo(0, 500)')
            time.sleep(5)
            # 输入Volume值
            self.wait_eleVisible(ds.input_volumeCount_ele, wait_times=10, doc=doc)
            self.clear_element_text(ds.input_volumeCount_ele, doc)
            time.sleep(3)
            self.input_text(ds.input_volumeCount_ele, '100')

            # 输入streetPrice值
            time.sleep(1)
            self.wait_eleVisible(ds.input_streetPrice_ele, wait_times=10, doc=doc)
            self.clear_element_text(ds.input_streetPrice_ele, doc)
            self.input_text(ds.input_streetPrice_ele, '10000')

            # 选择MOT的值
            self.driver.execute_script('window.scrollTo(0, 500)')
            time.sleep(1)
            self.driver.find_element(*ds.select_mot_ele).click()

            # 点击Save&Close
            self.click_element(ds.saveClose_btn)
            time.sleep(5)
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

     # Copy Deal Item
    def copy_dealItem(self):
        try:
            doc = 'Copy Deal Item'
            time.sleep(20)  # 自动刷新页面，需要添加等待时间
            self.driver.switch_to.window(main_window)
            self.switch_iframe(self.get_element(ds.ele_iframe2), doc)
            self.wait_eleVisible(ds.view_ele, wait_times=30, doc=doc)
            # 选择一条Item数据
            self.driver.find_element(*ds.firstItem_checkbox).click()
            self.click_element(ds.copyItem_btn)  # 点击copy按钮
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击Deal Item 的show log
    def showlog_Item(self):
        try:
            doc = 'Deal Item Log'
            time.sleep(10)
            # 选择一条Item数据
            self.driver.find_element(*ds.firstItem_checkbox).click()
            self.click_element(ds.logItem_btn)  # 点击log按钮
            time.sleep(3)

            # 切换到编辑item弹出窗口
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'DealItemLog' in self.driver.title:
                    break
            self.driver.close()
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    # Delete Deal Item
    def delete_DealItem(self):
        try:
            doc = 'Delete Deal Item'
            time.sleep(20)  # 自动刷新页面，需要添加等待时间
            # 选择一条Item数据
            self.driver.find_element(*ds.firstItem_checkbox).click()
            time.sleep(1)
            self.click_element(ds.deleteItem_btn)  # 点击delete按钮
            time.sleep(5)
            self.driver.switch_to.alert.accept()  # 确认
            time.sleep(5)
            self.driver.switch_to.alert.accept()  # 确认
            time.sleep(5)
        except:
            self.log.logger_error(doc + "失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    #提交Item
    def Submit_DealItem(self):
        try:
            doc = 'Deal Simulation--> 提交Deal Item'
            # submit deal item
            self.driver.switch_to_window(main_window)
            self.switch_iframe(self.get_element(ds.ele_iframe2), doc)
            # 刷新頁面
            time.sleep(15)
            # 点击Deal Item页面的Submit按钮
            self.wait_eleVisible(ds.dealItem_submit, wait_times=10, doc=doc)
            self.click_element(ds.dealItem_submit)
            # time.sleep(2)
            main_window1 = self.driver.current_window_handle
            # 切换到弹出窗口
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'DealApproverAddOrEdit' in self.driver.title:
                    break
            self.click_element(ds.dealsubmit_btn)
            time.sleep(15)
            self.driver.switch_to_window(main_window1)
            # 提交成功，会有个alert提示

            alert = self.driver.switch_to_alert()
            alertText = alert.text
            time.sleep(1)
            self.driver.switch_to.alert.accept()  # 点击alert的【确认】按钮
            time.sleep(2)
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    # Download/Upload Deal Item
    def Download_DealItem(self):
        try:
            doc = 'Deal Simulation-->Download/Upload Deal Item'
            self.driver.switch_to.default_content()
            self.switch_iframe(self.get_element(ds.ele_iframe2), doc)
            self.wait_eleVisible(ds.DownloadItem_btn, wait_times=10, doc=doc)
            self.click_element(ds.DownloadItem_btn)
            time.sleep(15)

            # 获取最新下载的文件
            downloadFile = self.get_latest_fileName()
            time.sleep(5)
            # 32 保存数据到Excel对应的单元格中(自动输入volumn,Street Price(LC)到excel中)
            self.write_excel(downloadFile, 'Deal', 17, 118, '500')  # Volume # sheet名，行数，列数，value值
            self.write_excel(downloadFile, 'Deal', 17, 122, '20000')  # Street Price(LC)
            self.write_excel(downloadFile, 'Deal', 17, 174, 'Air')  # MOT

            self.write_excel(downloadFile, 'Deal', 18, 118, '500')
            self.write_excel(downloadFile, 'Deal', 18, 122, '20000')
            self.write_excel(downloadFile, 'Deal', 18, 174, 'Air')

            self.write_excel(downloadFile, 'Deal', 19, 118, '500')
            self.write_excel(downloadFile, 'Deal', 19, 122, '20000')
            self.write_excel(downloadFile, 'Deal', 19, 174, 'Air')

            self.write_excel(downloadFile, 'Deal', 20, 118, '500')
            self.write_excel(downloadFile, 'Deal', 20, 122, '20000')
            self.write_excel(downloadFile, 'Deal', 20, 174, 'Air')

            # # 46 保存数据到Excel对应的单元格中(自动输入volumn,Street Price(LC)到excel中)
            # self.write_excel(downloadFile, 'Deal',17, 110, '500')    # Volume # sheet名，行数，列数，value值
            # self.write_excel(downloadFile, 'Deal', 17, 114, '20000') # Street Price(LC)
            # self.write_excel(downloadFile, 'Deal', 17, 166, 'Air')   #
            #
            # self.write_excel(downloadFile, 'Deal', 18, 110, '500')
            # self.write_excel(downloadFile, 'Deal', 18, 114, '20000')
            # self.write_excel(downloadFile, 'Deal', 18, 166, 'Air')
            #
            # self.write_excel(downloadFile, 'Deal', 19, 110, '500')
            # self.write_excel(downloadFile, 'Deal', 19, 114, '20000')
            # self.write_excel(downloadFile, 'Deal', 19, 166, 'Air')
            #
            # self.write_excel(downloadFile, 'Deal', 20, 110, '500')
            # self.write_excel(downloadFile, 'Deal', 20, 114, '20000')
            # self.write_excel(downloadFile, 'Deal', 20, 166, 'Air')
            time.sleep(15)
            # 切换到upload文件的新窗口
            self.wait_eleVisible(ds.UploadItem_btn, wait_times=10, doc=doc)
            self.driver.find_element(*ds.UploadItem_btn).click()
            # self.click_element(ds.UploadItem_btn)
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                if 'DealItemUpload' in self.driver.title:
                    break
            # Upload Deal Item
            self.driver.find_element(*ds.Uploadtext).send_keys(downloadFile)
            print("********************文件名：",downloadFile)
            time.sleep(5)
            self.wait_eleVisible(ds.btnUpload, wait_times=10, doc=doc)
            self.click_element(ds.btnUpload)
            time.sleep(10)
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise