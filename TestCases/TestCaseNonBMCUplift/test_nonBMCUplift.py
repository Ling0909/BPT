from TestDatas.datas_portfolioPlan import DatasPortfolioPlan as dpp
from TestDatas.datas_policyList import DatasPolicyList as dpl
from Common.datas_stor import DatasStor
import pytest

@pytest.mark.usefixtures('for_policyList_class')
@pytest.mark.usefixtures('for_policyList_function')
@pytest.mark.nbu
class TestNonBMCUplift:
    @pytest.mark.parametrize('data', dpp.datas_nonBMCUplift)
    def testCase(self,for_policyList_class,data):
        #获取portfolio页面中的baseI和fundingOthers1_Value
        CostFunding_Value=for_policyList_class[1].find_by_portfolioNo(dpl.datas_nonBMCUplift['CostFundingName'],data['portfolioNo'],data['lineCode'])
        print('CostFunding_Value的值为：',CostFunding_Value)
        baseInfo = getattr(DatasStor, 'baseInfo')
        if baseInfo['Region']=='ANZ':
            Excel_datas=for_policyList_class[0].get_the_last_data_ANZ()
            print(f'region是ANZ的时候，Excel_datas值为{Excel_datas}')
        else:#获取Excel表格中筛选后的数据
            nrowdict = for_policyList_class[0].get_bestDatas()
            Excel_datas=for_policyList_class[0].get_the_last_data(nrowdict,CostFunding_Value)
        assert CostFunding_Value==Excel_datas