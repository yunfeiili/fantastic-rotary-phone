
from utils.logutil import logger


import pytest

from common.debug import get_response_text
from common.read_case_data import read_case_dataall
from test_case import Test
from utils.asst import assert_tet



class Test_api_query(Test):


    @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/query.yaml.yaml'))
    def test_query(self,case):
        re = self.sendRequests.send(method=case['method'],url=case['path'],params=case['data'])
        texts = get_response_text(re.text,'msg')
        assert_tet(case['result']['msg'],texts)


    @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/queryid.yaml'))
    def test_query_id(self,case):
        re = self.sendRequests.send(method=case['method'],url=case['path'],params=case['data'])
        texts = get_response_text(re.text,'msg')
        assert_tet(case['result']['msg'],texts)





