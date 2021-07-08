import pytest
from TestDatas.common_datas import CommonDatas as da
@pytest.mark.usefixtures('for_executionPlansummary_class')
class TestBusinessPlanSummary():
    def test_excutionsummary_auto_HongKong_NB(self,for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanv(da.portfolio[0])

    def test_summary_auto_Korea_Tablet(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[1])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Taiwan_Option(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[2])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Japan_MobileGaming(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[3])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Germany_NB(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[4])
        # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Nordic_TDT_AIO(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[5])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_France_Tablet(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[6])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_UnitedKingdom_MobileGaming(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[7])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Mexico_NB(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[8])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Brazil_TDT_AIO(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[9])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_Peru_Option(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[10])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_UnitedStates_ofAmerica_NB(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[11])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_UnitedStates_ofAmerica_TDT_AIO(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[12])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()

    def test_summary_auto_UnitedStates_ofAmerica_Option(self, for_executionPlansummary_class):
        for_executionPlansummary_class.create_businessPlanSummy(da.portfolio[13])
        # # 进入审批页面拒绝审批
        # for_businessPlanv_class.businessPlanSummyApprove()
        # # 进入plansummary页面删除新创建的plansummary
        # for_businessPlanv_class.delete_businessPlanSummy()
        # # 进入businessplan中搜索刚刚操作summary所用到的businessplan
        # for_businessPlanv_class.search_businessPlan()
