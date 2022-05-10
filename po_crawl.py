from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from config import yt_id, yt_pw, vh_id, vh_pw
import os

def auto_po():
    print("starting PO retriever")
    os.environ['WDM_SSL_VERIFY']='0'

    ###logging into LG SCS
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://scs.lgdisplay.com/system/login/retrieveLogin.dev')
    print("entered LG scs")
    sleep(3)

    username_input = driver.find_element_by_id('userId')
    username_input.send_keys(yt_id)
    print("entered username")

    hover_1 = driver.find_element_by_xpath("(//div[@class='input-group'])[2]")
    password_input.send_keys(yt_pw)
    print("password entered")
  
    login_button = driver.find_element_by_xpath("(//button[normalize-space()='Login'])[1]")
    login_button.click()
    print("logging in")
