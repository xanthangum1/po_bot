import os
from config import download_file, script_file

def dateme_sama(today):
    today_str = str(today)
    tod_num = today_str[0] + today_str[1] + today_str[2] + today_str[3] + today_str[5] + today_str[6] + today_str[8] + today_str[9]
    return tod_num

def latest_download_file(client_name):
    os.chdir(download_file)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    new_name = client_name + "_" + newest
    os.rename(newest, new_name)
    os.chdir(script_file)
    return None

