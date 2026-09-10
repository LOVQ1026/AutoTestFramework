import logging
import os



def get_logger():


    logger = logging.getLogger(
        "AutoTest"
    )


    logger.setLevel(
        logging.INFO
    )


    # 防止重复添加handler
    if logger.handlers:

        return logger



    if not os.path.exists("logs"):

        os.mkdir(
            "logs"
        )


    file_handler = logging.FileHandler(

        "logs/test.log",

        encoding="utf-8"

    )


    console_handler = logging.StreamHandler()



    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )


    file_handler.setFormatter(
        formatter
    )


    console_handler.setFormatter(
        formatter
    )



    logger.addHandler(
        file_handler
    )


    logger.addHandler(
        console_handler
    )


    return logger



logger = get_logger()