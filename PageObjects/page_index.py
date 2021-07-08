from PageLocators.locators_indexPage import LocatorsIndexPage as lip
from selenium.webdriver.common.action_chains import ActionChains
from Common.base_page import BasePage
import time

class PageIndex(BasePage):

    def enter_main_menu(self,menuName):
        doc='首页-进入主菜单'
        self.driver.switch_to.default_content()
        self.ac = ActionChains(self.driver)
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(lip.button_switch))
        self.wait_eleVisible(lip.button_switch,doc=doc)
        ele_switch = self.driver.find_element(*lip.button_switch)
        self.ac.move_to_element(ele_switch).perform()  # 鼠标移动到switch按钮并打开弹框
        time.sleep(1)
        # 鼠标移动到左侧列表
        self.driver.find_element_by_link_text(menuName).click()

    # 包含二级菜单的，进入页面功能
    def enter_pageDoubleMenu(self,nameMenuLeve1,nameMenuLeve2):
        doc='含二级menu的页面菜单点击'
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.parent_frame()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(*lip.ele_iframe))
        time.sleep(1)
        self.ac.move_to_element(self.driver.find_element(*lip.img_Home)).perform()#鼠标移动到侧边栏
        time.sleep(1)
        self.wait_eleVisible(lip.eles_MenuLeve1_SMB, doc=doc)#等待一级菜单出现
        eles_MenuLeve1=self.driver.find_elements(*lip.eles_MenuLeve1_SMB)
        for ele_MenuLeve1 in eles_MenuLeve1:
            if ele_MenuLeve1.text==nameMenuLeve1:
                ele_MenuLeve1.click()   #点击一级菜单
                time.sleep(2)
                self.driver.find_element_by_link_text(nameMenuLeve2).click()    #点击二级菜单
                break
        time.sleep(8)
        self.driver.switch_to.parent_frame()

        # 包含二级菜单的，进入execution plan页面功能

    def enter_pageDoubleMenu_executePlan(self, nameMenuLeve1, nameMenuLeve2):
        doc = '含二级menu的页面菜单点击'
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.parent_frame()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(*lip.ele_iframe))
        time.sleep(1)
        self.ac.move_to_element(self.driver.find_element(*lip.img_Home)).perform()  # 鼠标移动到侧边栏
        time.sleep(1)
        self.wait_eleVisible(lip.eles_MenuLeve1_executePlan, doc=doc)  # 等待一级菜单出现
        eles_MenuLeve1 = self.driver.find_elements(*lip.eles_MenuLeve1_executePlan)
        for ele_MenuLeve1 in eles_MenuLeve1:
            if ele_MenuLeve1.text == nameMenuLeve1:
                ele_MenuLeve1.click()  # 点击一级菜单
                time.sleep(2)
                self.driver.find_element_by_link_text(nameMenuLeve2).click()  # 点击二级菜单
                break
        time.sleep(8)
        self.driver.switch_to.parent_frame()

    def enter_pageSingleMenu(self,nameMenuLeve1):
        doc='不含二级menu的页面菜单点击'
        self.ac = ActionChains(self.driver)
        self.driver.switch_to.parent_frame()
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(*lip.ele_iframe))
        time.sleep(1)
        self.ac.move_to_element(self.driver.find_element(*lip.img_Home)).perform()#鼠标移动到侧边栏
        time.sleep(2)
        self.wait_eleVisible(lip.eles_MenuLeve1_CPM, doc=doc)#等待一级菜单出现
        eles_MenuLeve1=self.driver.find_elements(*lip.eles_MenuLeve1_CPM)
        for ele_MenuLeve1 in eles_MenuLeve1:
            if ele_MenuLeve1.text==nameMenuLeve1:
                ele_MenuLeve1.click()   #点击一级菜单
                time.sleep(3)
        time.sleep(5)
        self.driver.switch_to.parent_frame()