from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
from TestDatas.datas_policyList import DatasPolicyList as dpl
import pytest
from Common.path_object import *

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.APCC
@pytest.mark.smoke3
class TestAP_CostCredit:
    @pytest.mark.parametrize('data', dpp.datas_APCostCredit)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的baseI和fundingOthers1_Value
        CostFunding_Value=for_policyList_class[1].find_by_portfolioNo(dpl.datas_APCostCredit['CostFundingName'],data['portfolioNo'],data['lineCode'])
        #获取portfolio页面需要的月份
        print('CostFunding_Value的值为：',CostFunding_Value)

        #获取Excel表格中筛选后的数据
        nrowdict = for_policyList_class[0].get_bestDatas()
        Excel_datas=for_policyList_class[0].get_the_last_data(nrowdict,CostFunding_Value)
        assert CostFunding_Value==Excel_datas

