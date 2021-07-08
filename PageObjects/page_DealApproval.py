import time
from selenium.webdriver import ActionChains
from Common.base_page import BasePage
from PageLocators.locators_DealApproval import locatorsDealApproval as da

class PageDealApproval(BasePage):

    '''
        导航到Deal Approval页面，进行审批
    '''
    def reject_DealItem(self):
        try:
            doc = 'Deal Approval页面'
            self.driver.switch_to.default_content()
            self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            self.ac = ActionChains(self.driver)
            self.wait_eleVisible(da.reset_btn_ele, wait_times=10, doc=doc)
            self.ac.move_to_element(self.driver.find_element(*da.reset_btn_ele)).perform()
            time.sleep(2)
            # 选择Deal No
            # self.driver.switch_to.default_content()
            # self.wait_eleVisible(da.ele_iframe2, wait_times=10, doc=doc)
            # self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            self.wait_eleVisible(da.dealNo_ele,wait_times=10, doc=doc)
            self.click_element(da.dealNo_ele)

            # self.driver.switch_to.default_content()
            # self.wait_eleVisible(da.ele_iframe2, doc=doc)
            time.sleep(15)  # 等待页面重新刷新加载
            self.driver.switch_to.default_content()
            self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            #检查Reject按钮是否存在
            ex = self.is_eleExist(da.dealItem_reject,doc=doc)
            if self.is_eleExist(da.dealItem_reject,doc=doc):
                # 选择一条Items数据
                self.driver.find_element(*da.firstItem_checkbox).click()
                time.sleep(2)
                # 点击Deal Item页面的Reject按钮
                # self.driver.switch_to.default_content()
                current_window = self.driver.current_window_handle
                # self.switch_iframe(self.get_element(da.ele_iframe2), doc)
                self.wait_eleVisible(da.dealItem_reject, wait_times=10, doc=doc)
                self.click_element(da.dealItem_reject)
                time.sleep(5)
                # 切换到弹出窗口
                for handle in self.driver.window_handles:
                    self.driver.switch_to_window(handle)
                    if 'DealItemApprove' in self.driver.title:
                        break
                self.driver.maximize_window()
                self.wait_eleVisible(da.dealReject_btn, wait_times=10, doc=doc)
                self.click_element(da.dealReject_btn)
                time.sleep(15)
                # 提交成功，会有个alert提示
                self.driver.switch_to.alert.accept()  # 点击alert的【确认】按钮
                time.sleep(5)
                self.driver.switch_to_window(current_window)
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    #Copy/Delete Deal Item数据
    def Delete_DealItem(self):
        try:
            doc = 'Deal Simulation-->Copy/Delete Deal Item数据'
            # 悬浮于BPT
            self.driver.switch_to_default_content()
            self.switch_iframe(self.get_element(da.ele_iframe4), doc)
            self.ac = ActionChains(self.driver)
            self.ac.move_to_element(self.driver.find_element(*da.bpt_ele)).perform()  # 悬浮于BPT
            time.sleep(5)

            # 导航到Execution Plan-->Deal Simulation页面
            self.click_element(da.dealSimulation1)
            time.sleep(2)
            self.click_element(da.dealSimulation2)
            time.sleep(2)
            self.driver.switch_to.default_content()
            self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            self.ac = ActionChains(self.driver)
            search = self.driver.find_element(*da.search_ele)
            self.ac.move_to_element(search).perform()
            # time.sleep(3)

            # 获取Deal No号
            self.wait_eleVisible(da.dealno_ele, wait_times=10, doc=doc)
            DealNo = self.driver.find_element(*da.dealno_ele).get_attribute('textContent')
            print('DealNo: ', DealNo)

            # 点击Deal No对应的Copy图标
            # self.driver.switch_to.default_content()
            # self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            # self.wait_eleVisible(da.copy_btn_ele, wait_times=10, doc=doc)
            # self.click_element(da.copy_btn_ele)

            time.sleep(3)
            # 点击Deal No对应的删除图标
            # self.driver.switch_to.default_content()
            # self.switch_iframe(self.get_element(da.ele_iframe2), doc)
            ele = '//a[text()="' + DealNo + '"]/../following-sibling::td[1]/a[2][@onclick="return DeleteConfirm();"]'
            self.driver.find_element_by_xpath(ele).click()
            # 关闭Alert弹框
            time.sleep(3)
            self.driver.switch_to.alert.accept()  # 确认
            time.sleep(5)
        except:
            self.log.logger_error(doc+"失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise


    #def Approval_DealItem(self):
        #doc='Execution Plan --> Deal Approval页面'
        # self.ac = ActionChains(self.driver)
        # #导航到Deal Approval页面-->悬浮于BPT
        # self.wait_eleVisible(da.ele_iframe4, wait_times=10, doc=doc)
        # self.driver.switch_to_default_content()
        # self.switch_iframe(self.get_element(da.ele_iframe4), doc)
        # self.ac = ActionChains(self.driver)
        # self.ac.move_to_element(self.driver.find_element(*da.bpt_ele)).perform()  # 悬浮于BPT
        # time.sleep(1)

        #进入Deal Approval页面
        # self.wait_eleVisible(da.menu_dealApproval, wait_times=10, doc=doc)
        # self.click_element(da.menu_dealApproval)





