import os
import time
#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
base_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#获取顶级目录结构
get_time=time.strftime("%Y_%m_%d_%H-%M-%S", time.localtime())#打印当前时间

#打印日志的路径地址
log_path=os.path.join(base_path,'OutPuts','logs','logs-{0}.txt'.format(get_time))

#生成测试报告的地址
report_path=os.path.join(base_path,'OutPuts','reports','HtmlReport-{0}.html'.format(get_time))

#截取图片地址（出现错误时）
screen_path=os.path.join(base_path,'OutPuts','ScreenShots')

files_upload=os.path.join(base_dir,"Outputs/data_files/file.xlsx")

file_create_portfoliio=os.path.join(base_path,'TestDatas/stor_data/create_portfolio_datas.xlsx')


