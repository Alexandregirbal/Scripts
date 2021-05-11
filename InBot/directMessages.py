import utils

def selectConversation(driver, numberOfConversation):
    try:
        print(f'Trying to go into conversation n°{numberOfConversation}')
        #unseen message .qyrsm
        # messagesList = dirver.find_element_by_class_name("Igw0E IwRSH eGOV_ _4EzTm i0EQd")
        messagesList = driver.find_element_by_css_selector("div.N9abW")
        divs = messagesList.find_elements_by_tag_name("a")
        for div in divs :
            print(div)
        
        # anchors = messagesList.find_elements_by_tag_name('a')
        # hrefs = [a.get_attribute('href') for a in anchors]
        # print(hrefs)
    except NameError:
        print (NameError)
        utils.end(driver, 3)