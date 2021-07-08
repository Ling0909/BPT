from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.BMCC
@pytest.mark.smoke3
class TestCase:
    @pytest.mark.parametrize('data', dpp.datas_BMC_Cost_W_Fundings)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的sum_fundings信息
        sum_BMCFundingsValueDict=for_policyList_class[0].calculate_BMC_Cost_w_Fundings(data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('sum_BMCFundingsValueDict的值为：',sum_BMCFundingsValueDict)

        #获取UnitFundingDict数据
        BMCFundingDict= for_policyList_class[0].get_dict_BMCFunding()
        print('UnitFundingDict的值为：',BMCFundingDict)
        assert BMCFundingDict==sum_BMCFundingsValueDict