import json
import random
import string

import jsonpath
from faker import Faker

from utils.mysqlutil import mysqlutil, sql

faker = Faker('zh_CN')
'''
zh_CN（简体中文）、zh_TW（繁体中文）、zh_TW（台湾）、en_US（美国英文）、en_GB（英国英文）、de_DE（德文）、ja_JP（日文）、ko_KR（韩文）、fr_FR（法文）
'''
def get_random():
    """生成一串6位数的字符+数组混合的字符串"""
    number = string.ascii_letters + string.digits
    number_n = ''.join(random.sample(number, 6))
    return number_n



def create_string_number(n=9):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

def rand_str():
    ''' 随机生成1000000到2000000数据 '''
    return str(random.randint(1000000, 2000000))

def  numbers():
    '''生成随机的电话号码 '''
    q = [134,133,135,136,137,138,139,150,151,152,157,158,159,182,183,
    184,187,188,147,178,130,131,132,155,156,145,185,186,176,175,
    133,153,180,181,189,177,173,149]
    e = random.choice(q)
    w = int(''.join(random.sample(string.digits,8)))
    return '{}{}'.format(e,w)



def get_name():
    '''
    :return: 随机生成一个中文名称
    '''
    return faker.name()

def get_email():
    '''

    :return: 随机获取电子邮箱
    '''
    return faker.email()

def get_text():
    '''

    :return: 随机获取一段文本
    '''
    return faker.text()


def get_phone():
    '''
    :return: 返回随机的手机号
    '''
    return faker.phone_number()


    # 获取指定内容
def get_response_text(res,key):
    '''
    获取文本中指定的内容
    :param res: 文本
    :param key: 取对应的value值
    :return:
    '''
    try:
        text = json.loads(res)
        value = jsonpath.jsonpath(text,'$..{}'.format(key))
        if value:
            if len(value) == 1:
                return value[0]
            return value
        return value
    except:
        return None


def get_userid():
    '''
    获取数据库中用户id
    :return:
    '''
    u_is = []
    for i in mysqlutil.getList(sql):
        if i[0] !=500:
            u_is.append(i[0])
    a = random.choice(u_is)
    return a
if __name__ == '__main__':
    print(get_userid())