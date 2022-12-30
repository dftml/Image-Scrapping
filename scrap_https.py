from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

def image(query : str, photos : int):
    
    def scroll_to_end():
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        
    url = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url)
    browser.refresh()
    link = set()
    starting = 0
    while True:
        
        session = browser.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        
        for image in session[starting:]:
            image.click()
            time.sleep(1)
            if 'http' in image.get_attribute('src'):
                link.add(image.get_attribute("src"))
            
            
            
            if len(link) == photos:
                browser.close()
                return link
        
        starting = len(session)
        scroll_to_end()

# to convert link & store in local drive
def download_local(image_links : set):
    lnk_image = list(image_links)
    for j in range(len(lnk_image)):
        
        link = requests.get(lnk_image[j])
        with open(f"Img_{j+1}.png", "wb") as I:
            I.write(link.content)
    
if __name__ == "__main__":
    query = input("Please enter anything: ")
    photos = int(input("Please enter the no. of photos: "))
    download_local(image(query,photos))
