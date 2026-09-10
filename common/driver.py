from selenium import webdriver
from common.config import get_config



def create_driver():

    config = get_config()


    if config["browser"] == "chrome":

        driver = webdriver.Chrome()


    driver.maximize_window()

    return driver