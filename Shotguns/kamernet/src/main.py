import time
import os
from datetime import datetime
from selenium import webdriver
from login import get_credentials, login

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

MESSAGE = """
Hello {owner_name},
My name is Alexandre, and I just accepted a job in Rotterdam as a software engineer. Therefore I am looking for an apartment in the city and yours looks great!
I can do a viewing at any time this week, just let me know please.

Kind regards,
Alexandre Girbal
"""

rooms_already_seen_file_path = os.path.join(ROOT_PATH,"assets/rooms_already_seen.csv")

def send_message(driver: webdriver, id: str, message: str, use_owner_name: bool=True):
    if use_owner_name:
        owner_name = driver.find_elements_by_css_selector(".owner-name")[0].text
        message = message.replace("{owner_name}",owner_name)
    driver.execute_script("window.scrollTo(0, 1800)")
    try:
        driver.find_elements_by_css_selector("#Message")[1].send_keys(message)
        time.sleep(2)
        driver.find_element_by_css_selector("#BtnSendMessage").click()
        print(" --- Message sent ---")
    except Exception as e:
        print(e)
        print("  Could not send message to", id)
    print("  Room added to list of seen rooms.")
    with open(rooms_already_seen_file_path,'a') as csv_file:
        csv_file.write("\n")
        csv_file.write(id)

def main():
    rooms_already_seen = []
    with open(rooms_already_seen_file_path,"r") as file:
        for line in file.readlines():
            rooms_already_seen.append(line.strip())
    username, password = get_credentials()
    
    with webdriver.Chrome(executable_path=os.path.join(ROOT_PATH, '..', "chromedriver")) as driver:
        driver = login(driver, username, password)
        driver.get("https://kamernet.nl/en/account/alerts")
        driver.find_elements_by_css_selector(".mdi-action-search")[0].click()
        time.sleep(2)
        while True:
            print(datetime.now())
            driver.refresh()
            search_results = driver.find_elements_by_css_selector(".rowSearchResultRoom > div")
            windows = 0
            for room in search_results:
                room_text = room.text.split("\n")
                if room_text[0] in ['Top ad','New!']:
                    offset = 1
                else : offset = 0
                name = room_text[0+offset]
                city = room_text[1+offset].split(" - ")[0]
                price = room_text[2+offset].split(",")[0].replace(" ", "")
                id = f"{name}-{city}-{price}"
                # print(id)
                
                if (not id in rooms_already_seen) and city == "Rotterdam":
                    print("  New room detected ! Sending message to", id)
                    room.click()
                    driver.switch_to.window(driver.window_handles[windows+1])
                    send_message(driver, id, MESSAGE)
                    driver.switch_to.window(driver.window_handles[0])
                    windows += 1
            time.sleep(10)
        
if __name__ == "__main__":
    main()