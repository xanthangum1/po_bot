import xlrd
from collections import OrderedDict
from config import download_file, script_file
import json
import csv
import pandas as pd
import pymongo
import os
from mongo_connect import db
from pymongo.errors import BulkWriteError
from db_logic import bulk_upserts_en, bulk_upserts_kr
from misc_tools import dict_key_space_destroyer


def excel_to_json_reader_and_saver(identity):
    os.chdir(download_file)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest_file = files[-1]
    data = []
    with open(newest_file) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            # po_id = rows["P/O No"]
            data.append(dict(rows))
    if not data:
        print("No POs here")
        pass
    else:
        try:
            if identity == "local":
                data = dict_key_space_destroyer(data)
                bulk_upserts_kr(data, db)
            elif identity == "yt" or identity == "vn":    
                bulk_upserts_en(data, db)
        except BulkWriteError:
            pass

        print("saved to mongo")

    os.chdir(script_file)
