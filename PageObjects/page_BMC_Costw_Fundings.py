from Common.base_page import BasePage
from PageLocators.locators_BMC_Cost_w_Fundings import LocatorsBMCCostWFundings as lbcf
import time

class PageBMCCostWFundings(BasePage):
    def calculate_BMC_Cost_w_Fundings(self,portfolioNo,lineCode):
        doc='BMC Cost w/ Fundings($)字段计算'
        self.wait_eleVisible(lbcf.ele_iframe,wait_times=50,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lbcf.ele_iframe))
        self.wait_eleVisible(lbcf.input_portfolioNo,wait_times=50,doc=doc)
        self.input_text(lbcf.input_portfolioNo,portfolioNo,doc)# 在Portfolio No.输入框输入条件
        self.click_element(lbcf.button_search,doc)  # 点击搜索按钮
        time.sleep(2)
        self.wait_eleVisible(lbcf.list_results_portfolio,wait_times=10,doc=doc)  # 等待按照portfolio No.查询结束

        # 继续选择输入筛选条件，筛选portfolio信息
        self.click_element(lbcf.ele_portfolio,doc)  # 点击搜索结果中的Portfolio No.值
        self.wait_eleVisible(lbcf.ele_product_title_result,wait_times=15,doc=doc)
        #等待进入lineCode界面
        self.wait_eleVisible(lbcf.input_product_lineCode,doc=doc)
        self.input_text(lbcf.input_product_lineCode,lineCode,doc)  # 在linecode输入框输入条件
        time.sleep(3)
        eles_lineCode = self.get_elements(lbcf.eles_lineCode)

        # 双击符合条件的lineCode，进入portfolio详情界面
        for txt_lineCode in eles_lineCode:
            if txt_lineCode.text == lineCode:
                self.double_click_element(txt_lineCode,doc)
                break

        time.sleep(2)

        self.wait_eleVisible(lbcf.ele_country, wait_times=100, doc=doc)#等待国家字段元素出现，证明页面加载完成
        time.sleep(2)
        # 点击Calculate按钮
        self.wait_eleVisible(lbcf.button_Calculate,doc=doc)
        self.click_element(lbcf.button_Calculate, doc)
        # 等待元素出现
        self.wait_eleVisible(lbcf.ele_load_img, 300, doc=doc)
        self.wait_elePresence(lbcf.ele_load_img_disappear, 100, doc=doc)

        BMCFundingsDict={} #BMCFundingsDict={'BMC_Cost':[239.00,240.00,241.00],'UnitFunding':[239.00,240.00,241.00]}
        #将所有元素放到字典中
        eles_BMCFundingsDict = {}
        eles_BMCFundingsDict['BMC_Cost']=lbcf.eles_BMC_Cost_Month
        eles_BMCFundingsDict['UnitFunding']=lbcf.eles_UnitFunding_Month

        for FundingsName in eles_BMCFundingsDict.keys():
            BMCFundingsDict[FundingsName] = []
            #对每个字段三个月份的值进行获取
            eles_Fundings=self.get_elements(eles_BMCFundingsDict[FundingsName])
            for ele_Funding_mon in eles_Fundings:
                Value_Funding_speci_mon=ele_Funding_mon.get_attribute('value')
                BMCFundingsDict[FundingsName].append(float(Value_Funding_speci_mon.replace(',','')))

        sum_BMCFundingsValueDict = {}  # sum_FundingValues={'sum_FundingsValue':[611.20,561.74,611.20,660.66]}
        # 计算后第一个月的结果
        if BMCFundingsDict['BMC_Cost'][0]==99999:
            sum_BMCFundingsValueDict['sum_month1_BMCFunding'] = '%.2f' % 99999
            sum_month1_BMCFunding=0
        else:
            sum_month1_BMCFunding = BMCFundingsDict['BMC_Cost'][0] - BMCFundingsDict['UnitFunding'][0]
            sum_BMCFundingsValueDict['sum_month1_BMCFunding'] = '%.2f' % sum_month1_BMCFunding
        # 计算后第二个月的结果
        if BMCFundingsDict['BMC_Cost'][1]==99999:
            sum_BMCFundingsValueDict['sum_month2_BMCFunding'] =  '%.2f' % 99999
            sum_month2_BMCFunding = 0
        else:
            sum_month2_BMCFunding = BMCFundingsDict['BMC_Cost'][1] - BMCFundingsDict['UnitFunding'][1]
            sum_BMCFundingsValueDict['sum_month2_BMCFunding'] = '%.2f' % sum_month2_BMCFunding

        # 计算后第三个月的结果
        if BMCFundingsDict['BMC_Cost'][2]==  99999:
            sum_BMCFundingsValueDict['sum_month3_BMCFunding'] = '%.2f' % 99999
            sum_month3_BMCFunding = 0
        else:
            sum_month3_BMCFunding=BMCFundingsDict['BMC_Cost'][2]-BMCFundingsDict['UnitFunding'][2]
            sum_BMCFundingsValueDict['sum_month3_BMCFunding'] = '%.2f' % sum_month3_BMCFunding
        i=3
        if sum_month1_BMCFunding == 0 or sum_month1_BMCFunding==9999 or sum_month1_BMCFunding==99999:
                i -= 1
        if sum_month2_BMCFunding == 0 or sum_month2_BMCFunding==9999 or sum_month2_BMCFunding==99999:
                i -= 1
        if sum_month3_BMCFunding == 0 or sum_month3_BMCFunding==9999 or sum_month3_BMCFunding==99999:
                i -= 1
        if i==0:
            i=1
        sum_BMCFundingsValueDict['sum_avg_BMCFunding']='%.2f' %((sum_month1_BMCFunding+sum_month2_BMCFunding+sum_month3_BMCFunding)/i)

        self.log.logger_info(BMCFundingsDict)
        return sum_BMCFundingsValueDict

    def get_dict_BMCFunding(self):
        doc='获取BMC Cost w/ Fundings($)的值'
        BMCFundingDict={}
        self.wait_eleVisible(lbcf.ele_avg_BMC_Cost_w_Fundings)
        data_avg_BMCFunding=self.get_element_attribute(lbcf.ele_avg_BMC_Cost_w_Fundings,'value',doc)
        BMCFundingDict['sum_avg_BMCFunding']=data_avg_BMCFunding.replace(',','')
        data_month1_BMCFunding=self.get_elements(lbcf.eles_BMC_Cost_w_Fundings_Month)[0].get_attribute('value')
        data_month2_BMCFunding = self.get_elements(lbcf.eles_BMC_Cost_w_Fundings_Month)[1].get_attribute('value')
        data_month3_BMCFunding = self.get_elements(lbcf.eles_BMC_Cost_w_Fundings_Month)[2].get_attribute('value')
        BMCFundingDict['sum_month1_BMCFunding']=data_month1_BMCFunding.replace(',','')
        BMCFundingDict['sum_month2_BMCFunding'] = data_month2_BMCFunding.replace(',','')
        BMCFundingDict['sum_month3_BMCFunding'] = data_month3_BMCFunding.replace(',','')
        return BMCFundingDict
