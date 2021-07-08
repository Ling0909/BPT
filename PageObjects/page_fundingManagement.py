from selenium.webdriver.support.ui import Select
from Common.base_page import BasePage
from PageLocators.locators_fundingManagementPage import LocatorsFundingManagementPage as lfmp
from Common.datas_stor import DatasStor
import xlrd
from Common.parameters.parameter_fundingManagement import *
import time
from Common.do_database import DoMysql
import datetime

class PageFundingManagement(BasePage):
    # 下载policy list
    def download_policyTemplate(self, policyType):
        doc='FundingManagement页面，下载Excel文件功能'
        self.driver.switch_to.frame(self.driver.find_element(*lfmp.ele_iframe))
        self.wait_eleVisible(lfmp.select_policyType, doc=doc)
        select_policyType=self.driver.find_element(*lfmp.select_policyType)
        Select(select_policyType).select_by_value(policyType)  # 选择policyType值
        time.sleep(2)
        self.driver.find_element(*lfmp.button_search).click()
        self.wait_eleVisible(lfmp.load_ok, doc=doc)
        time.sleep(2)
        self.driver.find_element(*lfmp.button_downLoad).click()#点击下载按钮
        # time.sleep(3)

    # 从下载的Excel中筛选数据，得到字典
    def get_bestDatas(self):
        # (依赖：1、Excel已下载；2、已经在portfolio界面获取了baseInfo信息）
        filename=self.get_latest_fileName()
        print('要打开的的Excel文件名字为：{}'.format(filename))
        # self.log.logger_info('要打开的的Excel文件名字为：{}'.format(filename))
        book=xlrd.open_workbook(filename)
        # 获取第一张sheet表单
        sh=book.sheets()[0]
        nrowdict={}
        nrowdict0={}
        nrowdict1={}
        nrowdict2={}
        baseInfo=getattr(DatasStor, 'baseInfo')
        for nrow in range(2, sh.nrows):
            everyrow=sh.row_values(nrow)
            if everyrow[PRODUCT_GROUP]!=baseInfo['PRODUCT_GROUP']:
                continue
            # if everyrow[BRAND] not in baseInfo['PRODUCT_CATEGORY']:
            #     continue
            if everyrow[CHARACTER_VALUE]!='ALL' and everyrow[CHARACTER_VALUE] not in baseInfo['Component V']:
                continue

            if everyrow[PRODUCT_FAMILY] != '': #首先判断product_family有值的情况
                if everyrow[PRODUCT_FAMILY]!=baseInfo['PRODUCT_FAMILY']: #与baseinfo里面的值相等就放到字典里
                    continue
                nrowdict0[nrow+1]=everyrow
            else:#判断product_family没有值的情况
                if everyrow[PRODUCT_SERIES]!='':#判断product_series有值的情况
                    if everyrow[PRODUCT_SERIES]!=baseInfo['PRODUCT_SERIES']:#与baseinfo里面的值相等就放到字典里
                        continue
                    nrowdict1[nrow + 1] = everyrow
                else:#判断product_series没有值的情况
                    nrowdict2[nrow + 1] = everyrow

            """
            if everyrow[PRODUCT_SERIES]!='' and everyrow[PRODUCT_SERIES]!=baseInfo['PRODUCT_SERIES']:
                continue
            nrowdict0[nrow+1]=everyrow

            if everyrow[PRODUCT_SERIES]!=baseInfo['PRODUCT_SERIES']:
                    continue
            if everyrow[PRODUCT_FAMILY]!='' and everyrow[PRODUCT_FAMILY]!=baseInfo['PRODUCT_FAMILY']:
                    continue
            nrowdict1[nrow+1]=everyrow

            if everyrow[PRODUCT_FAMILY]!=baseInfo['PRODUCT_FAMILY']:
                        continue
            nrowdict2[nrow+1]=everyrow
        if len(nrowdict0)==1:
            nrowdict=nrowdict0

        elif len(nrowdict1)==1:
            nrowdict=nrowdict1

        else:
            nrowdict=nrowdict2

            # # 获取所有有可能的值
            # nrowdict[nrow+1]=everyrow
        self.log.logger_info('筛选后得到的Excel值为：{}'.format(nrowdict))
        setattr(DatasStor, 'nrowdict', nrowdict)
        """
        if len(nrowdict0) !=0:#判断不为空就选它
            nrowdict = nrowdict0

        elif len(nrowdict1)!=0:
            nrowdict = nrowdict1

        else:
            nrowdict = nrowdict2

            # # 获取所有有可能的值
            # nrowdict[nrow+1]=everyrow
        self.log.logger_info('筛选后得到的Excel值为：{}'.format(nrowdict))
        setattr(DatasStor, 'nrowdict', nrowdict)

        # 获取月份值()
    def getExcelMonthBySystem(self, CostFunding_ValueDict):  # 通过系统页面测试数据的月份值，筛选出满足条件的月份名
        """
         结果类型：monthDict_on_portfolioPage={'JUL.': 0,'AUG.': 1,'SEP.':2}
        """
        monthDict_on_portfolioPage = {}
        # CostFunding_ValueDict=getattr(DatasStor,'CostFunding_ValueDict')
        for key in CostFunding_ValueDict.keys():
            CurrentMon = datetime.datetime.now().month
            CurrentYear = str(datetime.datetime.now().year)#CurrentYear='2019'
            Plan_Cycle=getattr(DatasStor,'Plan_Cycle')#Plan_Cycle='FY19/20Q2'
            if key not in [one for one in monthsDict.keys()]:  # CostFunding_ValueDict中不是月份的GEO Funding(Others) 1 ($)去掉
                continue
            if eval(Plan_Cycle[2:4])-eval(CurrentYear[2:4])==1:
                if (monthsDict[key] - CurrentMon) <0:
                    monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - CurrentMon+12}'
                else:
                    monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - CurrentMon}'
            elif eval(Plan_Cycle[2:4])-eval(CurrentYear[2:4])==0:
                if (monthsDict[key] - CurrentMon) <-2:
                    monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - CurrentMon+12}'
                else:
                    monthDict_on_portfolioPage[key] = f'MONTH{monthsDict[key] - CurrentMon}'
        print('打印的monthDict_on_portfolioPage为:',monthDict_on_portfolioPage)
        setattr(DatasStor, 'monthDict_on_portfolioPage', monthDict_on_portfolioPage)

    # 计算Excel表格中的数据，得到结果
    def excelDatas_count(self,CostFunding_Value):


        excelMon0=0
        excelMon1=0
        excelMon2=0
        excelMons={}
        month=getattr(DatasStor, 'monthDict_on_portfolioPage')
        # {'SEPT.': 'MONTH2', 'OCT.': 'MONTH3', 'NOV.': 'MONTH4'}
        monthkey=[]
        for key in month.keys():
            monthkey.append(key)  # ['SEPT.', 'OCT.', 'NOV.']

        for value in getattr(DatasStor, 'nrowdict').values():  # nrowdict是Excel中筛选出来的数据
            DataInBase0 = 0#存放数据库内查出的month-1的数据
            DataInBase1 = 0#存放数据库内查出的month-2的数据
            #product_family和product_series都为空
            query_sql1 = "SELECT BP_PreMonthOne,BP_PreMonthTwo FROM	BT_Policy_Funding WHERE BP_ProductSeries = ''AND BP_ProductFamily =''AND BP_Component='{}';".format(value[CHARACTER_VALUE])
            # 只有product_family为空
            query_sql2 = "SELECT BP_PreMonthOne,BP_PreMonthTwo FROM BT_Policy_Funding WHERE BP_ProductSeries=(select BPH_GUID FROM BS_ProductHierarchy WHERE BPH_Name='{}') AND BP_ProductFamily='' AND BP_Component='{}';".format(value[PRODUCT_SERIES], value[CHARACTER_VALUE])
            # product_family和product_series都不为空
            query_sql3 = "SELECT BP_PreMonthOne,BP_PreMonthTwo FROM	BT_Policy_Funding WHERE BP_ProductSeries = (select BPH_GUID FROM BS_ProductHierarchy WHERE BPH_Name='{}') AND BP_ProductFamily =(select Bs_Guid from BS_ProductFamily WHERE BS_Name='{}') AND BP_Component='{}';".format(value[PRODUCT_SERIES], value[PRODUCT_FAMILY], value[CHARACTER_VALUE])
            if month[monthkey[0]]=='MONTH-1':#如果日期表中存在MONTH-1的数据
                if value[PRODUCT_FAMILY]=='' and value[PRODUCT_SERIES]=='':#product_family和product_series都为空
                    """
                    因为product_family和product_series是否为空，查询语句不同，所以需要分情况来判断
                    """
                    DataInBase0=DoMysql().do_mysql(query_sql1)[0][0]#通过数据库查询出第一条数据来
                elif value[PRODUCT_FAMILY]=='' and value[PRODUCT_SERIES]!='':#只有product_family为空

                    DataInBase0 = DoMysql().do_mysql(query_sql2)[0][0]
                elif value[PRODUCT_FAMILY]!='' and value[PRODUCT_SERIES]!='':#product_family和product_series都不为空
                    DataInBase0 = DoMysql().do_mysql(query_sql3)[0][0]
                if DataInBase0==None:
                    DataInBase0=0
                excelMon0+=DataInBase0
                excelMon1 += eval(value[monthValues[month[monthkey[1]]]])
            elif month[monthkey[0]]=='MONTH-2':#如果第一条数据是MONTH-2,那么第二条数据就是MONTH-1
                if value[PRODUCT_FAMILY]=='' and value[PRODUCT_SERIES]=='':
                    DataInBase0 = DoMysql().do_mysql(query_sql1)[0][0]
                    DataInBase1 = DoMysql().do_mysql(query_sql1)[0][1]
                elif value[PRODUCT_FAMILY]=='' and value[PRODUCT_SERIES]!='':
                    DataInBase0 = DoMysql().do_mysql(query_sql2)[0][0]
                    DataInBase1 = DoMysql().do_mysql(query_sql2)[0][1]
                elif value[PRODUCT_FAMILY]!='' and value[PRODUCT_SERIES]!='':
                    DataInBase0 =DoMysql().do_mysql(query_sql3)[0][0]
                    DataInBase1 = DoMysql().do_mysql(query_sql3)[0][1]
                if DataInBase0==None:
                    DataInBase0=0
                if DataInBase1==None:
                    DataInBase1=0
                excelMon0+=DataInBase0
                excelMon1 += DataInBase1
            else:#不存在本季度所有月份为MONTH-1或者MONTH-2的情况
                excelMon0+=eval(value[monthValues[month[monthkey[0]]]])
                excelMon1 += eval(value[monthValues[month[monthkey[1]]]])
            excelMon2+=eval(value[monthValues[month[monthkey[2]]]])
        time.sleep(2)
        #判断CostFunding_Value内的值为0,9999,99999则为无效
        i=3
        for mon in month.keys():
            if eval(CostFunding_Value[mon])==0 or eval(CostFunding_Value[mon])==9999 or eval(CostFunding_Value[mon])==99999:
                i-=1
        if i==0:
            i=1

        print(excelMon0,excelMon1,excelMon2)
        excelMons[monthkey[0]]='%.2f' % excelMon0
        excelMons[monthkey[1]]='%.2f' % excelMon1
        excelMons[monthkey[2]]='%.2f' % excelMon2
        excelMons['CostFunding_value']='%.2f' % ((float(excelMon0)+float(excelMon1)+float(excelMon2)) / i)
        print('Excel中满足条件的值进行相加得到的值为：{}'.format(excelMons))
        time.sleep(3)
        return excelMons

    # 添加policyList数据
    def add_fundingManagement_Datas(self, filename):
        doc='policyList页面-添加数据功能'
        self.wait_eleVisible(lfmp.ele_iframe, doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lfmp.ele_iframe))  # 进入iframe
        self.wait_eleVisible(lfmp.select_policyType, doc=doc)
        self.driver.find_element(*lfmp.input_upLoadFile).send_keys(filename)  # 在文件上传框中直接输入文件绝对路径
        self.wait_eleVisible(lfmp.button_upLoad,doc=doc)
        self.driver.find_element(*lfmp.button_upLoad).click()
        time.sleep(15)
        alert=self.driver.switch_to_alert()
        alert.accept()
        time.sleep(3)
        if self.is_eleExist(lfmp.ele_iframe_upload,doc=doc):
            self.driver.switch_to.frame(self.driver.find_element(*lfmp.ele_iframe_upload))
            self.driver.find_element(*lfmp.button_close_in_iframe).click()
        self.driver.switch_to.default_content()