import pytest
from Common.logger import Logger


@pytest.mark.usefixtures('for_portfolioCheck_class')
class TestPortfolioCheck():
    def test_portfolioCheck(self,for_portfolioCheck_class):
        self.log = Logger()
        self.list1=for_portfolioCheck_class.portfolioCheck()
        self.list2=for_portfolioCheck_class.portfolioCheck_ww()
        pageVolume = round(float(str(self.list1[0])))
        pageNetRevenue = round(float(str(self.list1[1])))
        pageNetBMCGP = round(float(str(self.list1[2])))
        pageVolume_check = round(float(str(self.list2[0])))
        pageNetRevenue_check = round(float(str(self.list2[1])))
        pageNetBMCGP_check = round(float(str(self.list2[2])))

        try:
            self.log.logger_info(f'页面：{pageVolume}')
            self.log.logger_info(f'ww report：{pageVolume_check}')
            assert pageVolume == pageVolume_check

            self.log.logger_info('对数Sum of Volume成功')
        except:
            self.log.logger_info('对数Sum of Volume失败')

        try:
            self.log.logger_info(f'页面：{pageNetRevenue}')
            self.log.logger_info(f'ww report：{pageNetRevenue_check}')
            assert pageNetRevenue == pageNetRevenue_check

            self.log.logger_info('对数Sum of Total Net Revenue ($)成功')
        except:
            self.log.logger_info('对数Sum of Total Net Revenue ($)失败')

        try:
            self.log.logger_info(f'页面：{pageNetBMCGP}')
            self.log.logger_info(f'ww report：{pageNetBMCGP_check}')
            assert pageNetBMCGP == pageNetBMCGP_check

            self.log.logger_info('对数Sum of Total Net BMC GP ($)成功')
        except:
            self.log.logger_info('对数Sum of Total Net BMC GP ($)失败')






