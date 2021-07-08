import pytest

@pytest.mark.usefixtures('for_dealSimulation_class')
class TestDealSimulation():
    # 创建Deal Plan
    def test_Create_DealPlan(self,for_dealSimulation_class):
        for_dealSimulation_class.Create_DealPlan()

    # 调试时使用
    # def test_selectDealNo(self,for_dealSimulation_class):
    #     for_dealSimulation_class.selectDealNo()

    # 编辑Deal Item
    def test_Edit_DealItem(self, for_dealSimulation_class):
            for_dealSimulation_class.Edit_DealItem()

    # 编辑Deal Item
    def test_copy_dealItem(self, for_dealSimulation_class):
        for_dealSimulation_class.copy_dealItem()

    # 显示Deal Item的log记录
    def test_showlog_Item(self, for_dealSimulation_class):
        for_dealSimulation_class.showlog_Item()

    # 删除Deal Item
    def test_delete_DealItem(self, for_dealSimulation_class):
            for_dealSimulation_class.delete_DealItem()

    # 提交Deal Item
    def test_Submit_DealItem(self, for_dealSimulation_class):
        for_dealSimulation_class.Submit_DealItem()

    # 下载并上传Deal Item
    def test_Download_DealItem(self, for_dealSimulation_class):
        for_dealSimulation_class.Download_DealItem()




