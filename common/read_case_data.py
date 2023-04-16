
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


def read_case_dataall(path):
    '''
    执行is_run不为false的用例
    :param path: 测试用例的路劲
    :return: 返回is_run需要执行的用例数列表
    '''
    cases = yaml.safe_load(render(ensure_path_sep(path),**all_functions()))
    case_data=[]
    for case in cases:
        if case.get('is_run') != False:
            case_data.append(case)
    return case_data

def read_case_data_name(path,YamlCaseName=None):
    '''
    指定用例名称运行一条用例
    :param path: 测试用例的路劲
    :return: 返回is_run需要执行的用例数列表
    '''
    cases = yaml.safe_load(render(ensure_path_sep(path),**all_functions()))
    case_data=[]
    for case in cases:
        if  YamlCaseName == case.get('case_name'):
            case_data.append(case)
    return case_data


# if __name__ == '__main__':
#     a = read_case_dataall('\datas\logon.yaml')[0]
#     YamlCaseName = a.get('case_name')
#     q = read_case_data_name('\datas\logon.yaml',YamlCaseName='登录接口')
#     print(q)