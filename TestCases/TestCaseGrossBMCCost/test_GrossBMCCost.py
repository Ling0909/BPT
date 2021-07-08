from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.GBC
class TestCase:
    @pytest.mark.parametrize('data',dpp.datas_GrossBMCCost)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的sum_fundings信息
        calculate_GrossBMCCost_Dict=for_policyList_class[0].calculate_by_formula(data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('calculate_GrossBMCCost_Dict的值为：',calculate_GrossBMCCost_Dict)

        #获取UnitFundingDict数据
        GrossBMCCostDict= for_policyList_class[0].get_pageValue_GrossBMCCost()
        print('GrossBMCCostDict的值为：',GrossBMCCostDict)
        assert GrossBMCCostDict==calculate_GrossBMCCost_Dict