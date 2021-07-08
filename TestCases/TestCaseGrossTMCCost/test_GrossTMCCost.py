from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.GTC
class TestCase:
    @pytest.mark.parametrize('data', dpp.datas_GrossTMCCost)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的sum_fundings信息
        calculate_GrossTMCCost_Dict=for_policyList_class[0].calculate_by_formula(data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('calculate_GrossTMCCost_Dict的值为：',calculate_GrossTMCCost_Dict)

        #获取UnitFundingDict数据
        GrossTMCCostDict= for_policyList_class[0].get_pageValue_GrossTMCCost()
        print('GrossTMCCostDict的值为：',GrossTMCCostDict)
        assert GrossTMCCostDict==calculate_GrossTMCCost_Dict