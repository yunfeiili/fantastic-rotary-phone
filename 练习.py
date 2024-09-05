# import requests
#
# from config.read_environment import *
#
# url = "http://127.0.0.1:8888/api/private/v1/users/500"
# params = {'id': None}
# headers= get_headers()
# re = requests.get(url=url, params=params,headers=headers)
# print(re.text)
from utils.asst import assert_diff
from utils.logutil import *



import os
import jinja2
import importlib
import inspect
from common.setting import ensure_path_sep
import yaml


def render(tpl_path, **kwargs):
    """渲染yml文件"""
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(**kwargs)

def all_functions():
    """加载randoms.py模块"""
    debug_module = importlib.import_module('.debug',package='common')
    all_function = inspect.getmembers(debug_module, inspect.isfunction)
    return dict(all_function)


def read_case(path):
    '''
    执行is_run不为false的用例
    :param path: 测试用例的路劲
    :return: 返回is_run需要执行的用例数列表
    '''
    cases = yaml.safe_load(render(ensure_path_sep(path),**all_functions()))
    case_data=[]
    for case in cases:
        try:
            if case.get('is_run') != False:
                if case["method"]:
                    pass
                    if case["path"]:
                        pass
                case_data.append(case)
        except:
            logger.error("该用例缺少请求方发或者缺少请求地址")
    return case_data



# if __name__ == '__main__':
#     a = read_case('\datas\logon.yaml')
#     # YamlCaseName = a.get('case_name')
#     print( a)



import json
import random
import time
import os

import jsonpath
import requests
# import pywinauto.keyboard
from pywinauto.keyboard import send_keys  # 键盘

def read_txt(path):
    with open(path,mode="r",encoding="utf_8") as f:
        value = f.readlines()
        return random.choice(value)
def get_txt():

    url = "https://v1.hitokoto.cn/"
    res = requests.get(url=url)
    a = json.loads(res.text)
    b = jsonpath.jsonpath(a,"$..{}".format("hitokoto"))
    return b[0]





# while True:
#     time_now = time.strftime("%H:%M", time.localtime())  # 获取当前时间
#     sent_time = time.strftime("14:04", time.localtime())  # 发送时间（这里自己定时间）
#     if time_now != sent_time:  # 当前时间等于发送时间则执行以下程序
#         def open_app(app_dir):
#             os.startfile(app_dir)
#
#
#         # 打开微信
#         if __name__ == "__main__":
#             app_dir = r'D:\WeChat\WeChat.exe'  # 此处为微信的绝对路径
#             open_app(app_dir)
#             time.sleep(1)
#
#         # 进入微信，模拟按键Ctrl+F
#         send_keys('^f')
#         send_keys('苏萧')
#         time.sleep(1)
#         send_keys('{ENTER}')  # 回车键必须全部大小
#         for i in range(10):
#         # 需要发送的消息内容
#             message = get_txt()
#             time.sleep(3)
#             messages= "睡什么睡，起来嗨"
#
#         # 输入聊天内容
#             send_keys(message + messages + ":/t" + str(i))
#         # 回车发送消息
#             send_keys('{ENTER}')
#
#         time.sleep(3)
#
#         print('退出~~~')
#
#         exit()  # 退出程序
#     else:
#         print("不在当前时间")
#         exit()  # 退出程序

from deepdiff import DeepDiff

a = {
    "data": {
        "id": 500,
        "rid": 0,
        "username": "admin",
        "mobile": "12345678",
        "email": "adsfad@qq.com",
        "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE3MjUyODU3MzEsImV4cCI6MTcyNTM3MjEzMX0.Bb5CEbf5vGcxfZA3vxzamJfElPjtk0xRBsemeZ1GG5o"
    },
    "meta": {
        "msg": "登录成功",
        "status": 200
    }
}
b = {
    "data": {
        "id": 500,
        "rid": 0,
        "username": "admin",
        "mobile": "12345678",
        "email": "adsfad@qq.com",
        "token": "Be7arer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE3MjUyODU3MzEsImV4cCI6MTcyNTM3MjEzMX0.Bb5CEbf5vGcxfZA3vxzamJfElPjtk0xRBsemeZ1GG5o"
    },
    "meta": {
        "msg": "登录成功",
        "status": 200
    }
}
# a1 = {"name": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}, "type_": "20"}
# c = {"name": "yanan"}
# c1 = {"name": "yanan"}
# # 字典/json对比

# print(assert_diff(a,b))
# a = {'msg': '登录成功'}  #{'msg': '登录成功'}
# list1 = [{'case_name': '登录接口', 'data': {'password': 123456, 'username': 'admin'}, 'is_run': None, 'method': 'post', 'path': '/api/private/v1/login', 'result': {'msg': '登录成功'}}, {'case_name': '登录接口112', 'data': {'password': 123456, 'username': 'admin'}, 'is_run': None, 'method': 'post', 'path': '/api/private/v1/login', 'result': {'msg': '登录成功1312312'}}]
# print(list1)
# for data in list1:
#     data["result"] = a
#     # print(data)
# print(list1)


t1 = {"for life": "vegan", "ingredients": ["no meat", "no eggs", "no dairy"]}
t2 = {"for life": "vegan", "ingredients": ["veggies", "tofu", "soy sauce"]}

# 指定ingredients这个路径不对比差异

print(DeepDiff(a,b,exclude_paths="root['data']['token']"))
# print(DeepDiff(t1,t2,exclude_paths= "root['ingredients']"))
# print(DeepDiff(t1, t2, exclude_paths="root['ingredients']"))
def asstr_1(rea,exp,xiao):
   valus =  DeepDiff(rea,exp,exclude_paths=xiao)
   return valus



# 也可指定多个路径
# print(DeepDiff(t1, t2, exclude_paths=["root['ingredients']","root['ingredients2']"]))
print(asstr_1(a,b,"root['data']['token']"))


print("SJDKSJJSDKSJ"))
