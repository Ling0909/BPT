from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
from TestDatas.datas_policyList import DatasPolicyList as dpl
from Common.datas_stor import DatasStor
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.smoke
class TestCEOFundingOthers1:
    @pytest.mark.parametrize('data', getattr(DatasStor,'datas_GEOFundingOthers1'))
    def test_region_notLAS(self,for_policyList_class,data):
        #获取portfolio页面中的baseI和CostFunding_Value
        CostFunding_Value=for_policyList_class[1].find_by_portfolioNo(dpl.datas_GEOFundingOthers1['CostFundingName'],data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('CostFunding_Value的值为：{}'.format(CostFunding_Value))
        for_policyList_class[0].getExcelMonthBySystem(CostFunding_Value)
        #获取Excel表格中筛选后的数据
        for_policyList_class[0].get_bestDatas()
        Excel_datas=for_policyList_class[0].excelDatas_count(CostFunding_Value)
        assert CostFunding_Value==Excel_datas

    @pytest.mark.parametrize('data', getattr(DatasStor,'datas_region_isLAS'))
    def test_region_isLAS(self,for_policyList_class,data):
        # 获取portfolio页面中的baseI和CostFunding_Value
        CostFunding_Value = for_policyList_class[1].find_by_portfolioNo(dpl.datas_GEOFundingOthers1['CostFundingName'],data['portfolioNo'],data['lineCode'])
        # 获取portfolio页面需要的月份
        dict1= {'key1': '0.00', 'key2': '0.00', 'key3':'0.00', 'key4':'0.00'}
        assert str(CostFunding_Value.values())==str(dict1.values())
