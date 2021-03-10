import concurrent.futures
import os
from datetime import datetime

import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import utils as u
from config import *


def getImageByAnchor(anchor):
    options = Options()
    options.add_argument('--headless')
    tmpDriver = webdriver.Firefox(options=options)
    # tmpDriver = webdriver.Firefox()
    tmpDriver.get(anchor)
    WebDriverWait(tmpDriver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))).click()
    el = tmpDriver.find_elements_by_tag_name('img')
    image = [i.get_attribute('src') for i in el]
    print(image[1])
    u.randomSleep(3,5)
    tmpDriver.close()
    return image[1]

def dowloadOneImage(link, outputPath):
    wget.download(link, outputPath)
    print(f" ---> {outputPath}")

def downloadImages(driver,max,filesNamesTemplate):
    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors[:max] if str(a).startswith("https://www.instagram.com/p/")]
    print('Found ' + str(len(anchors)) + ' links to images')

    directory = os.path.dirname(os.path.abspath(__file__))
    downloadPath = os.path.join(directory, "downloaded")
    count = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # f1 = executor.submit(getImageLink,a)
        # print(f1.result())

        # results = [executor.submit(getImageLink, a) for a in anchors[:max-1]]

        # for f in concurrent.futures.as_completed(results):
        #     images.append(f.result)

        results = executor.map(getImageByAnchor, anchors)
        timestamp = str(datetime.now().timestamp()).replace('.','')
        for image in results:

            outputPath = os.path.join(downloadPath, filesNamesTemplate +'-' + str(count) + '_' + timestamp + '.jpg')
            dowloadOneImage(image,outputPath)
            count += 1
        return count
