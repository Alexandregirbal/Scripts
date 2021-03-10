import os
import time
import functools
from random import uniform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import *
import downloadImages as download
import utils as u
from decorators import Perf


def searchByTag(driver, tag, n):
    tag = "#"+tag.lower()
    print("Search by tag: " + tag)
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Rechercher']")))
    searchbox.clear()
    searchbox.send_keys(tag)
    searchbox.send_keys(Keys.ENTER)
    
    #Fix double ENTER  ---> _01UL2
    my_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + tag[1:] + "/')]")))
    my_link.click()

@Perf
def main(tag, maxImages, isClosing):
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    
    u.login(driver, username, password)
    searchByTag(driver, tag, 1)
    u.scroll(driver,1)
    #target all the link elements on the page
    print(f'Downloaded {download.downloadImages(driver, maxImages, tag)} images')
    if isClosing:
        u.end(driver,1)

main("amsterdam", 1, True)

#TODO delete duplicates, comment every picture with a word in a selection like 'nice, wow, where did you take that one...'
#TODO follow unfollow sendmessage