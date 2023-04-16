from utils.logutil import logger


def assert_tet(reality, expect):
    try:

        assert reality == expect
        logger.info('断言成功: {} == {}'.format(reality, expect))
        return True
    except Exception as e:
        logger.info(e)
        logger.error('断言失败: {} != {}'.format(reality, expect))
        return False