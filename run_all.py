import time,os

import pytest



if __name__ == '__main__':
    pytest.main()
    # pytest.main(['-k', 'test_query_sql_id'])  # 运行test_01这一个测试用例
    # pytest.main(['-q', 'Test_api_query'])
    time.sleep(3)
    os.system('allure generate ./temps -o ./reports --clean')
