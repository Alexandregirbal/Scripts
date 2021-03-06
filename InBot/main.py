
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from config import *

def login(driver, username, password):
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))).click()
    usernameInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    usernameInput.clear()
    usernameInput.send_keys(username)
    passwordInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    passwordInput.clear()
    passwordInput.send_keys(password)
    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Plus tard")]'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Plus tard")]'))).click()

def searchByTag(driver, tag):
    tag = tag.lower()
    print("Search by tag: " + tag)
    #target the search input field
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Rechercher']")))
    searchbox.clear()

    #search for the hashtag cat
    keyword = "#"+tag
    searchbox.send_keys(keyword)
    searchbox.send_keys(Keys.ENTER)
    
    #FIXING THE DOUBLE ENTER
    # time.sleep(3)
    my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
    my_link.click()

def end(driver, secs):
    print("End.")
    time.sleep(secs)
    driver.close()

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/direct/inbox/")

    login(driver, username, password)
    searchByTag(driver,"Lille")

    end(driver,10)

main()

