from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os

def auto_po():
    print("starting PO retriever")
    os.environ['WDM_SSL_VERIFY']='0'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://saas.lxsemicon.com:8000/saasplatform/ikep/sso/tenant/gportal.lxsemicon.com/sso.jsp?tntId=lxsemicon&appId=1')
  