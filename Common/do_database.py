from pymssql import connect
from TestDatas.common_datas import CommonDatas as cd
class DoMysql:
    def do_mysql(self,query_sql,state='all'):
        # db_config=()
        # 创建数据库连接
        cnn = connect(server=cd.data_base_conf['server'], user=cd.data_base_conf['user'], password=cd.data_base_conf['password'],database=cd.data_base_conf['database'])
        # 创建游标
        cursor = cnn.cursor()
        # 执行sql语句
        cursor.execute(query_sql)

        # 获取结果
        if state == 1:
            res = cursor.fetchone()  # 元组——针对一条数据
        else:
            res = cursor.fetchall()  # 列表嵌套元组——针对多行数据

        cursor.close()
        cnn.close()

        return res

if __name__ == '__main__':
 s=DoMysql().do_mysql(55)[0][0]
 print(type('%.2f' %(3)))
 print(float(3.13))
 print(s)
