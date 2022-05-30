from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import yt_id, yt_pw, vh_id, vh_pw
from misc_tools import dateme_sama, latest_download_file, day_to_string
import os
import datetime
from config import download_file
import time


def auto_po(username, password, identity, location):
    ### setting up webdriver
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_file,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    os.environ["WDM_SSL_VERIFY"] = "0"
    print("starting PO retriever")
    ###logging into LG SCS
    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    driver.get("https://scs.lgdisplay.com/system/login/retrieveLogin.dev")
    print("entered LG scs")
    sleep(2)

    username_input = driver.find_element_by_xpath("//input[@id='userId']")
    username_input.send_keys(username)
    print("entered username")

    password_input = driver.find_element_by_xpath("//input[@placeholder='Password']")
    password_input.send_keys(password)
    print("password entered")

    login_button = driver.find_element_by_xpath(
        "(//button[normalize-space()='Login'])[1]"
    )
    login_button.click()
    print("logging in")

    sleep(2)

    ### MFers input names are different for Overseas and Local... LOL. Hence the idiotic elif statement
    if location == "Overseas":
        overseas_path = driver.find_element_by_xpath(
            "//a[@href='#'][normalize-space()='Overseas']"
        )
        overseas_path.click()

        sleep(2)

        ###filtering POS for dates
        today = datetime.datetime.today()
        lower = dateme_sama(today)
        print(lower)
        po_date_lower = driver.find_element_by_xpath("//input[@id='idDateFrom']")
        # idiotic fix for date being entered twice...
        for _ in range(8):
            po_date_lower.send_keys(Keys.BACKSPACE)
        po_date_lower.send_keys(lower)

        po_date_upper = driver.find_element_by_xpath("//input[@id='idDateTo']")
        sleep(1)
        # idiotic fix for date being entered twice...
        po_date_upper.send_keys(day_to_string(today))
        for _ in range(8):
            po_date_upper.send_keys(Keys.BACKSPACE)
        sleep(1)
        ### search
        login_button = driver.find_element_by_css_selector("button[name='btnInquiry']")
        login_button.click()
        sleep(5)

        ### download excel
        login_button = driver.find_element_by_xpath("//button[@id='btnExcel']")
        login_button.click()
        sleep(5)

        latest_download_file(identity)

    elif location == "Local":
        local_path = driver.find_element_by_xpath(f"//a[contains(text(),'{location}')]")
        local_path.click()

        sleep(2)

        ###filtering POS for dates
        today = datetime.datetime.today()
        lower = dateme_sama(today)
        print(lower)
        po_date_lower = driver.find_element_by_xpath(
            "//div[@id='rangeDate']//input[@id='dateFrom']"
        )
        # idiotic fix for date being entered twice...
        for _ in range(8):
            po_date_lower.send_keys(Keys.BACKSPACE)
        po_date_lower.send_keys(lower)

        po_date_upper = driver.find_element_by_xpath(
            "//div[@id='rangeDate']//input[@id='dateTo']"
        )
        sleep(1)
        # idiotic fix for date being entered twice...
        po_date_upper.send_keys(day_to_string(today))
        for _ in range(8):
            po_date_upper.send_keys(Keys.BACKSPACE)
        sleep(1)
        ### search
        login_button = driver.find_element_by_css_selector("button[name='btnInquiry']")
        login_button.click()
        sleep(5)

        ### download excel
        login_button = driver.find_element_by_xpath("//button[@id='btnExcel']")
        login_button.click()
        sleep(5)

        latest_download_file(identity)
