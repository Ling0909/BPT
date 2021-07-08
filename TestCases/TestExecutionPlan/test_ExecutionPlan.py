import pytest
from TestDatas.common_datas import CommonDatas as da

@pytest.mark.usefixtures('for_executionPlansummary_class')
class TestExecutionPlan():
    def test_executionPlan_auto_HongKong_NB(self,for_executionPlansummary_class):

        for_executionPlansummary_class.create_businessPlan(da.portfolio[0])
        # 为新创建的plan中加入mtm
        for_executionPlansummary_class.create_businessPlanMtm()
        # 编辑mtm
        for_executionPlansummary_class.edit_portfolioItem()
        # 下载customer模板和上传customer模板
        for_executionPlansummary_class.customer()
        # 下载或上传mtm
        for_executionPlansummary_class.volume_mtm()
        # 复制mtm
        for_executionPlansummary_class.copy_portfolioItem()
        # 查看显示log
        for_executionPlansummary_class.showlog_Item()
        # 删除复制的mtm
        for_executionPlansummary_class.delete_portfolioItem()
        # 下载最新的volume后，自动填入想要填的数然后上传
        for_executionPlansummary_class.uploadDownload_Item()

    '''

        def test_executionPlan_auto_Korea_Tablet(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[1])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Taiwan_Option(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[2])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Japan_MobileGaming(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[3])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Germany_NB(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[4])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Nordic_TDT_AIO(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[5])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_France_Tablet(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[6])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_UnitedKingdom_MobileGaming(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[7])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Mexico_NB(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[8])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Brazil_TDT_AIO(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[9])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_Peru_Option(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[10])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_UnitedStates_ofAmerica_NB(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[11])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_UnitedStates_ofAmerica_TDT_AIO(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[12])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()


        def test_executionPlan_auto_UnitedStates_ofAmerica_Option(self, for_executionPlansummary_class):
            for_executionPlansummary_class.create_businessPlan(da.portfolio[13])
            # 为新创建的plan中加入mtm
            for_executionPlansummary_class.create_businessPlanMtm()
            # 编辑mtm
            for_executionPlansummary_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_executionPlansummary_class.customer()
            # 下载或上传mtm
            for_executionPlansummary_class.volume_mtm()
            # 复制mtm
            for_executionPlansummary_class.copy_portfolioItem()
            # 查看显示log
            for_executionPlansummary_class.showlog_Item()
            # 删除复制的mtm
            for_executionPlansummary_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_executionPlansummary_class.uploadDownload_Item()
        '''
