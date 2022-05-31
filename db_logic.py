from mongo_connect import db
from pymongo import UpdateOne

def bulk_upserts_kr(list_of_pos, my_col):
    operations = []
    for doc in list_of_pos:
        print(doc)
        operations.append(
            UpdateOne({ "주문번호": doc["주문번호"] },{ "$set": doc })
        )
        # Send once every 10 in batch
        if (len(operations) == 10):
            my_col.bulk_write(operations,ordered=False)
            operations = []

    if ( len(operations) > 0 ):
        my_col.bulk_write(operations,ordered=False)

def bulk_upserts_en(list_of_pos, my_col):
    operations = []
    for doc in list_of_pos:
        print(doc)
        operations.append(
            UpdateOne({ "P/O No": doc["P/O No"] },{ "$set": doc })
        )
        # Send once every 10 in batch
        if (len(operations) == 10):
            my_col.bulk_write(operations,ordered=False)
            operations = []

    if ( len(operations) > 0 ):
        my_col.bulk_write(operations,ordered=False)