import requests,pytest
from common.debug import get_response_text
from config.read_environment import rade_environmert




@pytest.fixture(scope='session', autouse=True)
def session_controller():
    url = 'http://127.0.0.1:8888/api/private/v1/login'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': 'admin',
            'password': 123456}
    res = requests.request('post',url=url,headers=headers,data=data)
    token = get_response_text(res.text,'token')
    rade_environmert(token)

