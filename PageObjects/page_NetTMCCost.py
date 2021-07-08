from Common.base_page import BasePage
from PageLocators.locators_NetTMCCost import LocatorsNetTMCCost as lntc
import time

class PageNetTMCCost(BasePage):
    def calculate_by_formula(self,portfolioNo,lineCode):
        doc='Net TMC Cost ($)字段计算'
        self.wait_eleVisible(lntc.ele_iframe,wait_times=50,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lntc.ele_iframe))
        self.wait_eleVisible(lntc.input_portfolioNo,wait_times=50,doc=doc)
        self.input_text(lntc.input_portfolioNo,portfolioNo,doc)# 在Portfolio No.输入框输入条件
        self.click_element(lntc.button_search,doc)  # 点击搜索按钮
        time.sleep(1)
        self.wait_eleVisible(lntc.list_results_portfolio,wait_times=10,doc=doc)  # 等待按照portfolio No.查询结束

        # 继续选择输入筛选条件，筛选portfolio信息
        self.click_element(lntc.ele_portfolio,doc)  # 点击搜索结果中的Portfolio No.值
        self.wait_eleVisible(lntc.ele_product_title_result,wait_times=20,doc=doc)
        #等待进入lineCode界面
        self.wait_eleVisible(lntc.input_product_lineCode,doc=doc)
        self.input_text(lntc.input_product_lineCode,lineCode,doc)  # 在linecode输入框输入条件
        time.sleep(3)
        eles_lineCode = self.get_elements(lntc.eles_lineCode)

        # 双击符合条件的lineCode，进入portfolio详情界面
        for txt_lineCode in eles_lineCode:
            if txt_lineCode.text == lineCode:
                self.double_click_element(txt_lineCode,doc)
                break
        # time.sleep(1)

        self.wait_eleVisible(lntc.ele_load_img)#等待在portfolio界面出现遮罩层
        self.wait_eleVisible(lntc.ele_country, wait_times=300, doc=doc)#等待国家字段元素出现，证明页面加载完成
        time.sleep(2)
        # 点击Calculate按钮
        self.wait_eleVisible(lntc.button_Calculate,doc=doc)
        self.click_element(lntc.button_Calculate, doc)
        # 等待元素出现
        self.wait_eleVisible(lntc.ele_load_img, 300, doc=doc)
        self.wait_elePresence(lntc.ele_load_img_disappear, 100, doc=doc)

        CostFundingsDict={} #CostFundingsDict={'non-BMC Uplift (%)':[239.00,240.00,241.00],'UnitFunding':[239.00,240.00,241.00]}
        #将所有元素放到字典中
        eles_CostFundingsDict = {}
        eles_CostFundingsDict['Net_BMC_Cost']=lntc.eles_Net_BMC_Cost_Month
        eles_CostFundingsDict['non_BMC_Uplift']=lntc.eles_non_BMC_Uplift_Month
        eles_CostFundingsDict['CountryAdjustment1']=lntc.eles_CountryAdjustment1_Month
        eles_CostFundingsDict['CountryAdjustment2']=lntc.eles_CountryAdjustment2_Month
        eles_CostFundingsDict['WarrantyCost']=lntc.eles_WarrantyCost_Month
        eles_CostFundingsDict['ADP']=lntc.eles_ADP_Month
        eles_CostFundingsDict['Geo_real_cost']=lntc.eles_Geo_real_cost_Month

        for FundingsName in eles_CostFundingsDict.keys():
            CostFundingsDict[FundingsName] = []
            #对每个字段三个月份的值进行获取
            eles_Fundings=self.get_elements(eles_CostFundingsDict[FundingsName])
            for ele_Funding_mon in eles_Fundings:
                Value_Funding_speci_mon=ele_Funding_mon.get_attribute('value')
                CostFundingsDict[FundingsName].append(float(Value_Funding_speci_mon.replace(',','')))

        calculate_NetTMCCost_Dict = {}  # calculate_NetTMCCost_Dict={'sum_FundingsValue':[611.20,561.74,611.20,660.66]}
        # 计算后第一个月的结果=Net BMC Cost ($) M1*（1+non-BMC Uplift (%)+Country Adjustment (%)）+Country Adjustment ($) M1+Warranty Cost($) M1+ADP($)+Geo real cost (TMC Adder) M1
        if CostFundingsDict['Net_BMC_Cost'][0]==99999:
            calculate_NetTMCCost_Dict['month1_NetTMCCost'] = '%.2f' % 99999
            month1_NetTMCCost=0
        else:
            month1_NetTMCCost = CostFundingsDict['Net_BMC_Cost'][0]*(1+CostFundingsDict['non_BMC_Uplift'][0]+CostFundingsDict['CountryAdjustment1'][0])+CostFundingsDict['CountryAdjustment2'][0]+CostFundingsDict['WarrantyCost'][0]+CostFundingsDict['ADP'][0]+CostFundingsDict['Geo_real_cost'][0]
            calculate_NetTMCCost_Dict['month1_NetTMCCost'] = '%.2f' % month1_NetTMCCost
        # 计算后第二个月的结果
        if CostFundingsDict['Net_BMC_Cost'][1]==99999:
            calculate_NetTMCCost_Dict['month2_NetTMCCost'] = '%.2f' % 99999
            month2_NetTMCCost=0
        else:
            month2_NetTMCCost = CostFundingsDict['Net_BMC_Cost'][1]*(1+CostFundingsDict['non_BMC_Uplift'][1]+CostFundingsDict['CountryAdjustment1'][1])+CostFundingsDict['CountryAdjustment2'][1]+CostFundingsDict['WarrantyCost'][1]+CostFundingsDict['ADP'][1]+CostFundingsDict['Geo_real_cost'][1]
            calculate_NetTMCCost_Dict['month2_NetTMCCost'] = '%.2f' % month2_NetTMCCost
        # 计算后第三个月的结果
        if CostFundingsDict['Net_BMC_Cost'][2]==99999:
            calculate_NetTMCCost_Dict['month3_NetTMCCost'] = '%.2f' % 99999
            month3_NetTMCCost=0
        else:
            month3_NetTMCCost = CostFundingsDict['Net_BMC_Cost'][2] * (1 + CostFundingsDict['non_BMC_Uplift'][2] + CostFundingsDict['CountryAdjustment1'][2]) +CostFundingsDict['CountryAdjustment2'][2] +CostFundingsDict['WarrantyCost'][2] + CostFundingsDict['ADP'][2] +CostFundingsDict['Geo_real_cost'][2]
            calculate_NetTMCCost_Dict['month3_NetTMCCost'] = '%.2f' % month3_NetTMCCost

        i=3
        if month1_NetTMCCost == 0 or month1_NetTMCCost==9999 or month1_NetTMCCost==99999:
                i -= 1
        elif month2_NetTMCCost == 0 or month2_NetTMCCost==9999 or month2_NetTMCCost==99999:
                i -= 1
        elif month3_NetTMCCost== 0 or month3_NetTMCCost==9999 or month3_NetTMCCost==99999:
                i -= 1
        if i==0:
            i=1
        calculate_NetTMCCost_Dict['avg_NetTMCCost']='%.2f' %((month1_NetTMCCost+month2_NetTMCCost+month3_NetTMCCost)/i)

        self.log.logger_info(f'calculate_NetTMCCost_Dict的值是：{calculate_NetTMCCost_Dict}')
        return calculate_NetTMCCost_Dict

    def get_pageValue_NetTMCCost(self):
        doc='获取Net TMC Cost ($)的值'
        NetTMCCostDict={}
        self.wait_eleVisible(lntc.ele_avg_Net_TMC_Cost)
        data_avg_BMCFunding=self.get_element_attribute(lntc.ele_avg_Net_TMC_Cost,'value',doc)
        NetTMCCostDict['avg_NetTMCCost']=data_avg_BMCFunding.replace(',','')
        data_month1_BMCFunding=self.get_elements(lntc.eles_Net_TMC_Cost_Month)[0].get_attribute('value')
        data_month2_BMCFunding = self.get_elements(lntc.eles_Net_TMC_Cost_Month)[1].get_attribute('value')
        data_month3_BMCFunding = self.get_elements(lntc.eles_Net_TMC_Cost_Month)[2].get_attribute('value')
        NetTMCCostDict['month1_NetTMCCost']=data_month1_BMCFunding.replace(',','')
        NetTMCCostDict['month2_NetTMCCost'] = data_month2_BMCFunding.replace(',','')
        NetTMCCostDict['month3_NetTMCCost'] = data_month3_BMCFunding.replace(',','')
        return NetTMCCostDict
