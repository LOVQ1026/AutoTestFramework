import yaml
import os



def read_yaml(filename):


    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )


    file_path = os.path.join(

        project_root,

        "data",

        filename

    )


    with open(
        file_path,
        encoding="utf-8"
    ) as file:


        return yaml.safe_load(file)