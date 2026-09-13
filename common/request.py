import requests
from common.logger import logger


class RequestClient:

    def get(self, url, params=None, headers=None, verify=True):
        logger.info(f"GET请求: {url}")
        response = requests.get(
            url, params=params, headers=headers, verify=verify
        )
        logger.info(f"响应状态码: {response.status_code}")
        return response

    def post(self, url, json=None, headers=None, verify=True):
        logger.info(f"POST请求: {url}")
        response = requests.post(
            url, json=json, headers=headers, verify=verify
        )
        logger.info(f"响应状态码: {response.status_code}")
        return response