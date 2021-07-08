class DatasPortfolioPlan:
    #UAT环境

    """datas_GEOFundingOthers1 = [{'portfolioNo': 'LP_20190725_010_DE', 'lineCode': 'LP_20190725_010_DE_0001_P'},
                               {'portfolioNo': 'LP_20190723_157_BR', 'lineCode': 'LP_20190723_157_BR_0001_P'},
                               {'portfolioNo': 'LP_20190604_210_DE', 'lineCode': 'LP_20190604_210_DE_0414_P'},
                               {'portfolioNo': 'LP_20190723_009_BR', 'lineCode': 'LP_20190723_009_BR_0006_P'},
                               {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                               {'portfolioNo': 'LP_20190725_003_BR', 'lineCode': 'LP_20190725_003_BR_0001_P'},
                               {'portfolioNo': 'LP_20190722_206_DE', 'lineCode': 'LP_20190722_206_DE_0001_P'},
                               {'portfolioNo': 'LP_20190725_004_BR', 'lineCode': 'LP_20190725_004_BR_0001_P'},=
                               {'portfolioNo': 'LP_20190725_005_BR', 'lineCode': 'LP_20190725_005_BR_0001_P'},
                               {'portfolioNo': 'LP_20190722_205_NZ', 'lineCode': 'LP_20190722_205_NZ_0001_P'},
                               {'portfolioNo': 'LP_20190719_154_CA', 'lineCode': 'LP_20190719_154_CA_0001_P'}]
    datas_region_isLAS = [{'portfolioNo': 'LP_20190815_009_AR', 'lineCode': 'LP_20190815_009_AR_0003_P'},
                          {'portfolioNo': 'LP_20190903_020_GT', 'lineCode': 'LP_20190903_020_GT_0001_P'}]

    datas_GEOFundingOthers2 = [{'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                               {'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                               {'portfolioNo': 'LP_20190904_300_FR', 'lineCode': 'LP_20190904_300_FR_0001_P'},
                               {'portfolioNo': 'LP_20190821_301_FR', 'lineCode': 'LP_20190821_301_FR_0003_G'}]
    datas_GEOFundingOthers3 = [{'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                               {'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                               {'portfolioNo': 'LP_20190904_300_FR', 'lineCode': 'LP_20190904_300_FR_0001_P'},
                               {'portfolioNo': 'LP_20190821_301_FR', 'lineCode': 'LP_20190821_301_FR_0003_G'}]
    datas_GEOFundingOthers4 = [{'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                               {'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                               {'portfolioNo': 'LP_20190904_300_FR', 'lineCode': 'LP_20190904_300_FR_0001_P'},
                               {'portfolioNo': 'LP_20190821_301_FR', 'lineCode': 'LP_20190821_301_FR_0003_G'}]
    datas_Funding1_CPU = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                          {'portfolioNo': 'LP_20190829_011_SG', 'lineCode': 'LP_20190829_011_SG_0001_P'},
                          {'portfolioNo': 'LP_20190909_001_CA', 'lineCode': 'LP_20190909_001_CA_0001_P'},
                          {'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                          {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                          {'portfolioNo': 'LP_20190821_302_FR', 'lineCode': 'LP_20190821_302_FR_0002_G'}]

    datas_Funding2_HDD_SSHD_SSD = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                                   {'portfolioNo': 'LP_20190829_011_SG', 'lineCode': 'LP_20190829_011_SG_0001_P'},
                                   {'portfolioNo': 'LP_20190909_001_CA', 'lineCode': 'LP_20190909_001_CA_0001_P'},
                                   {'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                                   {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                                   {'portfolioNo': 'LP_20190821_302_FR', 'lineCode': 'LP_20190821_302_FR_0002_G'}]

    datas_Funding3_Others = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                             {'portfolioNo': 'LP_20190829_011_SG', 'lineCode': 'LP_20190829_011_SG_0001_P'},
                             {'portfolioNo': 'LP_20190909_001_CA', 'lineCode': 'LP_20190909_001_CA_0001_P'},
                             {'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                             {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                             {'portfolioNo': 'LP_20190821_302_FR', 'lineCode': 'LP_20190821_302_FR_0002_G'}]
    datas_APCostCredit = [{'portfolioNo': 'LP_20190905_002_NZ', 'lineCode': 'LP_20190905_002_NZ_0001_P'},
                          {'portfolioNo': 'LP_20190909_008_ROI', 'lineCode': 'LP_20190909_008_ROI_0001_P'},
                          {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0001_P'},
                          {'portfolioNo': 'LP_20190903_222_AU', 'lineCode': 'LP_20190903_222_AU_0001_P'},
                          {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'}]

    datas_CountryAdjustment = [{'portfolioNo': 'LP_20190220_132_RU', 'lineCode': 'LP_20190220_132_RU_0002_P'},
                               {'portfolioNo': 'LP_20190909_008_ROI', 'lineCode': 'LP_20190909_008_ROI_0001_P'},
                               {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0001_P'},
                               {'portfolioNo': 'LP_20190903_222_AU', 'lineCode': 'LP_20190903_222_AU_0001_P'},
                               {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                               {'portfolioNo': 'LP_20190909_011_BR', 'lineCode': 'LP_20190909_011_BR_0001_P'}]

    datas_UnitFunding = [{'portfolioNo': 'LP_20190220_132_RU', 'lineCode': 'LP_20190220_132_RU_0002_P'},
                         {'portfolioNo': 'LP_20190909_008_ROI', 'lineCode': 'LP_20190909_008_ROI_0001_P'},
                         {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0001_P'},
                         {'portfolioNo': 'LP_20190903_222_AU', 'lineCode': 'LP_20190903_222_AU_0001_P'},
                         {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                         {'portfolioNo': 'LP_20190909_011_BR', 'lineCode': 'LP_20190909_011_BR_0001_P'}]

    datas_nonBMCUplift = [{'portfolioNo': 'LP_20190220_132_RU', 'lineCode': 'LP_20190220_132_RU_0002_P'},
                          {'portfolioNo': 'LP_20190909_008_ROI', 'lineCode': 'LP_20190909_008_ROI_0001_P'},
                          {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0001_P'},
                          {'portfolioNo': 'LP_20190903_222_AU', 'lineCode': 'LP_20190903_222_AU_0001_P'},
                          {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                          {'portfolioNo': 'LP_20190909_011_BR', 'lineCode': 'LP_20190909_011_BR_0001_P'}]

    datas_PNAssessment = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                          {'portfolioNo': 'LP_20190829_011_SG', 'lineCode': 'LP_20190829_011_SG_0001_P'},
                          {'portfolioNo': 'LP_20190909_001_CA', 'lineCode': 'LP_20190909_001_CA_0001_P'},
                          {'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                          {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                          {'portfolioNo': 'LP_20190821_302_FR', 'lineCode': 'LP_20190821_302_FR_0002_G'}]


    datas_BMC_Cost_W_Fundings = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                                 {'portfolioNo': 'LP_20190829_011_SG', 'lineCode': 'LP_20190829_011_SG_0001_P'},
                                 {'portfolioNo': 'LP_20190909_001_CA', 'lineCode': 'LP_20190909_001_CA_0001_P'},
                                 {'portfolioNo': 'LP_20190909_005_DE', 'lineCode': 'LP_20190909_005_DE_0001_P'},
                                 {'portfolioNo': 'LP_20190812_001_TW', 'lineCode': 'LP_20190812_001_TW_0001_P'},
                                 {'portfolioNo': 'LP_20190821_302_FR', 'lineCode': 'LP_20190821_302_FR_0002_G'}]

    datas_GrossTMCCost = [{'portfolioNo': 'LP_20190830_312_CA', 'lineCode': 'LP_20190830_312_CA_0001_P'},
                          {'portfolioNo': 'LP_20180530_053_INOS', 'lineCode': 'LP_20180530_053_INOS_0002_P'},
                          {'portfolioNo': 'LP_20190611_171_IN', 'lineCode': 'LP_20190611_171_IN_0001_P'},
                          {'portfolioNo': 'LP_20190730_290_ROI', 'lineCode': 'LP_20190730_290_ROI_0001_P'},
                          {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'}]

    datas_NetTMCCost = [{'portfolioNo': 'LP_20190830_312_CA', 'lineCode': 'LP_20190830_312_CA_0001_P'},
                        {'portfolioNo': 'LP_20180530_053_INOS', 'lineCode': 'LP_20180530_053_INOS_0002_P'},
                        {'portfolioNo': 'LP_20190611_171_IN', 'lineCode': 'LP_20190611_171_IN_0001_P'},
                        {'portfolioNo': 'LP_20190730_290_ROI', 'lineCode': 'LP_20190730_290_ROI_0001_P'},
                        {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'}]

    datas_GrossBMCCost = [{'portfolioNo': 'LP_20190830_312_CA', 'lineCode': 'LP_20190830_312_CA_0001_P'},
                          {'portfolioNo': 'LP_20180530_053_INOS', 'lineCode': 'LP_20180530_053_INOS_0002_P'},
                          {'portfolioNo': 'LP_20190730_290_ROI', 'lineCode': 'LP_20190730_290_ROI_0001_P'},
                          {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'},
                          {'portfolioNo': 'LP_20190816_178_UY', 'lineCode': 'LP_20190816_178_UY_0001_P'},
                          {'portfolioNo': 'LP_20190818_001_TR', 'lineCode': 'LP_20190818_001_TR_0059_P'}]

               # datas_UnitFunding用例维度：
               # data0:国家为Canada，季度是Q4
               # data1:GEO是AP,国家是India Offshore，季度Q3
               # data2:GEO是AP，国家ROI，季度Q2
               # data3:GEO是AP，国家Australia，季度Q1
               # data4:国家Germany，季度Q2
               # data5:Region是LAS,Sales mode是Offshore，国家Panama
               # data5:Region是LAS,Sales mode是Onshore，国家Uruguay
               # data6:国家Turkey，季度Q3
    datas_CountryAdjustment2 = [={'portfolioNo': 'LP_20190719_004_ROI', 'lineCode': 'LP_20190719_004_ROI_0001_P'},
                                {'portfolioNo': 'LP_20190530_034_VN', 'lineCode': 'LP_20190530_034_VN_0001_P'},
                                {'portfolioNo': 'LP_20190717_007_AU', 'lineCode': 'LP_20190717_007_AU_0001_P'},
                                {'portfolioNo': 'LP_20190719_007_JP', 'lineCode': 'LP_20190829_019_JP_0002_P'}]
    """


    #develop环境

    datas_GEOFundingOthers1 = [{'portfolioNo': 'LP_20190725_010_DE', 'lineCode': 'LP_20190725_010_DE_0001_P'},
                               {'portfolioNo': 'LP_20190723_157_BR', 'lineCode': 'LP_20190723_157_BR_0001_P'},
                               {'portfolioNo': 'LP_20190604_210_DE', 'lineCode': 'LP_20190604_210_DE_0414_P'}]
    datas_region_isLAS=[{'portfolioNo': 'LP_20190815_009_AR', 'lineCode': 'LP_20190815_009_AR_0003_P'},
                        {'portfolioNo': 'LP_20190722_196_GT', 'lineCode': 'LP_20190722_196_GT_0001_P'}]

    datas_GEOFundingOthers2 = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                            {'portfolioNo': 'LP_20190909_002_TR', 'lineCode': 'LP_20190909_002_TR_0001_P'},
                            {'portfolioNo': 'LP_20190605_192_BE', 'lineCode': 'LP_20190605_192_BE_0001_G'}]
    datas_GEOFundingOthers3 = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                            {'portfolioNo': 'LP_20190909_002_TR', 'lineCode': 'LP_20190909_002_TR_0001_P'},
                            {'portfolioNo': 'LP_20190605_192_BE', 'lineCode': 'LP_20190605_192_BE_0001_G'}]
    datas_GEOFundingOthers4 =[{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                            {'portfolioNo': 'LP_20190909_002_TR', 'lineCode': 'LP_20190909_002_TR_0001_P'},
                            {'portfolioNo': 'LP_20190605_192_BE', 'lineCode': 'LP_20190605_192_BE_0001_G'}]
    datas_Funding1_CPU = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190909_003_SG', 'lineCode': 'lp_20190909_003_sg_0002_p'},
                            {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                            {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'}]

    datas_Funding2_HDD_SSHD_SSD = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190909_003_SG', 'lineCode': 'LP_20190909_003_SG_0002_P'},
                            {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'}]

    datas_Funding3_Others = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                            {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                            {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'}]
    datas_APCostCredit= [{'portfolioNo': 'LP_20190729_003_NZ', 'lineCode': 'LP_20190729_003_NZ_0001_P'},
                         {'portfolioNo': 'LP_20190719_004_ROI', 'lineCode': 'LP_20190719_004_ROI_0001_P'},
                         {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0001_P'},
                         {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'}]
    """
       datas_APCostCredit用例维度：
       data0：国家New Zealand，季度Q2，Excel中没有匹配的数据；
       data1:国家Australia，季度Q1
       data2:国家为ROI，季度是Q4，Excel筛选结果的数据是0
       data3:国家Vietnam，季度Q2
       data4:国家Australia，季度Q3
       data5:国家Australia，季度Q1
       data6:区域Taiwan，季度Q3
       """
    datas_CountryAdjustment= [{'portfolioNo': 'LP_20190719_004_ROI', 'lineCode': 'LP_20190719_004_ROI_0001_P'},
                              {'portfolioNo': 'LP_20190530_036_VN', 'lineCode': 'LP_20190530_036_VN_0002_P'},
                              {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'},
                              {'portfolioNo': 'LP_20190723_009_BR', 'lineCode': 'LP_20190723_009_BR_0006_P'}]
    """
           datas_CountryAdjustment用例维度：EMEA不用支持显示
           data0：季度Q1,为了验证AP_RTM和Prodcut_category为ALL的四种状态加的用例
           data1:国家为ROI，季度是Q4，Excel筛选结果的数据是0
           data2:国家Vietnam，季度Q2,Excel中没有匹配的数据；
           data3:国家Australia，季度Q3
           data4:国家Panama，季度Q1
           data5:区域Taiwan，季度Q3
           data6:国家Brazil，季度Q3	
           """
    datas_UnitFunding = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                        {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                        {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'},
                        {'portfolioNo': 'LP_20190723_009_BR', 'lineCode': 'LP_20190723_009_BR_0006_P'}]
    """
           datas_UnitFunding用例维度：
           data0：国家Germany，季度Q1
           data1:国家为Canada，季度是Q2
           data2:国家Germany，季度Q4
           data3:国家Panama，季度Q1
           data4:区域Taiwan，季度Q3，为了验证AP_RTM和Prodcut_category为ALL的四种状态加的用例
           data5:国家Brazil，季度Q3	
               """
    datas_nonBMCUplift = [{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                        {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                        {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'},
                        {'portfolioNo': 'LP_20190723_009_BR', 'lineCode': 'LP_20190723_009_BR_0006_P'}]
    """
           datas_nonBMCUplift用例维度：
           data0：国家Germany，季度Q1
           data1:国家为Canada，季度是Q2
           data2:国家Germany，季度Q4
           data3:国家Panama，季度Q1
           data4:区域Taiwan，季度Q3，为了验证AP_RTM和Prodcut_category为ALL的四种状态加的用例
           data5:国家Brazil，季度Q3	
           """
    datas_PNAssessment=[{'portfolioNo': 'LP_20190502_180_DE', 'lineCode': 'LP_20190502_180_DE_0001_P'},
                        {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                        {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'},
                        {'portfolioNo': 'LP_20190723_159_FR', 'lineCode': 'LP_20190723_159_FR_00008_G'}]
    """
           datas_CountryAdjustment用例维度：
           data0：季度Q1
           data1:国家为ROI，季度是Q4，Excel筛选结果的数据是0
           data2:国家Canada，季度Q2；
           data3:国家Germany，季度Q4
           data4:国家Panama，季度Q1
           data5:区域Taiwan，季度Q3
           data6:国家Brazil，季度Q3
           """

    datas_BMC_Cost_W_Fundings = [{'portfolioNo': 'LP_20190909_003_SG', 'lineCode': 'LP_20190909_003_SG_0002_P'},
                                 {'portfolioNo': 'LP_20190722_207_DE', 'lineCode': 'LP_20190722_207_DE_0008_P'},
                                 {'portfolioNo': 'LP_20190909_001_TW', 'lineCode': 'LP_20190909_001_TW_0001_P'}]
    """
           datas_BMC_Cost_W_Fundings用例维度：
           data0：季度Q1
           data1:国家为Singapore，季度是Q4
           data2:国家Canada，季度Q2；
           data3:国家Germany，季度Q4
           data4:国家Panama，季度Q1
           data5:区域Taiwan，季度Q3
           """
    datas_GrossTMCCost= [{'portfolioNo': 'LP_20190722_212_CA', 'lineCode': 'LP_20190722_212_CA_0001_P'},
                        {'portfolioNo': 'LP_20190719_010_INOS', 'lineCode': 'LP_20190719_010_INOS_0001_P'},
                        {'portfolioNo': 'LP_20190719_133_IN', 'lineCode': 'LP_20190719_133_IN_0001_P'},
                        {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'}]
    """
               datas_UnitFunding用例维度：
               data0:国家为Canada，季度是Q4
               data1:region是INDIA，季度Q3
               data2:国家ROI，季度Q2
               data3:国家Australia，季度Q1
               data4:区域Germany，季度Q2
               data5:国家Brazil，季度Q3
               data6:国家Panama，季度Q1
               """
    datas_NetTMCCost = [{'portfolioNo': 'LP_20190722_212_CA', 'lineCode': 'LP_20190722_212_CA_0001_P'},
                        {'portfolioNo': 'LP_20190719_010_INOS', 'lineCode': 'LP_20190719_010_INOS_0001_P'},
                        {'portfolioNo': 'LP_20190719_133_IN', 'lineCode': 'LP_20190719_133_IN_0001_P'},
                        {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'}]
    """
               datas_UnitFunding用例维度：
               data0:国家为Canada，季度是Q4
               data1:region是India Offshore，季度Q3
               data2:region是India Onshore，季度Q4
               data3:国家ROI，季度Q2
               data4:国家Australia，季度Q1
               data5:区域Germany，季度Q2
               data6:国家Brazil，季度Q3
               data7:国家Panama，季度Q1
               """
    datas_GrossBMCCost = [{'portfolioNo': 'LP_20190722_212_CA', 'lineCode': 'LP_20190722_212_CA_0001_P'},
                          {'portfolioNo': 'LP_20180530_053_INOS', 'lineCode': 'LP_20180530_053_INOS_0002_P'},
                          {'portfolioNo': 'LP_20190529_211_DE', 'lineCode': 'LP_20190529_211_DE_0001_P'},
                          {'portfolioNo': 'LP_20190722_190_UY', 'lineCode': 'LP_20190722_190_UY_0001_P'},
                          {'portfolioNo': 'LP_20190909_002_TR', 'lineCode': 'LP_20190909_002_TR_0001_P'}]
    """
               datas_UnitFunding用例维度：
               data0:国家为Canada，季度是Q4
               data1:GEO是AP,国家是India Offshore，季度Q3
               data2:GEO是AP，国家ROI，季度Q2
               data3:GEO是AP，国家Australia，季度Q1
               data4:国家Germany，季度Q2
               data5:Region是LAS,Sales mode是Offshore，国家Panama
               data5:Region是LAS,Sales mode是Onshore，国家Uruguay
               data6:国家Turkey，季度Q3
               """
    datas_CountryAdjustment2 = [{'portfolioNo': 'LP_20190719_004_ROI', 'lineCode': 'LP_20190719_004_ROI_0001_P'},
                                {'portfolioNo': 'LP_20190530_034_VN', 'lineCode': 'LP_20190530_034_VN_0001_P'},
                                {'portfolioNo': 'LP_20190717_007_AU', 'lineCode': 'LP_20190717_007_AU_0001_P'},
                                {'portfolioNo': 'LP_20190719_007_JP', 'lineCode': 'LP_20190719_007_JP_0001_P'}]
    """
           datas_CountryAdjustment用例维度：EMEA不用支持显示
           data0：季度Q2,为了验证AP_RTM和Prodcut_category为ALL的四种状态加的用例
           data1:国家为ROI，季度是Q4
           data2:国家Vietnam，季度Q2,Excel中没有匹配的数据；
           data3:国家Australia，季度Q3
           data4:国家Australia，季度Q1
           data5:区域Japan，季度Q4，Excel筛选结果的数据是0
           data6:国家Brazil，季度Q3	,展示未加该数据
           """


    # #数据维护
    # datas_portfolio=[{'CostFundingDataName':'datas_GEOFundingOthers1','Country':'Argentina','Product_Group':'NB','Plan_Cycle':1,'Portfolio_Name':Portfolio_Name},
    #                  {'CostFundingDataName':'datas_GEOFundingOthers1','Country':'Brazil','Product_Group':'NB','Plan_Cycle':1,'Portfolio_Name':Portfolio_Name},
    #                  {'CostFundingDataName':'datas_Funding3_Others','Country':'Brazil','Product_Group':'NB','Plan_Cycle':1,'Portfolio_Name':Portfolio_Name}]
