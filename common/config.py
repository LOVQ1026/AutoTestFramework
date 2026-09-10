import yaml
import os


def get_config():

    # 当前文件目录
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )


    # 项目根目录
    project_root = os.path.dirname(
        current_dir
    )

    config_path = os.path.join(
        project_root,
        "config",
        "config.yaml"
    )


    with open(
        config_path,
        encoding="utf-8"
    ) as file:

        config = yaml.safe_load(file)


    return config