import pprint

from common.operator_yaml import *
from common.setting import ensure_path_sep, Environment

environment_path = ensure_path_sep('/config/environment.yaml')

def rade_environmert(token):
    value = read_yaml(environment_path)
    value['test_environment']['headers']['Authorization'] = token
    with open(environment_path, "w", encoding="utf-8") as f:
        yaml.dump(value, f)


def read_config():
    try:
        value = read_yaml(environment_path)
        value = value[Environment]
        return value
    except Exception as e:
        print(f'读取配置环境错误{e}')


def get_host():
    return read_config()['host']


def get_headers():
    return read_config()['headers']

