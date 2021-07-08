from Common.base_page import BasePage
from PageLocators.locators_GrossBMCCost import LocatorsGrossBMCCost as lgbc
import time

class PageGrossBMCCost(BasePage):
    def calculate_by_formula(self,portfolioNo,lineCode):
        doc='Gross BMC Cost ($)字段计算功能'
        self.wait_eleVisible(lgbc.ele_iframe,wait_times=50,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*lgbc.ele_iframe))
        self.wait_eleVisible(lgbc.input_portfolioNo,wait_times=50,doc=doc)
        self.input_text(lgbc.input_portfolioNo,portfolioNo,doc)# 在Portfolio No.输入框输入条件
        self.click_element(lgbc.button_search,doc)  # 点击搜索按钮
        time.sleep(1)
        self.wait_eleVisible(lgbc.list_results_portfolio,wait_times=10,doc=doc)  # 等待按照portfolio No.查询结束

        #获取搜索结果中的国家对应的GEO的值，用来判断GEO是否是EMEA
        countryName =self.get_text(lgbc.countryValue_on_portfolioList,doc)# 获取国家名称
        self.click_element(lgbc.input_country,doc)
        self.input_text(lgbc.input_country_in_list,countryName,doc)
        time.sleep(1)
        GEO=self.get_text(lgbc.ele_geo_in_list,doc)
        RegionName = self.get_text(lgbc.ele_region_in_list, doc)
        time.sleep(1)
        # 继续选择输入筛选条件，筛选portfolio信息
        self.click_element(lgbc.ele_portfolio,doc)  # 点击搜索结果中的Portfolio No.值
        self.wait_eleVisible(lgbc.ele_product_title_result,wait_times=15,doc=doc)
        #等待进入lineCode界面
        self.wait_eleVisible(lgbc.input_product_lineCode,doc=doc)
        self.input_text(lgbc.input_product_lineCode,lineCode,doc)  # 在linecode输入框输入条件
        time.sleep(3)
        eles_lineCode = self.get_elements(lgbc.eles_lineCode)

        # 双击符合条件的lineCode，进入portfolio详情界面
        for txt_lineCode in eles_lineCode:
            if txt_lineCode.text == lineCode:
                self.double_click_element(txt_lineCode,doc)
                break
        self.wait_eleVisible(lgbc.ele_load_img,doc=doc)  # 等待在portfolio界面出现遮罩层
        self.wait_eleVisible(lgbc.ele_country,doc=doc)#等待国家字段元素出现，证明页面加载完成
        Sales_mode=self.get_text(lgbc.ele_Sales_mode,doc)
        # 点击Calculate按钮
        time.sleep(2)
        self.wait_eleVisible(lgbc.button_Calculate,doc=doc)
        self.click_element(lgbc.button_Calculate, doc)
        # 等待元素出现
        self.wait_eleVisible(lgbc.ele_load_img, 300, doc=doc)
        self.wait_elePresence(lgbc.ele_load_img_disappear, 100, doc=doc)

        Value_CarryCase=float(self.get_element_attribute(lgbc.ele_CarryCase_Value,'value',doc).replace(',',''))
        Value_LineCode=float(self.get_element_attribute(lgbc.ele_LineCode_Value,'value',doc).replace(',',''))
        Value_Insurance=float(self.get_element_attribute(lgbc.ele_Insurance_Value,'value',doc).replace(',',''))
        Value_OEM=float(self.get_element_attribute(lgbc.ele_OEM_Value,'value',doc).replace(',',''))
        Value_Geo_real_cost=float(self.get_element_attribute(lgbc.ele_Geo_real_cost_Value,'value',doc).replace(',',''))
        Value_ThinkVisionImporterLabel=float(self.get_element_attribute(lgbc.ele_ThinkVisionImporterLabel_Value,'value',doc).replace(',',''))
        Value_LocalLogisticCost=float(self.get_element_attribute(lgbc.ele_LocalLogisticCost_Value,'value',doc).replace(',',''))

        FundingsDict={} #FundingsDict={'GEO_FundingMOU':[239.00,240.00,241.00]}
        #将所有元素放到字典中
        eles_FundingsDict = {}
        eles_FundingsDict['BMCCost']=lgbc.eles_BMCCost_Month
        eles_FundingsDict['FreightCost']=lgbc.eles_FreightCost_Month
        eles_FundingsDict['PNAssessment'] = lgbc.eles_PNAssessment_Month
        eles_FundingsDict['AggregateCustomDuty'] = lgbc.eles_AggregateCustomDuty_Month
        for FundingsName in eles_FundingsDict.keys():
            FundingsDict[FundingsName] = []
            #对每个字段三个月份的值进行获取
            eles_Fundings=self.get_elements(eles_FundingsDict[FundingsName])
            for ele_Funding_mon in eles_Fundings:
                Value_Funding_speci_mon=ele_Funding_mon.get_attribute('value')
                FundingsDict[FundingsName].append(float(Value_Funding_speci_mon.replace(',','')))
        if GEO=='AP':
            calculate_month1_Funding =FundingsDict['BMCCost'][0]+FundingsDict['FreightCost'][0]+Value_CarryCase+Value_LineCode+Value_Insurance+Value_OEM+Value_Geo_real_cost+Value_ThinkVisionImporterLabel+FundingsDict['AggregateCustomDuty'][0]+FundingsDict['PNAssessment'][0]
            calculate_month2_Funding = FundingsDict['BMCCost'][1] + FundingsDict['FreightCost'][1] + Value_CarryCase + Value_LineCode + Value_Insurance + Value_OEM + Value_Geo_real_cost + Value_ThinkVisionImporterLabel +FundingsDict['AggregateCustomDuty'][1] + FundingsDict['PNAssessment'][1]
            calculate_month3_Funding = FundingsDict['BMCCost'][2] + FundingsDict['FreightCost'][2] + Value_CarryCase + Value_LineCode + Value_Insurance + Value_OEM + Value_Geo_real_cost + Value_ThinkVisionImporterLabel +FundingsDict['AggregateCustomDuty'][2] + FundingsDict['PNAssessment'][2]
        elif RegionName=='LAS' and Sales_mode=='Onshore':
            calculate_month1_Funding=FundingsDict['BMCCost'][0]+FundingsDict['FreightCost'][0]+FundingsDict['AggregateCustomDuty'][0]+Value_LocalLogisticCost+FundingsDict['PNAssessment'][0]
            calculate_month2_Funding = FundingsDict['BMCCost'][1] + FundingsDict['FreightCost'][1] +FundingsDict['AggregateCustomDuty'][1] + Value_LocalLogisticCost +FundingsDict['PNAssessment'][1]
            calculate_month3_Funding = FundingsDict['BMCCost'][2] + FundingsDict['FreightCost'][2] +FundingsDict['AggregateCustomDuty'][2] + Value_LocalLogisticCost +FundingsDict['PNAssessment'][2]
        elif countryName=='Turkey':
            calculate_month1_Funding = FundingsDict['BMCCost'][0] + FundingsDict['FreightCost'][0] +FundingsDict['AggregateCustomDuty'][0]
            calculate_month2_Funding = FundingsDict['BMCCost'][1] + FundingsDict['FreightCost'][1] +FundingsDict['AggregateCustomDuty'][1]
            calculate_month3_Funding = FundingsDict['BMCCost'][2] + FundingsDict['FreightCost'][2] +FundingsDict['AggregateCustomDuty'][2]
        else:
            calculate_month1_Funding = FundingsDict['BMCCost'][0] + FundingsDict['FreightCost'][0] +FundingsDict['PNAssessment'][0]
            calculate_month2_Funding = FundingsDict['BMCCost'][1] + FundingsDict['FreightCost'][1] +FundingsDict['PNAssessment'][1]
            calculate_month3_Funding = FundingsDict['BMCCost'][2] + FundingsDict['FreightCost'][2] +FundingsDict['PNAssessment'][2]

        calculate_GrossBMCCostValueDict = {}
        i = 3
        if calculate_month1_Funding == 0 or calculate_month1_Funding>= 99999:
            i -= 1
            calculate_month1_Funding = 0
            calculate_GrossBMCCostValueDict['month1_GrossBMCCost'] = '%.2f' % 99999
        else:
            calculate_GrossBMCCostValueDict['month1_GrossBMCCost'] = '%.2f' % calculate_month1_Funding
        if calculate_month2_Funding == 0 or calculate_month2_Funding>= 99999:
            i -= 1
            calculate_month2_Funding = 0
            calculate_GrossBMCCostValueDict['month2_GrossBMCCost'] = '%.2f' % 99999
        else:
            calculate_GrossBMCCostValueDict['month2_GrossBMCCost'] = '%.2f' % calculate_month2_Funding
        if calculate_month3_Funding == 0 or calculate_month3_Funding>= 99999:
            i -= 1
            calculate_month3_Funding = 0
            calculate_GrossBMCCostValueDict['month3_GrossBMCCost'] = '%.2f' % 99999
        else:
            calculate_GrossBMCCostValueDict['month3_GrossBMCCost'] = '%.2f' % calculate_month3_Funding
        if i == 0:
            i = 1
        calculate_GrossBMCCostValueDict['avg_GrossBMCCost']='%.2f'%((calculate_month1_Funding+calculate_month2_Funding+calculate_month3_Funding)/i)

        return calculate_GrossBMCCostValueDict

    def get_pageValue_GrossBMCCost(self):
        doc='获取Gross BMC Cost ($)的值'
        GrossBMCCostDict={}
        self.wait_eleVisible(lgbc.ele_avg_GrossBMCCost)

        data_avg_GrossBMCCost = self.get_element_attribute(lgbc.ele_avg_GrossBMCCost, 'value', doc)
        GrossBMCCostDict['avg_GrossBMCCost'] = data_avg_GrossBMCCost.replace(',', '')

        data_month1_GrossBMCCost=self.get_elements(lgbc.eles_GrossBMCCost_Month)[0].get_attribute('value')
        data_month2_GrossBMCCost = self.get_elements(lgbc.eles_GrossBMCCost_Month)[1].get_attribute('value')
        data_month3_GrossBMCCost = self.get_elements(lgbc.eles_GrossBMCCost_Month)[2].get_attribute('value')
        GrossBMCCostDict['month1_GrossBMCCost']=data_month1_GrossBMCCost.replace(',','')
        GrossBMCCostDict['month2_GrossBMCCost'] = data_month2_GrossBMCCost.replace(',','')
        GrossBMCCostDict['month3_GrossBMCCost'] = data_month3_GrossBMCCost.replace(',','')

        return GrossBMCCostDict
