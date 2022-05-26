import xlrd
from collections import OrderedDict
import json
import csv
import pandas as pd


def excel_to_json_reader():
    csv_file_path = r"O:\해외영업팀\3.제품관리\PO\vn_PO_20220526_0139.csv"
    data = {}
    with open(csv_file_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            po_id = rows["P/O No"]
            data[po_id] = rows

    print(data)

excel_to_json_reader()