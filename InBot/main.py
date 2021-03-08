
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time
from config import *
from random import uniform
import os
import wget
import concurrent.futures


def randomSleep(min, max):
    sleepTime = round(uniform(min,max),3)
    print(f'Sleep for {sleepTime} secs')
    time.sleep(sleepTime)

def goBack(driver,numberOfTimes):
    for lap in range(1,numberOfTimes+1):
        print(f'Going backwards ({lap})')
        driver.execute_script("window.history.go(-1)")
        randomSleep(0.5,1.5)

def login(driver, username, password):
    print('Log in ...')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))).click()
    usernameInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    usernameInput.clear()
    usernameInput.send_keys(username)
    passwordInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    passwordInput.clear()
    passwordInput.send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Plus tard")]'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Plus tard")]'))).click()

def searchByTag(driver, tag):
    tag = "#"+tag.lower()
    print("Search by tag: " + tag)
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Rechercher']")))
    searchbox.clear()
    searchbox.send_keys(tag)
    searchbox.send_keys(Keys.ENTER)
    
    #Fix double ENTER
    my_link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + tag[1:] + "/')]")))
    my_link.click()

def scroll(driver,numberOfPages):
    for lap in range(0, numberOfPages):
        print(f"Scrolling down ({lap})")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        randomSleep(5,6)

def getImageByAnchor(anchor):
    options = Options()
    options.add_argument('--headless')
    tmpDriver = webdriver.Firefox(options=options)
    tmpDriver.get(anchor)
    WebDriverWait(tmpDriver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))).click()
    el = tmpDriver.find_elements_by_tag_name('img')
    image = [i.get_attribute('src') for i in el]
    print(image[1])
    randomSleep(3,5)
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
        for image in results:
            outputPath = os.path.join(downloadPath, filesNamesTemplate +'-' + str(count) + '.jpg')
            dowloadOneImage(image,outputPath)
            count += 1
        return count
        


def end(driver, secs):
    print(f"Closing window in {secs} secs...")
    time.sleep(secs)
    driver.close()
    print('Window closed')

def main(tag, maxImages, isClosing):
    start = time.perf_counter()
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    
    login(driver, username, password)
    searchByTag(driver, tag)
    scroll(driver,1)
    #target all the link elements on the page
    numberOfImages = downloadImages(driver, maxImages, tag)

    goBack(driver,1)

    finish = time.perf_counter()
    print(f"\033[92m \nFinish downloading {numberOfImages} pictures of #{tag} in {round(finish-start,3)} seconds.\n\033[0m")
    if isClosing:
        end(driver,10)

main("rotterdam", 20, True)

