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
import utils
from decorators import Perf
import directMessages


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
def downloadImagesByTag(tag, maxImages, isClosing):
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    
    utils.login(driver, username, password)
    searchByTag(driver, tag, 1)
    utils.scroll(driver,1)
    #target all the link elements on the page
    numberOfImagesDownloaded = download.downloadImages(driver, maxImages, tag)
    print(f'Downloaded {numberOfImagesDownloaded} images')
    if isClosing:
        utils.end(driver,1)

# downloadImagesByTag("rotterdam", 10, True)

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/direct/inbox/")
    utils.login(driver, username, password)
    directMessages.selectConversation(driver, 1)

    # utils.end(driver,5)

main()


#TODO send private message
#TODO follow / unfollow
#TODO like picture
#TODO comment picture