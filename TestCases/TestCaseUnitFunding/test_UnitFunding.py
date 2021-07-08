from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.UF
@pytest.mark.smoke3
class TestCase:
    @pytest.mark.parametrize('data', dpp.datas_UnitFunding)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的sum_fundings信息
        sum_FundingsValueDict=for_policyList_class[0].calculate_UnitFunding(data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('sum_FundingsValueDict的值为：',sum_FundingsValueDict)

        #获取UnitFundingDict数据
        UnitFundingDict= for_policyList_class[0].get_dict_UnitFunding()
        print('UnitFundingDict的值为：',UnitFundingDict)
        assert UnitFundingDict==sum_FundingsValueDict