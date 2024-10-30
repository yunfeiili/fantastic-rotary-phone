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


def assert_diff(reality1, expect1,zidpath = [ ]):
    """

    :param reality1: 实际值
    :param expect1: 实际值
    :param zidpath: 对比时排除指定的路径的字段不进行对比。忽略该路径的的对比
    :return:
    """

    try:
        values = DeepDiff(reality1, expect1,exclude_paths=zidpath,ignore_string_type_changes=True)
        if values == {}:
            logger.debug(f"1.实际数据是: {reality1}")
            logger.debug(f"2.预期数据是: {expect1}")
            logger.debug("忽略字段校验路径是{}".format(zidpath))
            assert values == {}
        else:
            logger.error("数据对比失败，以下是数据不一致处:{}".format(DeepDiff(reality1,expect1)) )
            return
    except Exception as s:
        raise s


def assert_diff_Ignore_case(reality1, expect1):
    """
    返回结果忽略大小写判断吧
    :param reality1: 实际值
    :param expect1: 预期值
    :return:
    """

    try:
        values = DeepDiff(reality1, expect1,ignore_string_case=True)
        if values == {}:
            logger.debug(f"1.实际数据是: {reality1}")
            logger.debug(f"2.预期数据是: {expect1}")
            assert values == {}
        else:
            logger.error("数据对比失败，以下是数据不一致处:{}".format(DeepDiff(reality1,expect1)) )
            return
    except Exception as s:
        raise s



