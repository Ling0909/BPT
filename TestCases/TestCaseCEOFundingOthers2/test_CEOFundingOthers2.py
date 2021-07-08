from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
from TestDatas.datas_policyList import DatasPolicyList as dpl
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.OTH
class TestCEOFundingOthers2:
    @pytest.mark.parametrize('data',dpp.datas_GEOFundingOthers2)
    def test_CEOFundingOthers2(self,for_policyList_class,data):

        #获取portfolio页面中的baseI和fundingOthers1_Value
        CostFunding_Value=for_policyList_class[1].find_by_portfolioNo(dpl.datas_GEOFundingOthers2['CostFundingName'],data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('GEOfundingOthers2_Value的值为：',CostFunding_Value)
        # for_policyList_class[0].getExcelMonthBySystem(CostFunding_Value)
        #获取Excel表格中筛选后的数据
        for_policyList_class[0].get_bestDatas()
        Excel_datas=for_policyList_class[0].excelDatas_count(CostFunding_Value)
        assert CostFunding_Value==Excel_datas