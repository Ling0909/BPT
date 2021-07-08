from selenium.webdriver.support.ui import Select
from Common.base_page import BasePage
from PageLocators.locators_PolicyListPage import LocatorsPolicyListPage as lplp
from Common.datas_stor import DatasStor
import xlrd
from Common.parameters.parameter_policyList import *
import time
import datetime

class PagePolicyList(BasePage):

    #下载policy list
    def download_policyList(self,policyType):
        doc='policyList页面，下载Excel-policyList数据功能'
        self.driver.switch_to.frame(self.driver.find_element(*lplp.ele_iframe))
        self.wait_eleVisible(lplp.select_policyType, doc=doc)
        select_policyType=self.driver.find_element(*lplp.select_policyType)
        Select(select_policyType).select_by_value(policyType)#选择policyType值
        time.sleep(2)
        # select_productGroup = self.driver.find_element(*lplp.select_productGroup)
        # Select(select_productGroup).select_by_value(productGroup)#选择productGroup值
        # time.sleep(2)
        self.driver.find_element(*lplp.button_search).click()
        self.wait_eleVisible(lplp.load_ok, doc=doc)
        self.driver.find_element(*lplp.button_export).click()
        self.wait_eleVisible(lplp.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lplp.ele_iframe_export))
        self.wait_eleVisible(lplp.button_export_in_frame, doc=doc)
        self.driver.find_element(*lplp.button_export_in_frame).click()
        time.sleep(5)
        self.driver.switch_to.parent_frame()
        self.driver.find_element(*lplp.aui_close).click()#关闭弹窗
        time.sleep(3)

    # 从下载的Excel中筛选数据，得到字典
    def get_bestDatas(self):
    #(依赖：1、Excel已下载；2、已经在portfolio界面获取了baseInfo信息）
        filename=self.get_latest_fileName()

        print('要打开的的Excel文件名字为：{}'.format(filename))
        book = xlrd.open_workbook(filename)
        # 获取第一张sheet表单
        sh = book.sheets()[0]
        nrowdict={}
        baseInfo=getattr(DatasStor,'baseInfo')
        for nrow in range(1, sh.nrows):
            everyrow = sh.row_values(nrow)
            if everyrow[GEO] != baseInfo['GEO']:
                continue
            elif everyrow[REGION] != 'ALL' and everyrow[REGION] != baseInfo['Region'] and everyrow[SUB_REGION]!=baseInfo['Sub_Region']:
                continue
            if everyrow[COUNTRY] != 'ALL' and everyrow[COUNTRY] != baseInfo['COUNTRY']:
                continue
            if everyrow[RTM] != 'ALL' and everyrow[RTM] != baseInfo['AP_RTM']:
                continue
            if everyrow[PRODUCT_GROUP] != baseInfo['PRODUCT_GROUP']:
                continue
            if everyrow[PRODUCT_CATEGORY] != 'ALL' and everyrow[PRODUCT_CATEGORY] != baseInfo['PRODUCT_CATEGORY']:
                continue
            if everyrow[PRODUCT_SERIES] != 'ALL' and everyrow[PRODUCT_SERIES] != baseInfo['PRODUCT_SERIES']:
                continue
            if everyrow[PRODUCT_FAMILY] != 'ALL' and everyrow[PRODUCT_FAMILY] != baseInfo['PRODUCT_FAMILY']:
                continue
            if everyrow[MAX_CHANNEL_PRICE] < float(baseInfo['Channel Price($)']):
                continue
            if everyrow[COMPONENT] != 'ALL' and (everyrow[COMPONENT] not in baseInfo['Component V']):
                continue
            # 获取所有有可能的值
            nrowdict[nrow + 1] = everyrow
        self.log.logger_info('筛选后得到的Excel值为：{}'.format(nrowdict))
        setattr(DatasStor,'nrowdict',nrowdict)

    # # 获取月份值()
    # def getExcelMonthBySystem(self, CostFunding_ValueDict):  # 通过系统页面测试数据的月份值，筛选出满足条件的月份名
    #     """
    #      结果类型：monthDict_on_portfolioPage={'JUL.': 'MONTH0','AUG.':'MONTH1','SEP.':'MONTH2'}
    #     """
    #     monthDict_on_portfolioPage = {}
    #     # CostFunding_ValueDict=getattr(DatasStor,'CostFunding_ValueDict')
    #     for key in CostFunding_ValueDict.keys():
    #         currentMon = datetime.datetime.now().month
    #         if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
    #             continue
    #         if (monthsDict[key] - currentMon) < -2:
    #             monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - currentMon+12}'
    #         else:
    #             monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - currentMon}'
    #     # print('打印的monthDict_on_portfolioPage为:',monthDict_on_portfolioPage)
    #     setattr(DatasStor, 'monthDict_on_portfolioPage', monthDict_on_portfolioPage)

    #计算Excel表格中的数据，得到结果
    def excelDatas_count(self,CostFunding_ValueDict):

        excelMon0 = 0
        excelMon1 = 0
        excelMon2 = 0
        excelMons = {}

        month_excelMark_Dict={}#month_excelMark_Dict={'JUL.': 'MONTH0','AUG.':'MONTH1','SEP.':'MONTH2'}
        month_on_portfolioPage=[]
        for key in CostFunding_ValueDict.keys():
            currentMon = datetime.datetime.now().month
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
            month_on_portfolioPage.append(key)
            if (monthsDict[key] - currentMon) < -2:
                month_excelMark_Dict[key]=f'MONTH{monthsDict[key] - currentMon+12}'
            else:
                month_excelMark_Dict[key]=f'MONTH{monthsDict[key] - currentMon}'

        for value in getattr(DatasStor,'nrowdict').values():#nrowdict是Excel中筛选出来的数据
            excelMon0 += value[monthValues[month_excelMark_Dict[month_on_portfolioPage[0]]]]
            excelMon1 += value[monthValues[month_excelMark_Dict[month_on_portfolioPage[1]]]]
            excelMon2 += value[monthValues[month_excelMark_Dict[month_on_portfolioPage[2]]]]
        time.sleep(3)
        # 判断CostFunding_Value内的值为0,9999,99999则为无效
        i = 3
        for mon in month_excelMark_Dict.keys():
            if eval(CostFunding_ValueDict[mon]) == 0 or eval(CostFunding_ValueDict[mon])==9999 or eval(CostFunding_ValueDict[mon])==99999:
                i -= 1
        if i==0:
            i=1
        excelMons[month_on_portfolioPage[0]] = '%.2f' % excelMon0
        excelMons[month_on_portfolioPage[1]] = '%.2f' % excelMon1
        excelMons[month_on_portfolioPage[2]] = '%.2f' % excelMon2
        excelMons['CostFunding_value'] = '%.2f' % ((excelMon0 + excelMon1 + excelMon2) / i)
        print('Excel中满足条件的值进行相加得到的值为：{}'.format(excelMons))
        return excelMons

    #添加policyList数据
    def add_policyList_Datas(self,filename):
        doc='policyList页面-添加数据功能'
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lplp.ele_iframe))
        self.wait_eleVisible(lplp.ele_iframe,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lplp.ele_iframe))#进入iframe
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lplp.button_import))
        self.wait_eleVisible(lplp.button_import, doc=doc)
        self.driver.find_element(*lplp.button_import).click()#点击import按钮
        # WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(lplp.ele_iframe_export))
        self.wait_eleVisible(lplp.ele_iframe_export, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lplp.ele_iframe_export))#进入打开的弹窗界面的iframe

        #选择本地Excel文件，并上传
        self.driver.find_element(*lplp.button_File_Upload).send_keys(filename) # 点击选择文件按钮
        self.driver.find_element(*lplp.button_import_in_iframe).click()
        time.sleep(15)
        self.driver.switch_to.default_content()

