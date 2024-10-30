import requests


from utils.logutil import logger
from config.read_environment import *


class  SenApi():

    def __init__(self):
        self.request=requests.Session()

    def get_method(self,path,params=None,headers=None):
        url = get_host() + path
        headers = get_headers()
        res = self.request.get(url=url,params=params,headers=headers)
        logger.info('请求的url是: {}'.format(url))
        logger.info('请求的headers是: {}'.format(headers))
        logger.info('请求的数据是: {}'.format(params))
        return res


    def post_method(self, path, data=None, json=None,headers=None):
        url = get_host() + path
        headers = get_headers()
        res = self.request.post(url=url, data=data, json=json, headers=headers)
        logger.info('请求的url是: {}'.format(url))
        logger.info('请求的headers是: {}'.format(headers))
        logger.info('请求的数据是: {}'.format(data))
        return res

    # 请求方法put
    def put_method(self, path, data=None, headers=None):
        url = get_host() + path
        headers = get_headers()
        if headers is not None:
            res = self.request.put(url, json=data, headers=headers)
            logger.info('请求的url是: {}'.format(url))
            logger.info('请求的headers是: {}'.format(headers))
            logger.info('请求的数据是: {}'.format(data))
        else:
            res = self.request.delete(url, json=data)
            logger.info('请求的url是: {}'.format(url))

            logger.info('请求的数据是: {}'.format(data))
        return res

    # 请求方法delete
    def delete_method(self, path, data=None, headers=None):
        url = get_host() + path
        headers = get_headers()
        if headers is not None:
            res = self.request.delete(url, json=data, headers=headers)
            logger.info('请求的url是: {}'.format(url))
            logger.info('请求的headers是: {}'.format(headers))
            logger.info('请求的数据是: {}'.format(data))
        else:
            res = self.request.delete(url, json=data)
            logger.info('请求的url是:{}'.format(url))
            logger.info('请求的headers是:{}'.format(headers))
            logger.info('请求的数据是:{}'.format(data))
        return res


    def send(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        if method == 'get' or method == 'GET':
            res = self.get_method(url,params=params,headers=headers)
        elif method == 'post' or method == 'POST':
            res = self.post_method(url, data=data, json=json,headers=headers)
        elif method == 'put' or method == 'PUT':
            res = self.put_method(url, data=data, headers=headers)
        elif method == 'delete' or method == 'DELETE':
            res = self.delete_method( url, data=data, headers=headers)
        else:
            logger.error("你的请求方式不正确！错误的方式是{}".format(method))

        return res


# if __name__ == '__main__':
#     sed = SenApi()
#     url = 'http://127.0.0.1:8888/api/private/v1/login'
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#     data = {'username': 'admin',
#             'password': 123456}
#     a = sed.send(method='post',path='/api/private/v1/login',headers=headers,data=data)
#     v = get_response_text(a.text,'msg')
#     assert_tet(a.json()['meta']['msg'],v)
#     print(a.json())



