import pytest
from TestDatas.common_datas import CommonDatas as da
from Common.logger import Logger

@pytest.mark.usefixtures('for_businessPlan_class')
class TestBusinessPlan():

    #创建businessplan_

    def test_auto_HongKong_NB(self,for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan(da.portfolio[0])
            #为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[0])
            #编辑mtm
            for_businessPlan_class.edit_portfolioItem()
            #下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            #下载或上传mtm
            for_businessPlan_class.volume_mtm()
            #复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            #查看显示log
            for_businessPlan_class.showlog_Item()
            #删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            #下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("HongKong_NB报错")

    def test_auto_Korea_Tablet(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[1])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[1])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Korea_Tablet报错")

    def test_auto_Taiwan_Option(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[2])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[2])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Taiwan_Option报错")

    def test_auto_Japan_MobileGaming(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[3])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[3])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Japan_MobileGaming报错")

    def test_auto_Germany_NB(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[4])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[4])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Germany_NB报错")

    def test_auto_Nordic_TDT_AIO(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[5])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[5])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Nordic_TDT_AIO报错")

    def test_auto_France_Tablet(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[6])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[6])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("France_Tablet报错")

    def test_auto_UnitedKingdom_MobileGaming(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[7])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[7])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("UnitedKingdom_MobileGaming报错")

    def test_auto_Mexico_NB(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[8])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[8])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Mexico_NB报错")

    def test_auto_Brazil_TDT_AIO(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[9])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[9])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Brazil_TDT_AIO报错")

    def test_auto_Peru_Option(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan1(da.portfolio[10])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm(da.mtm[10])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_Germany()
            # 下载customer模板和上传customer模板
            for_businessPlan_class.customer()
            # 下载或上传mtm
            for_businessPlan_class.volume_mtm()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item()
        except:
            self.log.logger_error("Peru_Option报错")


    def test_auto_UnitedStates_ofAmerica_NB(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan_UnitedStates_ofAmerica_NB1(da.portfolio[11])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm_american(da.mtm[11])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_UnitedStates_ofAmerica_NB()
            # 下载customer模板和上传customer模板
            # for_businessPlan_class.customer()
            # 下载或上传mtm
            # for_businessPlan_class.volume_mtm1()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item1()
        except:
            self.log.logger_error("UnitedStates_ofAmerica_NB报错")

    def test_auto_UnitedStates_ofAmerica_TDT_AIO(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan_UnitedStates_ofAmerica_NB1(da.portfolio[12])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm_american(da.mtm[12])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_UnitedStates_ofAmerica_NB()
            # 下载customer模板和上传customer模板
            # for_businessPlan_class.customer()
            # 下载或上传mtm
            # for_businessPlan_class.volume_mtm1()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item1()
        except:
            self.log.logger_error("UnitedStates_ofAmerica_TDT_AIO报错")

    def test_auto_UnitedStates_ofAmerica_Option(self, for_businessPlan_class):
        self.log = Logger()
        try:
            for_businessPlan_class.create_businessPlan_UnitedStates_ofAmerica_NB1(da.portfolio[13])
            # 为新创建的plan中加入mtm
            for_businessPlan_class.create_businessPlanMtm_american(da.mtm[13])
            # 编辑mtm
            for_businessPlan_class.edit_portfolioItem_UnitedStates_ofAmerica_NB()
            # 下载customer模板和上传customer模板
            # for_businessPlan_class.customer()
            # 下载或上传mtm
            # for_businessPlan_class.volume_mtm1()
            # 复制mtm
            # for_businessPlan_class.copy_portfolioItem()
            # 查看显示log
            for_businessPlan_class.showlog_Item()
            # 删除复制的mtm
            # for_businessPlan_class.delete_portfolioItem()
            # 下载最新的volume后，自动填入想要填的数然后上传
            for_businessPlan_class.uploadDownload_Item1()
        except:
            self.log.logger_error("UnitedStates_ofAmerica_Option报错")


