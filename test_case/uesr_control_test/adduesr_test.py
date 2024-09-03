
from utils.logutil import logger


import pytest

from common.debug import get_response_text
from common.read_case_data import read_case_dataall
from test_case import Test
from utils.asst import assert_tet



# class Test_api_add(Test):
#
#
#     @pytest.mark.parametrize('case',read_case_dataall('/datas/uesrquery/add.yaml'))
#     def test_add(self,case):
#         # logger.debug("这是请求参数{}".format(case))
#         re = self.sendRequests.send(method=case['method'],url=case['path'],data=case['data'])
#         texts = get_response_text(re.text,'msg')
#         assert_tet(case['result']['msg'],texts)







