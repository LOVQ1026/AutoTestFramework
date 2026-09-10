from common.config import get_config



def test_config():

    config = get_config()


    print(config)


    assert config["browser"] == "chrome"