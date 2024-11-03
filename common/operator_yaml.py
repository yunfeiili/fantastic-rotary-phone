import random

import yaml

from utils.mysqlutil import mysqlutil, sql


def read_yaml(flie_path):
    '''
    读取文件内容
    :param flie_path:
    :return:
    '''
    with open(flie_path, encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.FullLoader)
        f.close()
    return value


def write_yaml(path,data):
    '''
    写入文件内容
    :param data:
    :param path:
    :return:
    '''
    with open(path, mode='w+', encoding='utf-8') as f:
        value = yaml.dump(data, stream=f, allow_unicode=True)
        f.close()
    return value


def clear_yaml(path):
    '''
    清空文件内容
    :param path:
    :return:
    '''
    with open(path, mode='w', encoding='utf-8') as f:
        value = f.truncate()
        return value


def delete_userid():
    '''
    获取数据库中用户id
    :return:
    '''
    u_is = []
    for i in mysqlutil.getList(sql):
        if i[0] !=500 and i[0] !=502:
            u_is.append(i[0])
    a = random.choice(u_is)
    return a


# if __name__ == '__main__':
#     sqlss = "DELETE FROM sp_manager WHERE mg_id = %s"
#     print(delete_userid())
#     mysqlutil.delete(sqlss,(delete_userid()))