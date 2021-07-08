from selenium.webdriver.support.ui import Select
from Common.base_page import BasePage
from PageLocators.locators_nonBMCUplift import LocatorsNonBMCUplift as lnbu
from Common.datas_stor import DatasStor
import xlrd
from Common.parameters.parameter_nonBMCUplift import *
import time
import datetime

class PageNonBMCUplift(BasePage):

    #下载policy list
    def download_policyList_CountryAdjustment(self,policyType):
        doc='policyList页面，下载Excel-policyList数据功能'
        self.driver.switch_to.frame(self.driver.find_element(*lnbu.ele_iframe))
        self.wait_eleVisible(lnbu.select_policyType, doc=doc)
        select_policyType=self.driver.find_element(*lnbu.select_policyType)
        Select(select_policyType).select_by_value(policyType)#选择policyType值
        time.sleep(2)
        self.driver.find_element(*lnbu.button_search).click()
        self.wait_eleVisible(lnbu.load_ok, doc=doc)
        self.driver.find_element(*lnbu.button_export).click()
        self.wait_eleVisible(lnbu.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lnbu.ele_iframe_export))
        self.wait_eleVisible(lnbu.button_export_in_frame, doc=doc)
        self.driver.find_element(*lnbu.button_export_in_frame).click()
        time.sleep(5)
        self.driver.switch_to.parent_frame()
        self.driver.find_element(*lnbu.aui_close).click()#关闭弹窗


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
        #nrowdict=['', '', '', 1.0, 'Australia', 'TS', 'NB', 'ALL', 6.65, 9.96, 8.12, 11.54, 33.67]

    def get_the_last_data(self, nrowdict,CostFunding_ValueDict):
        """
        :param nrowdict: 列表
        :param CostFunding_ValueDict: 字典--{'CostFunding_value': '33.67', 'APR.': '33.67', 'MAY.': '33.67', 'JUN.': '33.67'}
        :return: excelMons字典--{'CostFunding_value': '33.67', 'APR.': '33.67', 'MAY.': '33.67', 'JUN.': '33.67'}
        """
        excel_data = ''
        CurrentMon = datetime.datetime.now().month
        year = datetime.datetime.now().year  # 系统中当前的年份
        Plan_Cycle = getattr(DatasStor, 'Plan_Cycle')  # 页面中的Plan Cycle  'FY19/20Q1'

        if CurrentMon - 4 >= 0:#获取当前月份对应的季度
            Cur_Cycle = (CurrentMon-1)//3
        else: #如果月份是1,2,3月的情况
            Cur_Cycle = (CurrentMon+12)//3

        if int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 0:#判断页面中季度年份与系统当前年份相同
            excel_data = 'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1)
        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == 1:#判断页面中季度年份大于系统当前年份
            excel_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle + 1 + 4)
        elif int(Plan_Cycle[2:4]) - int(str(year)[2:4]) == -1:#判断页面中季度年份小于系统当前年份
            excel_data =  'Q{}'.format(int(Plan_Cycle[-1]) - Cur_Cycle - 4)

        if nrowdict==[]:#判断Excel中筛选结果为空的情况
            nrowdict=['', '', '', 1.0, 'Australia', 'TS', 'NB', 'ALL', 0.00, 0.00, 0.00, 0.00, 0.00]

        monthkey = []
        for key in CostFunding_ValueDict.keys():
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
            monthkey.append(key)  # monthkey=['SEPT.', 'OCT.', 'NOV.']
        # 分支依据：页面中是否存在月份对应的值为0的情况，只有Q0会出现，原因是数据库未保留MONTH-4的值
        excelMons = {}
        if excel_data!='Q0':
            excelMons[monthkey[0]] = '%.2f' %nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[1]] =  '%.2f' %nrowdict[CycleValues[excel_data]]
            excelMons[monthkey[2]] =  '%.2f' %nrowdict[CycleValues[excel_data]]
            excelMons['CostFunding_value'] = '%.2f' % ((float(excelMons[monthkey[0]])+float(excelMons[monthkey[1]])+float(excelMons[monthkey[2]]))/3)
        else:
            for key in monthkey:
                if monthsDict[key] - CurrentMon>-4:
                    excelMons[key]='%.2f' %nrowdict[CycleValues[excel_data]]
                else:
                    excelMons[key]='%.2f' % 0.00
            Sum_monthDatas = 0.00  # Sum_monthDatas代表各月份的值相加
            for key in excelMons.values():
                Sum_monthDatas+=float(key)
            excelMons['CostFunding_value'] = '%.2f' % (Sum_monthDatas/ 3)
        return excelMons

    def get_the_last_data_ANZ(self):
        doc='国家的region是ANZ时，通过页面加减获取值'
        FundingsDict = {}  # FundingsDict={'GEO_FundingMOU':[240.00,239.00,240.00,241.00]}
        # 将所有元素放到字典中
        eles_FundingsDict = {}
        eles_FundingsDict['CountryAdjustment'] = [lnbu.ele_CountryAdjustment,lnbu.eles_CountryAdjustment_mouthsValues]
        eles_FundingsDict['PCA'] = [lnbu.ele_PCA,lnbu.eles_PCA_mouthsValues]
        # 对每个字段三个月份的名字进行获取
        monthsList=[]
        eles_Fundings_mon = self.get_elements(lnbu.eles_CountryAdjustment_months)
        for ele_Funding_monName in eles_Fundings_mon:
            Name_Funding_speci_mon = ele_Funding_monName.text
            monthsList.append(Name_Funding_speci_mon)
        for FundingsName in eles_FundingsDict.keys():
            """
                    取界面各字段的值，并放到FundingsDict字典里
                    遍历元素字典eles_FundingsDict中的key，进而通过eles_FundingsDict[key]对元素进行处理
            """
            Value_Funding_speci = self.get_element_attribute(eles_FundingsDict[FundingsName][0], 'value', doc)  # 获取具体的值
            FundingsDict[FundingsName] = []
            FundingsDict[FundingsName].append(float(Value_Funding_speci.replace(',', '')))

            # 对每个字段三个月份的数值进行获取
            eles_Fundings = self.get_elements(eles_FundingsDict[FundingsName][1])
            for ele_Funding_monValue in eles_Fundings:
                Value_Funding_speci_mon = ele_Funding_monValue.get_attribute('value')
                FundingsDict[FundingsName].append(float(Value_Funding_speci_mon.replace(',', '')))
        sum_avg_Funding = 0  # 将所有值得平均值相加并保存
        sum_month1_Funding = 0  # 保存第一个月的所有值的和
        sum_month2_Funding = 0  # 保存第二个月的所有值的和
        sum_month3_Funding = 0  # 保存第三个月的所有值的和
        sum_FundingsValueDict = {}  # sum_FundingValues={'sum_FundingsValue':[611.20,561.74,611.20,660.66]}
        for FundingValues in FundingsDict.values():  # 遍历FundingsDict所有的values值
            sum_avg_Funding += FundingValues[0]
            sum_month1_Funding += FundingValues[1]  # 将所有值的第一个月的值进行相加并保存
            sum_month2_Funding += FundingValues[2]
            sum_month3_Funding += FundingValues[3]
        sum_FundingsValueDict['CostFunding_value'] = '%.2f' % ((sum_month1_Funding + sum_month2_Funding + sum_month3_Funding) / 3)
        sum_FundingsValueDict[monthsList[0]] = '%.2f' % sum_month1_Funding
        sum_FundingsValueDict[monthsList[1]] = '%.2f' % sum_month2_Funding
        sum_FundingsValueDict[monthsList[2]] = '%.2f' % sum_month3_Funding
        self.log.logger_info(f'FundingsDict的值:{FundingsDict}')
        return sum_FundingsValueDict


    def add_policyList_Datas(self,filename):
        doc='policyList页面-添加数据功能'
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lnbu.ele_iframe))
        self.wait_eleVisible(lnbu.ele_iframe,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lnbu.ele_iframe))#进入iframe
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lnbu.button_import))
        self.wait_eleVisible(lnbu.button_import, doc=doc)
        self.driver.find_element(*lnbu.button_import).click()#点击import按钮
        # WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(lnbu.ele_iframe_export))
        self.wait_eleVisible(lnbu.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lnbu.ele_iframe_export))#进入打开的弹窗界面的iframe

        #选择本地Excel文件，并上传
        self.driver.find_element(*lnbu.input_File_Upload).send_keys(filename) # 点击选择文件按钮
        self.driver.find_element(*lnbu.button_import_in_iframe).click()
        time.sleep(15)
        self.driver.switch_to.default_content()

