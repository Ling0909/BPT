from Common.base_page import BasePage
from PageLocators.locators_CountryAdjust2 import LocatorsCountryAdjust2 as lca
from Common.datas_stor import DatasStor
import xlrd
from Common.parameters.parameter_CountryAdjust2 import *
import time
import datetime

class PageCountryAdjustment2(BasePage):

    #下载policy list
    def download_policyList_CountryAdjustment2(self,policyType):
        doc='policyList页面，下载Excel-policyList数据功能'
        self.switch_iframe(self.get_element(lca.ele_iframe))
        self.wait_eleVisible(lca.select_policyType, doc=doc)
        self.select_selectBox(lca.select_policyType,policyType)#选择policyType值
        time.sleep(2)
        self.click_element(lca.button_search,doc)
        self.wait_eleVisible(lca.load_ok, doc=doc)
        self.click_element(lca.button_export,doc)
        self.wait_eleVisible(lca.ele_iframe_export, doc=doc)
        self.switch_iframe(self.get_element(lca.ele_iframe_export,doc))
        self.wait_eleVisible(lca.button_export_in_frame, doc=doc)
        self.click_element(lca.button_export_in_frame,doc)
        time.sleep(5)
        self.driver.switch_to.parent_frame()
        self.click_element(lca.aui_close,doc)#关闭弹窗

    # 从下载的Excel中筛选数据，得到字典
    def get_bestDatas(self):
        # (依赖：1、Excel已下载；2、已经在portfolio界面获取了baseInfo信息）
        filename = self.get_latest_fileName()
        print('要打开的的Excel文件名字为：{}'.format(filename))
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
        #nrowdict=['', '', '', 1.0, 'Australia', 'TS', 'NB', 'ALL', 6.65, 9.96, 8.12, 11.54, 33.67]

    def get_the_last_data(self, nrowdict,CostFunding_ValueDict):
        """
        :param nrowdict: 列表
        :param CostFunding_ValueDict: 字典--{'CostFunding_value': '33.67', 'APR.': '33.67', 'MAY.': '33.67', 'JUN.': '33.67'}
        :return: excelMons字典--{'CostFunding_value': '33.67', 'APR.': '33.67', 'MAY.': '33.67', 'JUN.': '33.67'}
        """
        CurrentMon = datetime.datetime.now().month
        year = datetime.datetime.now().year  # 系统中当前的年份
        Plan_Cycle = getattr(DatasStor, 'Plan_Cycle')  # 页面中的Plan Cycle  'FY19/20Q1'

        if CurrentMon - 4 >= 0:#获取当前月份对应的季度
            Cur_Cycle = (CurrentMon-1)//3
        else: #如果月份是1,2,3月的情况
            Cur_Cycle = (CurrentMon+12)//3

        #为了区分上一个季度的情况，需要通过季度的计算来进行判断
        excel_Cycle_data=''
        if int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 0:#判断页面中季度年份与系统当前年份相同
            excel_Cycle_data = 'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1)
        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 1:#判断页面中季度年份大于系统当前年份
            excel_Cycle_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1 + 4)
        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == -1:#判断页面中季度年份小于系统当前年份
            excel_Cycle_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle - 4)

        if nrowdict==[]:#判断Excel中筛选结果为空的情况
            nrowdict=['', '', '', '', 'CountryName', 'AP RTM', 'Product Group', 'ALL', 0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]

        excelMons = {}
        for key in CostFunding_ValueDict.keys():
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
        # 分支依据：页面中是否存在月份对应的值为0的情况，只有Q0会出现，原因是Excel表格中未保留MONTH-4的值
            if excel_Cycle_data != 'Q0':

                if (monthsDict[key] - CurrentMon) < -3:
                    excel_data= f'MONTH{monthsDict[key] - CurrentMon+12}'
                else:
                    excel_data = f'MONTH{monthsDict[key] - CurrentMon}'
                excelMons[key] ='%.2f' %nrowdict[monthValues[excel_data]]
            else:
                if monthsDict[key] - CurrentMon > -4:
                    excel_data = f'MONTH{monthsDict[key] - CurrentMon}'
                    excelMons[key] = '%.2f' % nrowdict[monthValues[excel_data]]
                else:
                    excelMons[key] = '%.2f' % 0.00
        #计算平均值并放到字典excelMons中
        Sum_monthDatas = 0.00  # Sum_monthDatas代表各月份的值相加
        for key in excelMons.values():
            Sum_monthDatas += float(key)
        excelMons['CostFunding_value'] = '%.2f' % (Sum_monthDatas / 3)

        return excelMons

    def add_policyList_Datas(self,filename):
        doc='policyList页面-添加数据功能'
        self.wait_eleVisible(lca.ele_iframe,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lca.ele_iframe))#进入iframe
        self.wait_eleVisible(lca.button_import, doc=doc)
        self.click_element(lca.button_import,doc)#点击import按钮
        self.wait_eleVisible(lca.ele_iframe_export, doc=doc)
        self.switch_iframe(self.get_element(lca.ele_iframe_export))#进入打开的弹窗界面的iframe

        #选择本地Excel文件，并上传
        self.input_text(lca.input_File_Upload,filename,doc) # 点击选择文件按钮
        self.click_element(lca.button_import_in_iframe,doc)
        time.sleep(15)
        self.driver.switch_to.default_content()