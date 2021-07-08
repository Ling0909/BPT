class CommonDatas:
    #登录模块配置信息
    #AUT测试环境
    # login_url='http://10.99.244.176/index.aspx'
    # login_username='zhangpf5'
    # login_password='zpf000000$'
    #SIT开发环境
    login_url = 'http://10.64.190.32/'   # http://10.64.190.46/
    login_username = 'liugz3'
    login_password = 'zZ888888'

    #进入菜单的信息
    menuName=[{'MainMenu':'SMB','NameMenuLeve1':'Data Maintenance','NameMenuLeve2':'Policy List'},
              {'MainMenu':'SMB','NameMenuLeve1':'Business Plan','NameMenuLeve2':'Country Portfolio & Plan'},
              {'MainMenu':'CPM','NameMenuLeve1':'Funding Management'},
              {'MainMenu':'Consumer','NameMenuLeve1':'Business Plan','NameMenuLeve2':'Country Portfolio & Plan'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Business Plan', 'NameMenuLeve2': 'Business Plan Summary'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Business Plan', 'NameMenuLeve2': 'Business Plan Approval'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Execution Plan', 'NameMenuLeve2': 'Exec Portfolio & Plan'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Execution Plan', 'NameMenuLeve2': 'Execution Plan summary'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Execution Plan', 'NameMenuLeve2': 'Execution Plan Approval'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Execution Plan', 'NameMenuLeve2': 'Deal Simulation'},
              {'MainMenu':'Consumer','NameMenuLeve1': 'Execution Plan', 'NameMenuLeve2': 'Deal Approval'}
              ]
    '''
    执行自动化国家及产品组
    AP: Hongkong NB; Korea Tablet; Taiwan  Option; Japan Mobile Gaming
    EMEA: Germany NB; Nordic DT; France Tablet; United Kingdom Mobile Gaming
    LAS: Mexico NB; Brazil DT; Peru Option
    United States of America : NB DT Option
    Deal的
    United Kingdom ： NB & DT & Option & Visual
    Sweden: NB & DT & Option & Visual
    '''
    portfolio=[{'CountryGroup':'HongKong','ProductGroup':'NB','PlanCycle':'FY21/22Q2',
                'PortfolioType':'Channel','PortfolioName':'auto_HongKong_NB'},
               {'CountryGroup': 'Korea', 'ProductGroup': 'Tablet', 'PlanCycle':'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Korea_Tablet'},
               {'CountryGroup': 'Taiwan', 'ProductGroup': 'Option', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Taiwan_Option'},
               {'CountryGroup': 'Japan', 'ProductGroup': 'Mobile Gaming', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Japan_MobileGaming'},
               {'CountryGroup': 'Germany', 'ProductGroup': 'NB', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Germany_NB'},
               {'CountryGroup': 'Nordic', 'ProductGroup': 'TDT/AIO', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Nordic_TDT_AIO'},
               {'CountryGroup': 'France', 'ProductGroup': 'Tablet', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_France_Tablet'},
               {'CountryGroup': 'United Kingdom', 'ProductGroup': 'Mobile Gaming', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_UnitedKingdom_MobileGaming'},
               {'CountryGroup': 'Mexico', 'ProductGroup': 'NB', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Mexico_NB'},
               {'CountryGroup': 'Brazil', 'ProductGroup': 'TDT/AIO', 'PlanCycle': 'FY21/22Q2',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Brazil_TDT_AIO'},
               {'CountryGroup': 'Peru', 'ProductGroup': 'Option', 'PlanCycle': 'FY21/22Q1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_Peru_Option'},
               {'CountryGroup': 'United States of America', 'ProductGroup': 'NB', 'PlanCycle': '2021 Cycle 1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_UnitedStates_ofAmerica_NB'},
               {'CountryGroup': 'United States of America', 'ProductGroup': 'TDT/AIO', 'PlanCycle': '2021 Cycle 1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_UnitedStates_ofAmerica_TDT_AIO'},
               {'CountryGroup': 'United States of America', 'ProductGroup': 'Option', 'PlanCycle': '2021 Cycle 1',
                'PortfolioType': 'Channel', 'PortfolioName': 'auto_UnitedStates_ofAmerica_Option'}
              ]
    deal=[{'CountryGroup':'United Kingdom'},{'CountryGroup':'Sweden'}]

    deal_mtm=[{'PN':'81YM000YUK', 'CountryGroup':'United Kingdom','Product Group':'NB'},
              {'PN':'F0FB000QUK', 'CountryGroup':'United Kingdom','Product Group':'TDT'},
              {'PN':'GX40M52027', 'CountryGroup':'United Kingdom','Product Group': 'Option'},
              {'PN':'65DEKAC1UK', 'CountryGroup':'United Kingdom','Product Group': 'Visual'},

              {'PN': '81YM000YUK', 'CountryGroup': 'Sweden', 'Product Group': 'NB'},
              {'PN': 'F0FB000QUK', 'CountryGroup': 'Sweden', 'Product Group': 'TDT'},
              {'PN': 'GX40M52027', 'CountryGroup': 'Sweden', 'Product Group': 'Option'},
              {'PN': '65DEKAC1UK', 'CountryGroup': 'Sweden', 'Product Group': 'Visual'}
    ]

    mtm=[{'PN':'81WF004RHH','CountryGroup':'HongKong'},
         {'PN':'ZA190046KR','CountryGroup':'Korea'},
         {'PN':'ZG38C01504','CountryGroup':'Taiwan'},
         {'PN': 'PAG50048JP', 'CountryGroup': 'Japan'},
         {'PN': '81VU007CGE', 'CountryGroup': 'Germany'},
         {'PN': 'F0E7001VMT', 'CountryGroup': 'Nordic'},
         {'PN': 'ZA550050SE', 'CountryGroup': 'France'},
         {'PN': 'PAG50055GB', 'CountryGroup': 'United Kingdom'},
         {'PN': '81N600A0LM', 'CountryGroup': 'Mexico'},
         {'PN': 'F0E8004XBP', 'CountryGroup': 'Brazil'},
         {'PN': 'GY40T26478', 'CountryGroup': 'Peru'},
         {'PN': '81TE0003US', 'CountryGroup': 'United States of America'},
         {'PN': 'F0E5003BUS', 'CountryGroup': 'United States of America'},
         {'PN': '40AN0135US', 'CountryGroup': 'United States of America'}
         ]

    CheckData_Country = [{'Region/Country':'Ukraine', 'Plan Cycle':'FY20/21Q4'},
                         {'Region/Country':'Mexico', 'Plan Cycle':'FY20/21Q4'},
                         {'Region/Country': 'Taiwan', 'Plan Cycle': 'FY20/21Q4'}
                         ]

    ProductGroup = ['NB', 'TDT/AIO', 'Tablet', 'Option']

    #wwreport筛选框相关数据
    ww_CountryGroup=['HongKong','Korea','Taiwan','Japan','Germany','Nordic','France','United Kingdom',
                     'Mexico','Brazil','Peru','United States of America']
    ww_Quarter=['FY20/21Q1','FY20/21Q2','FY20/21Q3','FY20/21Q4','FY21/22Q1','FY21/22Q2','FY21/22Q3']
    ww_PlanType=['Business Plan','Execution Plan','Deal','Business & Execution Plan']
    ww_ProductGroup=['NB','TDT/AIO','Tablet','Smart Device','Visual','Option','Service','Workstation','Mobile Gaming']
    ww_PortfolioType=['To be Approved','All Portfolios']
    ww_Version=['All','Latest Approved','Latest Version']

    #server数据库配置信息
    #UAT测试环境
    # data_base_conf = {'server': "10.99.244.177", 'user': "sa", 'password': "abcd-1234", 'database': "CBT_III"}

   #develop开发环境
    data_base_conf={'server': "10.111.110.122:8900", 'user': "sa", 'password': "Password01!", 'database': "CBT_PRD"}
