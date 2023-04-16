import os
from typing import Text

DB_CONFIG = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'database':'api_server',
    'port':3306,
    'charset':'utf8'
}
Environment='test_environment'

project_path = os.path.dirname(os.path.dirname(__file__))

def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return project_path + path





def get_long_path():
    log_path = ensure_path_sep('/log')
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    else:
        pass
    return log_path

