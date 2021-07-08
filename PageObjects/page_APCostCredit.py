from selenium.webdriver.support.ui import Select
from Common.base_page import BasePage
from PageLocators.locators_APCostCredit import LocatorsAPCostCredit as lacc
from Common.datas_stor import DatasStor
import xlrd
from Common.parameters.parameter_APCostCredit import *
import time
import datetime

class PageAPCostCredit(BasePage):

    #下载policy list
    def download_policyList_APCostCredit(self,policyType):
        doc='policyList页面，下载Excel-policyList数据功能'
        self.driver.switch_to.frame(self.driver.find_element(*lacc.ele_iframe))
        self.wait_eleVisible(lacc.select_policyType, doc=doc)
        select_policyType=self.driver.find_element(*lacc.select_policyType)
        Select(select_policyType).select_by_value(policyType)#选择policyType值
        time.sleep(2)
        self.driver.find_element(*lacc.button_search).click()
        self.wait_eleVisible(lacc.load_ok, doc=doc)
        self.driver.find_element(*lacc.button_export).click()
        self.wait_eleVisible(lacc.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lacc.ele_iframe_export))
        self.wait_eleVisible(lacc.button_export_in_frame, doc=doc)
        self.driver.find_element(*lacc.button_export_in_frame).click()
        time.sleep(5)
        self.driver.switch_to.parent_frame()
        self.driver.find_element(*lacc.aui_close).click()#关闭弹窗


    # 从下载的Excel中筛选数据，得到字典
    def get_bestDatas(self):
        # (依赖：1、Excel已下载；2、已经在portfolio界面获取了baseInfo信息）
        filename = self.get_latest_fileName()
        print('要打开的的Excel文件名字为：{}'.format(filename))
        # self.log.logger_info('要打开的的Excel文件名字为：{}'.format(filename))
        book = xlrd.open_workbook(filename)
        # 获取第一张sheet表单
        sh = book.sheets()[0]
        nrowdict = []
        nrowdict0 = []
        nrowdict1 = []
        nrowdict2 = []
        nrowdict3=[]
        baseInfo = getattr(DatasStor, 'baseInfo')
        for nrow in range(1, sh.nrows):
            everyrow = sh.row_values(nrow)
            if everyrow[COUNTRY] != baseInfo['COUNTRY']:
                continue
            if everyrow[PRODUCT_GROUP] != baseInfo['PRODUCT_GROUP']:
                continue
            # 判断AP_RTM有确定值，PRODUCT_CATEGORY也有确定值的情况
            if everyrow[AP_RTM] ==baseInfo['AP_RTM'] and everyrow[PRODUCT_CATEGORY] == baseInfo['PRODUCT_CATEGORY']:
                nrowdict0=everyrow
            # 判断AP_RTM有确定值，PRODUCT_CATEGORY为ALL的情况
            elif everyrow[AP_RTM] ==baseInfo['AP_RTM'] and everyrow[PRODUCT_CATEGORY] =='ALL':
                nrowdict1=everyrow
            # 判断AP_RTM为ALL，PRODUCT_CATEGORY有确定值的情况
            elif everyrow[AP_RTM] =='ALL' and everyrow[PRODUCT_CATEGORY] ==baseInfo['PRODUCT_CATEGORY']:
                nrowdict2=everyrow
            # 判断AP_RTM、PRODUCT_CATEGORY都为ALL的情况
            elif everyrow[AP_RTM] =='ALL' and everyrow[PRODUCT_CATEGORY] =='ALL':
                nrowdict3=everyrow
        #优先级是AP_RTM高于PRODUCT_CATEGORY

        if len(nrowdict0) != 0:
            nrowdict = nrowdict0
        elif len(nrowdict1)!=0:
            nrowdict=nrowdict1
        elif len(nrowdict2)!=0:
            nrowdict=nrowdict2
        elif len(nrowdict3)!=0:
            nrowdict=nrowdict3
        self.log.logger_info('筛选后得到的Excel值为：{}'.format(nrowdict))
        return nrowdict
    """
    {65: ['', '76E87E01-91AE-4D7A-9288-2C3E13F41E0B', '', '', 'EMEA', 'testyh008_Product Series makeSure', 'ALL', 'Germany', 'ALL', 'NB', 'ALL', 'V Series', 'ALL', 'ALL', 'ALL', 'ALL', 0.0, 100000.0, 8.0, 8.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 16.0, 'N', 0.0, 0.0, 0.0, 0.0], 
    77: ['', '356046EE-5867-4D00-9399-41844AF9E860', '', '', 'EMEA', '', 'ALL', 'ALL', 'ALL', 'NB', 'Lenovo NB', 'V Series', 'ALL', '128G M.2 PCIE 2242', 'ALL', 'ALL', 0.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'N', 0.0, 0.0, 0.0, 0.0], 
    257: ['', '52491258-E381-454A-BCD4-FACD33A3C9E0', '', '', 'EMEA', 'testyh006_ProductCategory makeSure', 'ALL', 'Germany', 'ALL', 'NB', 'Lenovo NB', 'ALL', 'ALL', 'ALL', 'ALL', 'ALL', 0.0, 100000.0, 6.0, 6.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 16.0, 'N', 0.0, 0.0, 0.0, 0.0]}
    """

    def get_the_last_data(self, nrowdict,CostFunding_ValueDict):
        """
        :param nrowdict: 列表
        :param CostFunding_ValueDict: 字典--{'CostFunding_value': '33.67', 'APR.': '33.67', 'MAY.': '33.67', 'JUN.': '33.67'}
        :return: 字符串
        """
        excel_data = ''
        CurrentMon = datetime.datetime.now().month
        year = datetime.datetime.now().year #系统中当前的年份
        Plan_Cycle = getattr(DatasStor, 'Plan_Cycle')  # 页面中的Plan Cycle  'FY19/20Q1'
        # 只对每个季度的第一个月进行计算，以下判断只适用于每季度的第一个月
        if CurrentMon - 4 >= 0:#获取当前月份对应的季度
            Cur_Cycle = (CurrentMon-1)//3

        else: #如果月份是1,2,3月的情况
            Cur_Cycle = (CurrentMon+12)//3

        if int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 0:#判断页面中季度年份与系统当前年份相同
            excel_data = 'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1)
            print(f'Plan_Cycle:{Plan_Cycle};Cur_Cycle:{Cur_Cycle}')
        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 1:#判断页面中季度年份大于系统当前年份
            excel_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1 + 4)

        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == -1:#判断页面中季度年份小于系统当前年份
            excel_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle - 4)

        print(f'excel_data的值为{excel_data}')
        if nrowdict==[]:#判断Excel中筛选结果为空的情况
            nrowdict=['', '', '', 1.0, 'Australia', 'TS', 'NB', 'ALL', 0.00, 0.00, 0.00, 0.00, 0.00]
        monthkey = []
        for key in CostFunding_ValueDict.keys():
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
            monthkey.append(key)  # monthkey=['SEPT.', 'OCT.', 'NOV.']
        # 分支依据：页面中是否存在月份对应的值为0的情况，只有Q0会出现，原因是数据库未保留MONTH-4的值
        excelMons = {}
        if excel_data != 'Q0':
            excelMons[monthkey[0]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[1]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[2]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons['CostFunding_value'] = '%.2f' % ((float(excelMons[monthkey[0]]) + float(
                excelMons[monthkey[1]]) + float(excelMons[monthkey[2]])) / 3)
        else:
            for key in monthkey:
                if monthsDict[key] - CurrentMon > -4:
                    excelMons[key] = '%.2f' % nrowdict[CycleValues[excel_data]]
                else:
                    excelMons[key] = '%.2f' % 0.00
            Sum_monthDatas = 0.00  # Sum_monthDatas代表各月份的值相加
            for key in excelMons.values():
                Sum_monthDatas += float(key)
            excelMons['CostFunding_value'] = '%.2f' % (Sum_monthDatas / 3)
        monthkey = []
        for key in CostFunding_ValueDict.keys():
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
            monthkey.append(key)  # monthkey=['SEPT.', 'OCT.', 'NOV.']
        # 分支依据：页面中是否存在月份对应的值为0的情况，只有Q0会出现，原因是数据库未保留MONTH-4的值
        excelMons = {}
        i=3
        if excel_data != 'Q0':
            excelMons[monthkey[0]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[1]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[2]] = '%.2f' % nrowdict[CycleValues[excel_data]]
            excelMons['CostFunding_value'] = '%.2f' % ((float(excelMons[monthkey[0]]) + float(
                excelMons[monthkey[1]]) + float(excelMons[monthkey[2]])) / i)
        else:
            for key in monthkey:
                if monthsDict[key] - CurrentMon > -4:
                    excelMons[key] = '%.2f' % nrowdict[CycleValues[excel_data]]
                else:
                    excelMons[key] = '%.2f' % 0.00
                    i-=1
            if i==0:
                i=1
            Sum_monthDatas = 0.00  # Sum_monthDatas代表各月份的值相加
            for key in excelMons.values():
                Sum_monthDatas += float(key)
            excelMons['CostFunding_value'] = '%.2f' % (Sum_monthDatas /i)
        return excelMons

    def add_policyList_Datas(self,filename):
        doc='policyList页面-添加数据功能'
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lacc.ele_iframe))
        self.wait_eleVisible(lacc.ele_iframe,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lacc.ele_iframe))#进入iframe
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lacc.button_import))
        self.wait_eleVisible(lacc.button_import, doc=doc)
        self.driver.find_element(*lacc.button_import).click()#点击import按钮
        # WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(lacc.ele_iframe_export))
        self.wait_eleVisible(lacc.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lacc.ele_iframe_export))#进入打开的弹窗界面的iframe

        #选择本地Excel文件，并上传
        self.driver.find_element(*lacc.input_File_Upload).send_keys(filename) # 点击选择文件按钮
        self.driver.find_element(*lacc.button_import_in_iframe).click()
        time.sleep(15)
        self.driver.switch_to.default_content()

