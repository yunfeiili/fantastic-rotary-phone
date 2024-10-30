


import pytest

from common.debug import get_response_text
from common.operator_yaml import delete_userid
from common.read_case_data import read_case_dataall
from datas.sqlshuju.query_sql import delete_id_sql
from test_case import Test
from utils.asst import assert_tet
from utils.logutil import logger
from utils.mysqlutil import mysqlutil


class Test_api_add(Test):


    @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/add.yaml'))
    def test_add(self,case):
        logger.info("请求的用例名称是: {}".format(case["case_name"]))
        re = self.sendRequests.send(method=case['method'],url=case['path'],data=case['data'])
        texts = get_response_text(re.text,'msg')
        assert_tet(case['result']['msg'],texts)
        mysqlutil.delete(delete_id_sql, (delete_userid()))







