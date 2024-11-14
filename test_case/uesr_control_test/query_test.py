import allure

from common.write_case_result_data import wr
from datas.sqlshuju.query_sql import *
from utils.logutil import logger


import pytest

from common.debug import get_response_text
from common.read_case_data import read_case_dataall
from test_case import Test
from utils.asst import assert_tet
from utils.mysqlutil import mysqlutil

@allure.parent_suite("查询数据")
class Test_api_query(Test):

    @allure.suite("查询返回多条数据")
    # @allure.sub_suite("更具条件返回对应数据")
    @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/query.yaml.yaml'))
    def test_query(self,case):
        logger.info("请求的用例名称是: {}".format(case["case_name"]))
        re = self.sendRequests.send(method=case['method'],url=case['path'],params=case['data'])
        texts = get_response_text(re.text,'msg')
        assert_tet(case['result']['msg'],texts)

    @allure.suite("根据已有用户id查询")
    @allure.sub_suite("已有id")
    @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/queryid.yaml'))
    def test_query_id(self,case):
        logger.info("请求的用例名称是: {}".format(case["case_name"]))
        re = self.sendRequests.send(method=case['method'],url=case['path'],params=case['data'])
        texts = get_response_text(re.text,'msg')
        assert_tet(case['result']['msg'],texts)

    @allure.title("case")
    # @allure.description("描述阿森纳大家萨迪克")
    @allure.suite("sql插入数据")
    @allure.sub_suite("查询SQL插入的数据")
    @pytest.mark.parametrize('case', read_case_dataall('/datas/uesrquery/queryid_sql.yaml'))
    def test_query_sql_id(self, case):
        logger.info("请求的用例名称是: {}".format(case["case_name"]))
        allure.dynamic.title(case["case_name"])
        mysqlutil.insert(query_id)
        re = self.sendRequests.send(method=case['method'], url=case['path'], params=case['data'])
        wr.writresult("/datas/uesrquery/queryid_sql.yaml", re.json(), is_writ=False)
        mysqlutil.delete_one(delete_id)
        texts = get_response_text(re.text, 'msg')
        assert_tet(case['result']['meta']['msg'], texts)

 




