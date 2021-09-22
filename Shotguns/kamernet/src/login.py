"""Login functions for Kamernet account."""
import os
from typing import Tuple
import time
from selenium import webdriver


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def get_env_values(string: str):
    return string.split("=")[1]

def get_credentials() -> Tuple[str,str]:
    with open(os.path.join(ROOT_PATH,'..',".env"), "r") as txt_file:
        credentials = list(map(get_env_values,map(str.strip,txt_file.readlines())))
        return credentials[0], credentials[1]

def login(driver: webdriver, username: str, password: str):
    driver.maximize_window()
    driver.get("https://kamernet.nl/en/for-rent/rooms-rotterdam")
    driver.find_element_by_css_selector(".header-login").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#UserEmail").send_keys(username)
    driver.find_element_by_css_selector("#LoginPassword").send_keys(password)
    driver.find_element_by_css_selector(".signin-login-popup").click()
    time.sleep(2)
    return driver
    