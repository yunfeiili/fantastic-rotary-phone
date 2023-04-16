
import pymysql,random

from common.setting import DB_CONFIG
from utils.logutil import logger


class MysqlUtil():



    def __init__(self):
        self.connection = None
        self.cursor = None


    def getOne(self, sql, *args):
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as ex:
            logger.error('查询单条数据失败失败原因可能是：{}'.format(ex))

        finally:
            self.close()
            # logger.info("资源以释放，数据库已关闭")

        # 从数据库表中查询多行数据
    def getList(self, sql, *args):
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return list(self.cursor.fetchall())
        except Exception as ex:
            logger.error('查询所有数据失败失败原因可能是：{}'.format(ex))
        finally:
            self.close()
            # logger.info("资源以释放，数据库已关闭")


    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()



mysqlutil = MysqlUtil()


sql  = """SELECT `mg_id`
FROM `sp_manager` 

"""



