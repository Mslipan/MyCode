import pymysql

class ConnectMysql():

    def __init__(self,db_info):
        '''连接数据库
        :arg  db_info 数据库的配置信息
        '''
        # 连接数据库pymysql.connect(host='49.235.92.12',port=3306,)
        self.db = pymysql.connect(**db_info)

        # 创建游标
        self.cur = self.db.cursor()

    def select_mysql(self,sql):
        '''查询数据库
        :arg sql 查询数据的sql
        '''

        self.cur.execute(sql)#执行sql

        select_data = self.cur.fetchall() #获取值

        return select_data

    def execute_mysql(self,sql):
        '''新增，删除，更新
        :arg sql sql语句
        '''

        self.cur.execute(sql)

        #进行提交
        self.db.commit()

    def close(self):
        self.db.close()

if __name__ == "__main__":
    db_info = {
        "host": "49.235.92.12",
        "user": "root",
        "password": "123456",
        "port": 3309,
        "db":"apps"
    }
    sql = "SELECT * from auth_user WHERE username='test';"
    select_data = ConnectMysql(db_info).select_mysql(sql)
    print(select_data[0])


