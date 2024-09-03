from utils.logutil import logger

from deepdiff import DeepDiff

def assert_tet(reality, expect):
    try:

        assert reality == expect
        logger.debug('断言成功: {} == {}'.format(reality, expect))
    except Exception as e:
        logger.info(e)
        logger.error('断言失败: {} != {}'.format(reality, expect))
        raise e


def assert_diff(reality1, expect1,zidpath = " "):
    '''
    全字段进行对比
    :param reality: 实际值
    :param expect: 预期值
    :return:
    '''
    try:
        values = DeepDiff(reality1, expect1,exclude_paths=zidpath,ignore_string_type_changes=True)
        if values == {}:
            logger.debug("接口数据断言成功。忽略字段校验路径是{}\n1.实际数据是: {}\n2.预期数据是: {}".format(zidpath,reality1,expect1))
            assert values == {}
        else:
            logger.error("数据对比失败，以下是数据不一致处:{}".format(DeepDiff(reality1,expect1)) )
            raise
    except Exception as s:
        raise s
