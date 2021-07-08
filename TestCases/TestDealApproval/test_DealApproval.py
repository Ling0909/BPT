import pytest


@pytest.mark.usefixtures('for_dealApproval_class')
class TestDealApproval():
    def test_reject_DealItem(self,for_dealApproval_class):
        for_dealApproval_class.reject_DealItem()

    def test_Delete_DealItem(self, for_dealApproval_class):
        for_dealApproval_class.Delete_DealItem()

