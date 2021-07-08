from Common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from PageLocators.locators_PortfolioCheck import LocatorsPortfolioCheck as lb
import time
import xlrd
from TestDatas.common_datas import CommonDatas as da



main_window=''
class PagePortfolioCheck(BasePage):

      #portfolio相关
      def portfolioCheck(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
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
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        time.sleep(2)
        self.driver.find_element(*lb.country).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[text()="{}"]'.format(da.ww_CountryGroup[0])).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlProductGroup"]//option[text()="{}"]'.format(da.ww_ProductGroup[0])).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlQuarter"]//option[text()="FY20/21Q4"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder1_ddlStatus"]//option[text()="Approved"]').click()
        time.sleep(1)
        self.driver.find_element(*lb.search).click()
        time.sleep(5)
        self.driver.find_element(*lb.table1).click()
        time.sleep(15)

        self.driver.find_element(*lb.pc).click()
        time.sleep(1)
        pageVolume1=float(str(self.driver.find_element(*lb.Volume).text).replace(',',''))
        pageNetRevenue1 = float(str(self.driver.find_element(*lb.NetRevenue).text).replace(',',''))
        pageNetBMCGP1 =float(str(self.driver.find_element(*lb.NetBMCGP).text).replace(',',''))
        list1.append(pageVolume1)
        list2.append(pageNetRevenue1)
        list3.append(pageNetBMCGP1)
        self.driver.back()
        time.sleep(10)
        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.table2).click()
        time.sleep(15)
        self.driver.find_element(*lb.pc).click()
        time.sleep(1)
        pageVolume2 = float(str(self.driver.find_element(*lb.Volume).text).replace(',', ''))
        pageNetRevenue2= float(str(self.driver.find_element(*lb.NetRevenue).text).replace(',', ''))
        pageNetBMCGP2 = float(str(self.driver.find_element(*lb.NetBMCGP).text).replace(',', ''))

        list1.append(pageVolume2)
        list2.append(pageNetRevenue2)
        list3.append(pageNetBMCGP2)
        self.driver.back()
        time.sleep(10)

        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.table3).click()
        time.sleep(15)
        pageVolume3 = float(str(self.driver.find_element(*lb.Volume1).text).replace(',', ''))
        pageNetRevenue3 = float(str(self.driver.find_element(*lb.NetRevenue2).text).replace(',', ''))
        pageNetBMCGP3 = float(str(self.driver.find_element(*lb.NetBMCGP3).text).replace(',', ''))

        list1.append(pageVolume3)
        list2.append(pageNetRevenue3)
        list3.append(pageNetBMCGP3)
        self.driver.back()
        time.sleep(10)

        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.table4).click()
        time.sleep(15)
        self.driver.find_element(*lb.pc).click()
        time.sleep(1)
        pageVolume4 = float(str(self.driver.find_element(*lb.Volume).text).replace(',',''))
        pageNetRevenue4 = float(str(self.driver.find_element(*lb.NetRevenue).text).replace(',',''))
        pageNetBMCGP4 = float(str(self.driver.find_element(*lb.NetBMCGP).text).replace(',',''))

        list1.append(pageVolume4)
        list2.append(pageNetRevenue4)
        list3.append(pageNetBMCGP4)
        self.driver.back()
        time.sleep(10)

        self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        self.driver.find_element(*lb.table5).click()
        time.sleep(15)
        self.driver.find_element(*lb.pc).click()
        time.sleep(1)
        pageVolume5 = float(str(self.driver.find_element(*lb.Volume).text).replace(',', ''))
        pageNetRevenue5= float(str(self.driver.find_element(*lb.NetRevenue).text).replace(',', ''))
        pageNetBMCGP5 = float(str(self.driver.find_element(*lb.NetBMCGP).text).replace(',', ''))

        list1.append(pageVolume5)
        list2.append(pageNetRevenue5)
        list3.append(pageNetBMCGP5)
        self.driver.back()
        time.sleep(10)
        a1=float(list1[0])
        a2=float(list1[1])
        a3=float(list1[2])
        a4=float(list1[3])
        a5=float(list1[4])
        b1=float(list2[0])
        b2=float(list2[1])
        b3=float(list2[2])
        b4=float(list2[3])
        b5=float(list2[4])
        c1=float(list3[0])
        c2=float(list3[1])
        c3=float(list3[2])
        c4=float(list3[3])
        c5=float(list3[4])
        self.log.logger_info(f'页面Volume:{a1}')
        self.log.logger_info(f'页面Volume:{a1}')
        self.log.logger_info(f'页面Volume:{a2}')
        self.log.logger_info(f'页面Volume:{a3}')
        self.log.logger_info(f'页面Volume:{a4}')
        self.log.logger_info(f'页面Volume:{a5}')
        self.log.logger_info(f'页面Net Revenue ($):{b1}')
        self.log.logger_info(f'页面Net Revenue ($):{b2}')
        self.log.logger_info(f'页面Net Revenue ($):{b3}')
        self.log.logger_info(f'页面Net Revenue ($):{b4}')
        self.log.logger_info(f'页面Net Revenue ($):{b5}')
        self.log.logger_info(f'页面Net BMC GP ($):{c1}')
        self.log.logger_info(f'页面Net BMC GP ($):{c2}')
        self.log.logger_info(f'页面Net BMC GP ($):{c3}')
        self.log.logger_info(f'页面Net BMC GP ($):{c4}')
        self.log.logger_info(f'页面Net BMC GP ($):{c5}')

        pageVolumesum =a1+a2+a3+a4+a5
        self.log.logger_info(f'页面Sum of Volume:{pageVolumesum}')
        pageNetRevenuesum=b1+b2+b3+b4+b5
        self.log.logger_info(f'页面Sum of Total Net Revenue ($):{pageNetRevenuesum}')
        pageNetBMCGPsum=c1+c2+c3+c4+c5
        self.log.logger_info(f'页面Sum of Total Net BMC GP ($):{pageNetBMCGPsum}')
        list4.append(pageVolumesum)
        list4.append(pageNetRevenuesum)
        list4.append(pageNetBMCGPsum)

        print(list4)

        return list4
      #ww  report相关
      def portfolioCheck_ww(self):
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe1))
        # time.sleep(2)
        # bpt0 = self.driver.find_element(*lb.ele_bpt)
        # self.ac.move_to_element(bpt0).perform()  # 悬浮于BPT
        # time.sleep(2)
        # self.driver.find_element(*lb.menu_track).click()  # 点击country plan summary
        # time.sleep(3)
        # self.driver.find_element(*lb.menu_ww_report).click()  # 点击country plan summary
        # time.sleep(5)
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame(self.driver.find_element(*lb.ele_iframe2))
        # self.driver.find_element(*lb.country_ww).click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//span[text()="{}"]'.format(da.ww_CountryGroup[0])).click()
        # self.driver.find_element(*lb.country_ww).click()
        # # time.sleep(3)
        # # self.driver.find_element(*lb.select_planCycle_ww).click()
        # # time.sleep(1)
        # # self.driver.find_element_by_xpath('//label[text()="FY21/22Q1"]').click()
        # # self.driver.find_element(*lb.select_planCycle_ww).click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder2_ddl_PlanType"]//option[text()="{}"]'.format(da.ww_PlanType[0])).click()
        # time.sleep(1)
        # self.driver.find_element(*lb.select_productGroup_ww).click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//label[text()="{}"]'.format(da.ww_ProductGroup[0])).click()
        # self.driver.find_element(*lb.select_productGroup_ww).click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder2_ddlPortfolioType"]//option[text()="To be Approved"]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//select[@id="ContentPlaceHolder2_ddlVersion"]//option[text()="All"]').click()
        # time.sleep(1)
        # self.driver.find_element(*lb.refresh_ww).click()
        # time.sleep(6)
        # self.driver.switch_to.alert.accept()
        # time.sleep(6)# 确认
        # self.driver.find_element(*lb.download_ww).click()
        # time.sleep(5)
        # self.driver.find_element(*lb.downloads_ww).click()
        # time.sleep(6)
        # self.driver.switch_to.alert.accept()
        # time.sleep(6)  # 确认
        # self.driver.find_element(*lb.download_tab_ww).click()
        # time.sleep(180)
        # self.driver.find_element(*lb.select_page_ww).click()
        # time.sleep(6)
        # self.driver.find_element(*lb.select_page_ww1).click()
        # time.sleep(6)
        # self.driver.find_element(*lb.download_tab_table1).click()
        # time.sleep(10)
        file_new = self.get_latest_fileName()
        time.sleep(5)
        book = xlrd.open_workbook(file_new)
        sh = book.sheets()[1]
        list2=[]
        pageVolume_check = '%.2f'%(float(str(sh.cell(21,1).value).replace(',','')))
        pageNetRevenue_check = '%.2f'%(float(str(sh.cell(21,3).value).replace(',','')))
        pageNetBMCGP_check = '%.2f'%(float(str(sh.cell(21,4).value).replace(',','')))
        self.log.logger_info(f'ww report Sum of Volume:{pageVolume_check}')
        self.log.logger_info(f'ww report um of Total Net Revenue ($):{pageNetRevenue_check}')
        self.log.logger_info(f'ww report Sum of Total Net BMC GP ($):{pageNetBMCGP_check}')

        list2.append(pageVolume_check)
        list2.append(pageNetRevenue_check)
        list2.append(pageNetBMCGP_check)

        return list2


























