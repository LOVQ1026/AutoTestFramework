from common.logger import logger



def test_logger():


    logger.info(
        "开始执行测试"
    )


    logger.warning(
        "这是测试警告"
    )


    assert True