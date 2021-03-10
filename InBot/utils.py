import os
import time
from random import uniform

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def scroll(driver,numberOfPages):
    for lap in range(1, numberOfPages+1):
        print(f"Scrolling down ({lap})")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        randomSleep(5,6)

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


def end(driver, secs):
    print(f"Closing window in {secs} secs...")
    time.sleep(secs)
    driver.close()
    print('Window closed')
