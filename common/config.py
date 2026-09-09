import yaml



def get_config():

    with open(
        "config/config.yaml",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)