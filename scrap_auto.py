from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
import requests
from pathlib import Path

def image(query : str, photos : int):
    
    def scroll_to_end():
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

    url1 = "http://google.com"
    url2 = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
    url3 = "https://write-box.appspot.com/"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url1)
    browser.refresh()


    browser.execute_script("window.open('about:blank', 'secondtab');")
    browser.switch_to.window("secondtab")
    browser.get(url2)
    time.sleep(1)
    browser.execute_script("window.open('about:blank', 'thirdtab');")
    browser.switch_to.window("thirdtab")
    browser.get(url3)
    time.sleep(1)

    browser.switch_to.window("secondtab")
    browser.refresh()
    time.sleep(3)

    link = 0
    starting = 0
    while True:

        session = browser.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")

        for index in range(starting,len(session)):
            session[index].click()
            time.sleep(2)
            pyautogui.rightClick(x=1560,y=390, duration=1)
            time.sleep(1)
            pyautogui.click(x=1630,y=664, duration=1)
            time.sleep(1)
            browser.switch_to.window("thirdtab")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(['enter'])
            time.sleep(1)
            browser.switch_to.window("secondtab")

            link = link + 1

            if link == photos:
                browser.close()
                pyautogui.click(x=1820,y=122,duration=1)
                time.sleep(1)
                pyautogui.click(x=1742, y=196)
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'shift', 'w')
                return

        starting = len(session)
        scroll_to_end()

# to convert link & store in local drive
def download_local():
    link_path = str(Path.home()/ 'Downloads'/'download')
    with open(link_path, "r") as f:
        data = f.read()

    lnk_image = data.split("\n")[:-1]
    for j in range(len(lnk_image)):
        try:
            link = requests.get(lnk_image[j])
        except:
            pass
        else:
            with open(f"Img_{j+1}.png", "wb") as I:
                I.write(link.content)
        
        
        
if __name__ == "__main__":
    query = input("Please enter anything: ")
    photos = int(input("Please enter the no. of photos: "))
    lnk_image = image(query,photos)
    download_local()
