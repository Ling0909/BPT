class DatasStor:
    baseInfo={}
    """
        :return: 示例：baseInfo={'GEO': 'EMEA', 'Region': 'DACH', 'COUNTRY': 'Germany', 'AP_RTM': 
                                '2', 'PRODUCT_GROUP': 'NB', 'PRODUCT_CATEGORY': 'Lenovo NB', 
                                'PRODUCT_SERIES': 'V Series', 'PRODUCT_FAMILY': 'V145-15AST',
                                 'Component V': ['BLACK 45W 2-PIN', 'NO', '2CELL 30WH', 
                                 '0.3 MEGA WITH SINGLE MIC', 'NONE', 'BLACK', 'GERMANY', 
                                 'A4-9125', '100/1000M', 'NO FINGERPRINT', '1TB 7MM 5400RPM', 
                                 'HDMI', 'KB GERMAN', 'GERMAN', '15.6 HD TN AG 200N', 
                                 'LENOVO V145-15AST', 'SINGLE', 'NO NFC', 
                                 '9.0MM SUPER MULTI(TRAY IN)', 'NO OFFICE', 'FREE-DOS',
                                  '4G(1X4GBDDR4 1866)', 'NO SSD', 'TEXTURE', 'INTEGRATED',
                                   'N01_1YEAR_DEP_CI_IPSTD', 'YES', 'WIFI 1X1 AC+BT4.1'], 
                                   'Channel Price($)': '153.15'}
    
    """
    # CostFunding_ValueDict={}#页面中的对应数据值={'GEO Funding(MOU) ($)': '8.00', 'SEP.': '7.00', 'OCT.': '8.00', 'NOV.': '9.00'}
    monthDict_on_portfolioPage={}#月份字典，page_portfolioPlan模块下getExcelMonthBySystem（）函数生成
    nrowdict=[]
    Plan_Cycle=''
    #存储添加的portfolio数据
    datas_GEOFundingOthers1 = []
    datas_region_isLAS = []
    datas_GEOFundingOthers2 = []
    datas_GEOFundingOthers3 = []
    datas_GEOFundingOthers4 = []
    datas_Funding1_CPU = []
    datas_Funding2_HDD_SSHD_SSD = []
    datas_Funding3_Others = []

    datas_portfolio_new=[]#
