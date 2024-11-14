
import pymysql

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

    def insert(self, sql, *args):
        """

        :param sql:
        :param args: 插入一条数据
        :return:
        """
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            self.connection.commit()
            logger.info("插入的数据是: {},对应的值是: {}".format(sql,args))
        except Exception as ex:
            logger.error('数据插入失败的原因可能是：{}'.format(ex))
        finally:
            self.close()

    def inserts(self, sql, *args):
        """

        :param sql:
        :param args: 插入多条数据
        :return:
        """
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.executemany(query=sql,args=args)
            self.connection.commit()
            logger.info("插入的数据是: {},对应的值是: {}".format(sql, args))
        except Exception as ex:
            logger.error('数据插入失败的原因可能是：{}'.format(ex))
        finally:
            self.close()

    def update(self, sql, *args):
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            self.connection.commit()
            logger.info("更新的数据是: {}".format(sql,args))
        except Exception as ex:
            logger.error('数据更新失败的原因可能是：{}'.format(ex))
        finally:
            self.close()
            # logger.info("资源以释放，数据库已关闭")


    def delete(self, sql, *args):
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            self.connection.commit()
            # logger.info("删除的数据是: {}".format(sql))
            logger.debug("删除的数据SQL是: {}，删除的条件是: {}".format(sql,args))
        except Exception as ex:
            logger.error('数据删除失败的原因可能是：{}'.format(ex))
        finally:
            self.close()
            # logger.info("资源以释放，数据库已关闭"



    def delete_one(self, sql):
        try:
            self.connection = pymysql.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql)
            self.connection.commit()
            # logger.info("删除的数据是: {}".format(sql))
            logger.debug("删除的数据SQL是: {}".format(sql))
        except Exception as ex:
            logger.error('数据删除失败的原因可能是：{}'.format(ex))
        finally:
            self.close()
            # logger.info("资源以释放，数据库已关闭"

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()



mysqlutil = MysqlUtil()


sql  = """SELECT `mg_id`
FROM `sp_manager` 

"""

# sql = " INSERT INTO `sp_manager` (`mg_name`, `mg_pwd`, `mg_mobile`, `mg_email`, `mg_time`, `role_id`, `mg_state`) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# valus = (get_name(), get_random(), get_phone(), get_email(), 1729928045, 1,None )
# a = """
#  INSERT INTO `sp_manager` (`mg_name`, `mg_pwd`, `mg_mobile`, `mg_email`, `mg_time`, `role_id`, `mg_state`) VALUES
#   ('谢玉兰', '$2y$10$TemKQjH0.gpv2OfzaS4Ow.9IF8ya94Hi/ldgsrEZrhk/RR4vSPcJK', '18032040387', 'yong45@example.com', 1729928045, -1, NULL)
# """

# b = "DELETE FROM sp_manager WHERE mg_name = '谢玉兰' "
# c = " UPDATE sp_manager SET mg_pwd = 123456  WHERE mg_name = '谢玉兰' "

# # mysqlutil.insert(a)
# mysqlutil.update(c)
# from common.debug import *
# mysqlutil.delete(f,(delete_userid()))
# sql_q = "INSERT INTO sp_manager (mg_id, mg_name, mg_pwd, mg_time, role_id, mg_mobile, mg_email, mg_state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
# args = [(992,"jhhh","ksdksdks@.com",1486720211,1,154545455,"ksdksdks@.com",True),
#         (993,"get_name","ksdksdks@.com",1486720211,1,154545455,"ksdksdks@.com",True)
#         ]
# mysqlutil.inserts(sql_q,args)
