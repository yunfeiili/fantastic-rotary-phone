




import pytest
from deepdiff import DeepDiff

from common.write_case_result_data import wr

from common.debug import get_response_text
from common.read_case_data import read_case_dataall
from test_case import  Test
from utils.asst import assert_tet, assert_diff

paths = r'\datas\logon.yaml'

class Test_api_case3(Test):


    @pytest.mark.parametrize('case',read_case_dataall(paths))
    def test_login(self,case):
        re = self.sendRequests.send(method=case['method'],url=case['path'],data=case['data'])
        texts1 = re.json()
        wr.writresult(paths, texts1,is_writ=False)
        assert_diff(case["result"],texts1,"root['data']['token']")
        assert_tet(case['result']["meta"]['msg'],get_response_text(re.text,'msg'))







