import pytest
from TestDatas.common_datas import CommonDatas as da

@pytest.mark.usefixtures('for_checkDataByPortfolio_class')
class TestGetPortfolioData():
    # 一个产品组的数据比对，EMEA_Tablet
    # def test_CheckData_OneProductGroup(self,for_checkDataByPortfolio_class):
    #     # 导航到Plan Summary页面
    #     for_checkDataByPortfolio_class.navigateToSummaryPage()
    #     # Summary页面Search数据
    #     for_checkDataByPortfolio_class.SearchData_SummaryPage_Tablet(da.CheckData_Country[0])
    #     # 获取plan summary页面中的CAs和BMC GP($)的值
    #     summaryData = for_checkDataByPortfolio_class.get_OneProductGroup_summaryData()
    #     CAs_ActualValue = summaryData.get('CAs')
    #     BMC_GP_ActualValue = summaryData.get('Net_BMC_GP')
    #     TabletPlanNo = summaryData.get('TabletPlanNo')
    #
    #     # 导航到Portfolio Plan页面
    #     for_checkDataByPortfolio_class.navigateToPortfolioPage()
    #     # 获取Portfolio Item里的Volume和BMC GP($)的值
    #     portfolioData = for_checkDataByPortfolio_class.get_OneProductGroup_portfolioData(TabletPlanNo)
    #     Volume_ExpectValue = portfolioData.get('TotalVolume')
    #     BMC_GP_ExpectValue = portfolioData.get('TotalNetBMCGP')
    #
    #     try:
    #         print('plan页面Volume：',Volume_ExpectValue)
    #         print('summary页面CAs：',CAs_ActualValue)
    #         assert Volume_ExpectValue == CAs_ActualValue
    #         print('Volume对数成功')
    #     except:
    #         print('Volume对数失敗')
    #
    #     try:
    #         print('plan页面Net BMC GP($)：', BMC_GP_ExpectValue)
    #         print('summary页面Net BMC GP($)：', BMC_GP_ActualValue)
    #         assert BMC_GP_ExpectValue == BMC_GP_ActualValue
    #         print('Net BMC GP($)对数成功')
    #     except:
    #         print('Net BMC GP($)对数失敗')


    # 多个产品组的数据比对：LA_All
    def test_CheckData_multiProductGroup(self,for_checkDataByPortfolio_class):
        # 导航到Plan Summary页面
        # for_checkDataByPortfolio_class.navigateToSummaryPage1()
        for_checkDataByPortfolio_class.navigateToSummaryPage()
        # Summary页面Search数据
        for_checkDataByPortfolio_class.SearchData_SummaryPage(da.CheckData_Country[1])
        # 导航到PortfolioListComments页面
        for_checkDataByPortfolio_class.navigateToPortfolioListCommentsPage()
        # 获取每个产品组对应的Plan No
        NBSummaryData = for_checkDataByPortfolio_class.get_NBProductGroup_summaryData()
        TDTSummaryData = for_checkDataByPortfolio_class.get_TDTProductGroup_summaryData()
        TabletSummaryData = for_checkDataByPortfolio_class.get_TabletProductGroup_summaryData()
        OptionsSummaryData = for_checkDataByPortfolio_class.get_OptionProductGroup_summaryData()
        AllSummaryData = for_checkDataByPortfolio_class.get_AllProductGroup_summaryData()

        # NBSummaryData = for_checkDataByPortfolio_class.get_ProductGroup_summaryData('NB')
        # TDTSummaryData = for_checkDataByPortfolio_class.get_ProductGroup_summaryData('TDT/AIO')
        # TabletSummaryData = for_checkDataByPortfolio_class.get_ProductGroup_summaryData('Tablet')
        # OptionsSummaryData = for_checkDataByPortfolio_class.get_ProductGroup_summaryData('Option')
        # AllSummaryData = for_checkDataByPortfolio_class.get_ProductGroup_summaryData('All')

        #获取summary页面NB产品组的值
        NBCAs_summaryValue = NBSummaryData.get('NBCAs')
        NBBMC_GP_summaryValue = NBSummaryData.get('NBNet_BMC_GP')
        NBPlanNo = NBSummaryData.get('NBPlanNo')

        # 获取summary页面TDT产品组的值
        TDTCAs_summaryValue = TDTSummaryData.get('TDTCAs')
        TDTBMC_GP_summaryValue = TDTSummaryData.get('TDTNet_BMC_GP')
        TDTPlanNo = TDTSummaryData.get('TDTPlanNo')

        # 获取summary页面Tablet产品组的值
        TabletCAs_summaryValue = TabletSummaryData.get('TabletCAs')
        TabletBMC_GP_summaryValue = TabletSummaryData.get('TabletNet_BMC_GP')
        TabletPlanNo = TabletSummaryData.get('TabletPlanNo')

        # 获取summary页面Option产品组的值
        OptionCAs_summaryValue = OptionsSummaryData.get('OptionCAs')
        OptionBMC_GP_summaryValue = OptionsSummaryData.get('OptionNet_BMC_GP')
        OptionPlanNo = OptionsSummaryData.get('OptionPlanNo')

        # 获取summary页面所有产品组All的值
        AllCAs_summaryValue = AllSummaryData.get('AllCAs')
        AllBMC_GP_summaryValue = AllSummaryData.get('AllNet_BMC_GP')


        # 导航到Portfolio Plan页面
        for_checkDataByPortfolio_class.navigateToPortfolioPage()
        # 获取Portfolio Item里的Volume和BMC GP($)的值
        # 获取plan页面NB产品组的值
        NBPortfolioData = for_checkDataByPortfolio_class.get_multiProductGroup_portfolioData(NBPlanNo)
        NBVolume_PlanValue = NBPortfolioData.get('TotalVolume')
        NBBMC_GP_PlanValue = NBPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面TDT产品组的值
        TDTPortfolioData = for_checkDataByPortfolio_class.get_multiProductGroup_portfolioData(TDTPlanNo)
        TDTVolume_PlanValue = TDTPortfolioData.get('TotalVolume')
        TDTBMC_GP_PlanValue = TDTPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面Tablet产品组的值
        TabletPortfolioData = for_checkDataByPortfolio_class.get_multiProductGroup_portfolioData(TabletPlanNo)
        TabletVolume_PlanValue = TabletPortfolioData.get('TotalVolume')
        TabletBMC_GP_PlanValue = TabletPortfolioData.get('TotalNetBMCGP')

        # 获取plan页面Option产品组的值
        OptionPortfolioData = for_checkDataByPortfolio_class.get_multiProductGroup_portfolioData(OptionPlanNo)
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