import yaml

from common.setting import ensure_path_sep


data =[

    {'case_name': '用例名称',
     'method': '接口请求方法',
     'is_run': True,
     'path': '接口请求路径',
     'data': {'参数1': 2310,"参数2": "value"},
     'result': {'msg': '校验接口数据，做断言使用'}
     }

]




class CaceTemplate():


    def write_cacetemplate_yaml(slef,path, data):

        with open(path, mode='w', encoding='utf-8') as f:
            value = yaml.dump(data, stream=f, allow_unicode=True)
            f.close()
        return value

if __name__ == '__main__':
    CaceTemplate = CaceTemplate()
    CaceTemplate.write_cacetemplate_yaml(ensure_path_sep('/datas/excel/cacetemplate.yaml'),data)

