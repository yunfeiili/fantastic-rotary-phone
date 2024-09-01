import time

import requests

URL = "http://127.0.0.1:8888/api/private/v1/login"
data = {
    "username": "admin",
    "password": "123456"
}
headers = {
    "Content-Type": "null",
    "accept-language":"zh-CN,zh;q=0.9",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,likeGecko) Chrome/104.0.0.0 Safari/537.36",
}


# res = requests.post(url=URL,json = data)
# print(res.json())
# print(res.text)
a = requests.request(method="post",url=URL,json = data)
print(a.text)




