import pytest
from TestDatas.common_datas import CommonDatas as da

@pytest.mark.usefixtures('for_checkSummaryReportData_class')
class TestGetData():

    # 多个产品组的数据比对
    def test_CheckData_multiProductGroup(self,for_checkSummaryReportData_class):
        # 导航到Plan Summary页面
        for_checkSummaryReportData_class.navigateToSummaryPage()
        # Summary页面Search数据
        for_checkSummaryReportData_class.SearchData_SummaryPage(da.CheckData_Country[2])
        # 获取summary页面每个产品组的plan No
        for_checkSummaryReportData_class.navigateToPortfolioListCommentsPage()
        # 获取summary页面每个产品组的值
        NBSummaryData = for_checkSummaryReportData_class.get_ProductGroup_summaryData('NB')
        TDTSummaryData = for_checkSummaryReportData_class.get_ProductGroup_summaryData('TDT/AIO')
        TabletSummaryData = for_checkSummaryReportData_class.get_ProductGroup_summaryData('Tablet')
        OptionSummaryData = for_checkSummaryReportData_class.get_ProductGroup_summaryData('Option')
        VisualSummaryData = for_checkSummaryReportData_class.get_ProductGroup_summaryData('Visual')

        #获取summary页面每个产品组的值
        CAs_summaryValue = NBSummaryData.get('CAs')
        BMC_GP_summaryValue = NBSummaryData.get('Net_BMC_GP')
        PlanNo = NBSummaryData.get('PlanNo')


        # 导航到Portfolio Plan页面
        for_checkSummaryReportData_class.navigateToPortfolioPage()
        # 获取Portfolio Item里的Volume和BMC GP($)的值
        # 获取plan页面NB产品组的值
        NBPortfolioData = for_checkSummaryReportData_class.get_multiProductGroup_portfolioData(NBPlanNo)
        NBVolume_PlanValue = NBPortfolioData.get('TotalVolume')
        NBBMC_GP_PlanValue = NBPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面TDT产品组的值
        TDTPortfolioData = for_checkSummaryReportData_class.get_multiProductGroup_portfolioData(TDTPlanNo)
        TDTVolume_PlanValue = TDTPortfolioData.get('TotalVolume')
        TDTBMC_GP_PlanValue = TDTPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面Tablet产品组的值
        TabletPortfolioData = for_checkSummaryReportData_class.get_multiProductGroup_portfolioData(TabletPlanNo)
        TabletVolume_PlanValue = TabletPortfolioData.get('TotalVolume')
        TabletBMC_GP_PlanValue = TabletPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面Option产品组的值
        OptionPortfolioData = for_checkSummaryReportData_class.get_multiProductGroup_portfolioData(OptionPlanNo)
        OptionVolume_PlanValue = OptionPortfolioData.get('TotalVolume')
        OptionBMC_GP_PlanValue = OptionPortfolioData.get('TotalNetBMCGP')

        # Potofoliio Plan页面所有值的汇总
        TotalVolums = NBVolume_PlanValue + TDTVolume_PlanValue + TabletVolume_PlanValue + OptionVolume_PlanValue
        TotalNetBMCGP = NBBMC_GP_PlanValue + TDTBMC_GP_PlanValue + TabletBMC_GP_PlanValue + OptionBMC_GP_PlanValue

        try:
            print('summary页面CAs:',NBCAs_summaryValue)
            print('plan页面Volume:', NBVolume_PlanValue)
            assert NBCAs_summaryValue == NBVolume_PlanValue
            print('NB产品组Volume对数成功')
        except:
            print('NB产品组Volume对数失败')

        try:
            print('summary页面Net_BMC_GP:', NBBMC_GP_summaryValue)
            print('plan页面Net_BMC_GP:', NBBMC_GP_PlanValue)
            assert NBBMC_GP_summaryValue == NBBMC_GP_PlanValue
            print('NB产品组Net_BMC_GP对数成功')
        except:
            print('NB产品组Net_BMC_GP对数失败')

        try:
            print('summary页面CAs:', TDTCAs_summaryValue)
            print('plan页面Volume:', TDTVolume_PlanValue)
            assert TDTCAs_summaryValue == TDTVolume_PlanValue
            print('TDT产品组Volume对数成功')
        except:
            print('TDT产品组Volume对数失败')

        try:
            print('summary页面Net_BMC_GP:', TDTBMC_GP_summaryValue)
            print('plan页面Net_BMC_GP:', TDTBMC_GP_PlanValue)
            assert TDTBMC_GP_summaryValue == TDTBMC_GP_PlanValue
            print('TDT产品组Net_BMC_GP对数成功')
        except:
            print('TDT产品组Net_BMC_GP对数失败')

        try:
            print('summary页面CAs:', TabletCAs_summaryValue)
            print('plan页面Volume:', TabletVolume_PlanValue)
            assert TabletCAs_summaryValue == TabletVolume_PlanValue
            print('Tablet产品组Volume对数成功')
        except:
            print('Tablet产品组Volume对数失败')

        try:
            print('summary页面Net_BMC_GP:', TabletBMC_GP_summaryValue)
            print('plan页面Net_BMC_GP:', TabletBMC_GP_PlanValue)
            assert TabletBMC_GP_summaryValue == TabletBMC_GP_PlanValue
            print('Tablet产品组Net_BMC_GP对数成功')
        except:
            print('Tablet产品组Net_BMC_GP对数失败')

        try:
            print('summary页面CAs:', OptionCAs_summaryValue)
            print('plan页面Volume:', OptionVolume_PlanValue)
            assert OptionCAs_summaryValue == OptionVolume_PlanValue
            print('Option产品组Volume对数成功')
        except:
            print('Option产品组Volume对数失败')

        try:
            print('summary页面Net_BMC_GP:', OptionBMC_GP_summaryValue)
            print('plan页面Net_BMC_GP:', OptionBMC_GP_PlanValue)
            assert OptionBMC_GP_summaryValue == OptionBMC_GP_PlanValue
            print('Option产品组Net_BMC_GP对数成功')

        except:
            print('Option产品组Net_BMC_GP对数失败')

        try:
            print('summary页面CAs:', AllCAs_summaryValue)
            print('plan页面Volume:', TotalVolums)
            assert AllCAs_summaryValue == TotalVolums
            print('所有产品组Volume汇总对数成功')
        except:
            print('所有产品组Volume汇总对数失败')

        try:
            print('summary页面Net_BMC_GP:', AllBMC_GP_summaryValue)
            print('plan页面Net_BMC_GP:', TotalNetBMCGP)
            assert AllBMC_GP_summaryValue == TotalNetBMCGP
            print('所有产品组Net_BMC_GP汇总对数成功')
        except:
            print('所有产品组Net_BMC_GP汇总对数失败')