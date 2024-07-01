from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time,getpass
 
def fileUploader(url):
    dr = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    try:
        dr.get(url)
        file = dr.find_element(By.NAME, "SavedVarFileInput")
        file.send_keys(r'/Users/'+ getpass.getuser() +r'/Documents/Elder Scrolls Online/live/SavedVariables/TamrielTradeCentre.lua')
 
        ##submit = dr.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        ##submit.click()
 
        print("File Uploaded Successfully")
        time.sleep(5)
        dr.quit()
    except RuntimeError as e:
        print("An error occurred while fetching and uploading the file {}".format(e))
 
if __name__ == "__main__":
    url = "https://us.tamrieltradecentre.com/pc/Trade/WebClient"
    fileUploader(url)
