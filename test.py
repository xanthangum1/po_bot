from example import example_list
from pymongo.errors import BulkWriteError
from mongo_connect import db
from misc_tools import dict_key_space_destroyer


def excel_to_json_reader_and_saver():
    # os.chdir(download_file)
    # files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    # newest_file = files[-1]
    data = example_list
    date = dict_key_space_destroyer(example_list)
    # with open(newest_file) as csvFile:
    #     csvReader = csv.DictReader(csvFile)
    #     for rows in csvReader:
    #         # po_id = rows["P/O No"]
    #         data.append(dict(rows))
    # print(data)

    db["dev_po"].insert_many(data)

    print("saved to mongo")

excel_to_json_reader_and_saver()
