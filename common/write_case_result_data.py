import yaml

from common.read_case_data import read_case_dataall
from common.setting import ensure_path_sep


class WriteresultData():

    def writresult(self,casepath,result,is_writ=False):
        '''

        :param casepath: 用例路径
        :param result: 结果
        :param is_writ: is_writ=False不更新接口返回结果，Ture时把接口返回的数据写入用例的result下
        :return:
        '''
        # datas = read_case_dataall(casepath)
        datas = read_case_dataall(casepath)
        for data in datas:
            data["result"] = result
        if is_writ:
            with open(ensure_path_sep(casepath), "w", encoding="utf-8") as f:
                yaml.dump(datas, stream=f, allow_unicode=True,)

        return datas


wr = WriteresultData()




