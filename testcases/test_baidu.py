from common.logger import logger
from common.config import get_config



def test_baidu_title(driver):


    config = get_config()


    logger.info(
        "打开百度首页"
    )


    driver.get(
        config["base_url"]
    )


    logger.info(
        "获取页面标题"
    )


    title = driver.title


    logger.info(
        f"页面标题:{title}"
    )


    assert "百度" in title