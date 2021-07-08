import pytest
from TestDatas.common_datas import CommonDatas as da
@pytest.mark.usefixtures('for_dealSimulation_class')
class TestDealSimulation():

    def test_DealPlan_UnitedKingdom(self,for_dealSimulation_class):
        # 创建Deal Plan
        for_dealSimulation_class.Create_DealPlan(da.deal[0])
        # 上传MTM
        for_dealSimulation_class.clickSelectFromMTM()
        for_dealSimulation_class.inputPNValue(da.deal_mtm[0])  #NB
        for_dealSimulation_class.inputPNValue(da.deal_mtm[1])  #TDT
        for_dealSimulation_class.inputPNValue(da.deal_mtm[2])  #Option
        for_dealSimulation_class.inputPNValue(da.deal_mtm[3])  #Visual
        for_dealSimulation_class.closeMTMWindow()
        # 编辑Deal Item
        for_dealSimulation_class.Edit_DealItem()
        # Copy Deal Item
        for_dealSimulation_class.copy_dealItem()
        # 删除Deal Item
        for_dealSimulation_class.delete_DealItem()
        # # 调试时使用
        # for_dealSimulation_class.selectDealNo()
        # 下载并上传Deal Item
        for_dealSimulation_class.Download_DealItem()
        # 提交Deal Item
        for_dealSimulation_class.Submit_DealItem()


    # def test_DealPlan_Sweden(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Create_DealPlan()



    # 调试时使用
    # def test_selectDealNo(self,for_dealSimulation_class):
    #     for_dealSimulation_class.selectDealNo()

    # # 编辑Deal Item
    # # def test_Edit_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Edit_DealItem()
    #
    # # Copy Deal Item
    # # def test_copy_dealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.copy_dealItem()
    #
    # #显示Deal Item的log记录
    # # def test_showlog_Item(self, for_dealSimulation_class):
    # #     for_dealSimulation_class.showlog_Item()
    #
    # # 删除Deal Item
    # # def test_delete_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.delete_DealItem()
    #
    # # 提交Deal Item
    # # def test_Submit_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Submit_DealItem()
    #
    # # 下载并上传Deal Item
    # # def test_Download_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Download_DealItem()
    # def test_Create_DealPlan_Sweden(self,for_dealSimulation_class):
    #     for_dealSimulation_class.Create_DealPlan(da.deal[1])
    #
    # # 调试时使用
    # # def test_selectDealNo(self,for_dealSimulation_class):
    # #     for_dealSimulation_class.selectDealNo()
    #
    # # 编辑Deal Item
    # # def test_Edit_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Edit_DealItem()
    #
    # # 编辑Deal Item
    # # def test_copy_dealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.copy_dealItem()
    #
    # # 显示Deal Item的log记录
    # # def test_showlog_Item(self, for_dealSimulation_class):
    # #     for_dealSimulation_class.showlog_Item()
    #
    # # 删除Deal Item
    # # def test_delete_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.delete_DealItem()
    #
    # # 提交Deal Item
    # # def test_Submit_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Submit_DealItem()
    #
    # # 下载并上传Deal Item
    # # def test_Download_DealItem(self, for_dealSimulation_class):
    #     for_dealSimulation_class.Download_DealItem()




