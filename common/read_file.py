

import yaml


# from common.operation_excle import operation_excle
from pathlib import Path


class ReadFile:
    config_dict = None
    config_path = f"{str(Path(__file__).parent.parent)}/config/config.yaml"

    @classmethod
    def get_config_dict(cls,) -> dict:
        """读取配置文件，并且转换成字典
        return cls.config_dict
        """
        if cls.config_dict is None:
            # 指定编码格式解决，win下跑代码抛出错误
            with open(cls.config_path, "r", encoding="utf-8") as file:
                cls.config_dict = yaml.load(file.read(), Loader=yaml.FullLoader)
        return cls.config_dict

    @classmethod
    def get_case_data_yaml(cls,case_data_yaml) -> dict:
        """读取配置文件，并且转换成字典
        return cls.config_dict
        """
        with open(case_data_yaml, "r", encoding="utf-8") as file:
            data_yaml_dict = yaml.load(file.read(), Loader=yaml.FullLoader)

        return data_yaml_dict


    @classmethod
    def read_config(cls, expr: str = ".") -> str:
        """默认读取config目录下的config.yaml配置文件，根据传递的expr jsonpath表达式可任意返回任何配置项
        :param expr: 提取表达式, 使用jsonpath语法,默认值提取整个读取的对象
        return 根据表达式返回的值
        """
        from common.exchange_data import ExchangeData
        return ExchangeData.Extract_noe(cls.get_config_dict(), expr)



