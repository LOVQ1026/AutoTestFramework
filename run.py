import pytest
import os
import time



if __name__ == "__main__":


    report_dir = "reports"


    if not os.path.exists(report_dir):

        os.mkdir(report_dir)



    timestamp = time.strftime(
        "%Y%m%d_%H%M%S"
    )


    pytest.main(

        [

            "-v",

            "-s",

            "testcases",

            f"--html={report_dir}/report_{timestamp}.html",

            "--self-contained-html",

            f"--alluredir={report_dir}/allure-results"

        ]

    )