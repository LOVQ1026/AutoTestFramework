import os
import time



def save_screenshot(driver):


    if not os.path.exists(
        "screenshots"
    ):

        os.mkdir(
            "screenshots"
        )


    filename = (

        "screenshots/"
        +
        time.strftime(
            "%Y%m%d_%H%M%S"
        )
        +
        ".png"

    )


    driver.save_screenshot(
        filename
    )

    return filename