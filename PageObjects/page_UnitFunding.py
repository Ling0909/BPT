from Common.base_page import BasePage
from PageLocators.locators_UnitFunding import LocatorsUnitFunding as luf
from selenium.webdriver.common.action_chains import ActionChains
import time

class PageUnitFunding(BasePage):
    def calculate_UnitFunding(self,portfolioNo,lineCode):
        doc='Unit Funding ($)字段计算功能'
        self.wait_eleVisible(luf.ele_iframe,wait_times=50,doc=doc)
        self.driver.switch_to.frame(self.driver.find_element(*luf.ele_iframe))
        self.wait_eleVisible(luf.input_portfolioNo,wait_times=50,doc=doc)
        self.input_text(luf.input_portfolioNo,portfolioNo,doc)# 在Portfolio No.输入框输入条件
        self.click_element(luf.button_search,doc)  # 点击搜索按钮
        time.sleep(1)
        self.wait_eleVisible(luf.list_results_portfolio,wait_times=10,doc=doc)  # 等待按照portfolio No.查询结束

        #获取搜索结果中的国家对应的GEO的值，用来判断GEO是否是EMEA
        countryName =self.get_text(luf.countryValue_on_portfolioList,doc)# 获取国家名称
        self.click_element(luf.input_country,doc)
        self.input_text(luf.input_country_in_list,countryName,doc)
        time.sleep(1)
        GEO=self.get_text(luf.ele_geo_in_list,doc)
        time.sleep(1)
        # 继续选择输入筛选条件，筛选portfolio信息
        self.click_element(luf.ele_portfolio,doc)  # 点击搜索结果中的Portfolio No.值
        self.wait_eleVisible(luf.ele_product_title_result,wait_times=15,doc=doc)
        # if self.get_text(luf.ele_title_secondLine) == 'Line Code':
        # 如果有lineCode值，执行以下逻辑
        self.wait_eleVisible(luf.input_product_lineCode,doc=doc)
        self.input_text(luf.input_product_lineCode,lineCode,doc)  # 在linecode输入框输入条件
        time.sleep(3)
        eles_lineCode = self.get_elements(luf.eles_lineCode)

        # 鼠标操作
        ac = ActionChains(self.driver)
        for txt_lineCode in eles_lineCode:
            if txt_lineCode.text == lineCode:
                ac.double_click(txt_lineCode).perform()
                break
        time.sleep(2)
        self.wait_eleVisible(luf.ele_country, wait_times=100, doc=doc)#等待国家字段元素出现，证明页面加载完成
        # 点击Calculate按钮
        time.sleep(1)
        self.wait_eleVisible(luf.button_Calculate,doc=doc)
        self.click_element(luf.button_Calculate, doc)
        # 等待元素出现
        self.wait_eleVisible(luf.ele_load_img, 300, doc=doc)
        self.wait_elePresence(luf.ele_load_img_disappear, 100, doc=doc)

        FundingsDict={} #FundingsDict={'GEO_FundingMOU':[240.00,239.00,240.00,241.00]}
        #获取Special Funding($)的值，放到字典中
        ele_SpecialFunding=self.get_element(luf.ele_Special_Funding,doc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",ele_SpecialFunding)
        time.sleep(2)
        Value_Special_Funding= self.get_element_attribute(luf.ele_Special_Funding,'value',doc)
        FundingsDict['Special_Funding']=[]
        FundingsDict['Special_Funding'].append(float(Value_Special_Funding.replace(',','')))
        FundingsDict['Special_Funding'].append(float(Value_Special_Funding.replace(',','')))
        FundingsDict['Special_Funding'].append(float(Value_Special_Funding.replace(',','')))
        # 为了与其他funding的值保持一致，需要添加四次值，FundingsDict={'Special_Funding':[240.00,240.00,240.00]}

        #将所有元素放到字典中
        eles_FundingsDict = {}
        if GEO == 'EMEA' or GEO=='AP':
            eles_FundingsDict['GEO_FundingMOU']=luf.eles_GEO_FundingMOU_Month
            eles_FundingsDict['GEO_FundingOthers1']=luf.eles_GEO_FundingOthers1_Month
            eles_FundingsDict['GEO_FundingOthers2'] = luf.eles_GEO_FundingOthers2_Month
            eles_FundingsDict['GEO_FundingOthers3'] = luf.eles_GEO_FundingOthers3_Month
            eles_FundingsDict['GEO_FundingOthers4'] = luf.eles_GEO_FundingOthers4_Month
            eles_FundingsDict['Funding1_CPU'] = luf.eles_Funding1_CPU_Month
            eles_FundingsDict['Funding2_HDD_SSHD_SSD'] = luf.eles_Funding2_HDD_SSHD_SSD_Month
            eles_FundingsDict['Funding3_Others'] = luf.eles_Funding3_Others_Month
            eles_FundingsDict['WW_Funding'] = luf.eles_WW_Funding_Month
            eles_FundingsDict['SegmentFunding'] = luf.eles_SegmentFunding_Month
        elif (GEO == 'LA' or GEO=='NA') and countryName!='Brazil':
            eles_FundingsDict['GEO_FundingMOU'] = luf.eles_GEO_FundingMOU_Month
            eles_FundingsDict['GEO_FundingOthers1'] = luf.eles_GEO_FundingOthers1_Month
            eles_FundingsDict['Funding1_CPU'] = luf.eles_Funding1_CPU_Month
            eles_FundingsDict['Funding2_HDD_SSHD_SSD'] = luf.eles_Funding2_HDD_SSHD_SSD_Month
            eles_FundingsDict['Funding3_Others'] = luf.eles_Funding3_Others_Month
            eles_FundingsDict['WW_Funding'] = luf.eles_WW_Funding_Month
            eles_FundingsDict['SegmentFunding'] = luf.eles_SegmentFunding_Month
        elif countryName=='Brazil':
            eles_FundingsDict['GEO_FundingMOU'] = luf.eles_GEO_FundingMOU_Month
            eles_FundingsDict['GEO_FundingOthers_Brazil'] =luf.eles_GEO_FundingOthers_Brazil_Month
            eles_FundingsDict['Funding1_CPU'] = luf.eles_Funding1_CPU_Month
            eles_FundingsDict['Funding2_HDD_SSHD_SSD'] =luf.eles_Funding2_HDD_SSHD_SSD_Month
            eles_FundingsDict['Funding3_Others'] =luf.eles_Funding3_Others_Month
            eles_FundingsDict['WW_Funding'] =luf.eles_WW_Funding_Month
            eles_FundingsDict['SegmentFunding'] =luf.eles_SegmentFunding_Month
        for FundingsName in eles_FundingsDict.keys():
            """
                    取界面各字段的值，并放到FundingsDict字典里
                    遍历元素字典eles_FundingsDict中的key，进而通过eles_FundingsDict[key]对元素进行处理
            """
            #对每个字段三个月份的值进行获取
            FundingsDict[FundingsName]=[]
            eles_Fundings=self.get_elements(eles_FundingsDict[FundingsName])
            for ele_Funding_mon in eles_Fundings:
                Value_Funding_speci_mon=ele_Funding_mon.get_attribute('value')
                FundingsDict[FundingsName].append(float(Value_Funding_speci_mon.replace(',','')))
        sum_month1_Funding=0 #保存第一个月的所有值的和
        sum_month2_Funding=0 #保存第二个月的所有值的和
        sum_month3_Funding=0 #保存第三个月的所有值的和
        sum_FundingsValueDict={}#sum_FundingValues={'sum_FundingsValue':[611.20,561.74,611.20,660.66]}
        for FundingValues in FundingsDict.values():#遍历FundingsDict所有的values值
            sum_month1_Funding+=FundingValues[0] #将所有值的第一个月的值进行相加并保存
            sum_month2_Funding += FundingValues[1]
            sum_month3_Funding += FundingValues[2]
        sum_FundingsValueDict['sum_avg_Funding']='%.2f' %((sum_month1_Funding+sum_month2_Funding+sum_month3_Funding)/3)
        sum_FundingsValueDict['sum_month1_Funding']='%.2f' %sum_month1_Funding
        sum_FundingsValueDict['sum_month2_Funding']='%.2f' %sum_month2_Funding
        sum_FundingsValueDict['sum_month3_Funding']='%.2f' %sum_month3_Funding
        self.log.logger_info(FundingsDict)
        return sum_FundingsValueDict

    def get_dict_UnitFunding(self):
        doc='获取Unit Funding ($)的值'
        UnitFundingDict={}
        self.wait_eleVisible(luf.ele_avg_UnitFunding)
        data_avg_UnitFunding=self.get_element_attribute(luf.ele_avg_UnitFunding,'value',doc)
        UnitFundingDict['sum_avg_Funding']=data_avg_UnitFunding.replace(',','')
        data_month1_UnitFunding=self.get_elements(luf.eles_UnitFunding_Month)[0].get_attribute('value')
        data_month2_UnitFunding = self.get_elements(luf.eles_UnitFunding_Month)[1].get_attribute('value')
        data_month3_UnitFunding = self.get_elements(luf.eles_UnitFunding_Month)[2].get_attribute('value')
        UnitFundingDict['sum_month1_Funding']=data_month1_UnitFunding.replace(',','')
        UnitFundingDict['sum_month2_Funding'] = data_month2_UnitFunding.replace(',','')
        UnitFundingDict['sum_month3_Funding'] = data_month3_UnitFunding.replace(',','')
        return UnitFundingDict
