from pymongo import MongoClient
from config import mongo_pass

client = MongoClient(
    f"mongodb+srv://adriankim18:<{mongo_pass}>@lxs-iot.htx5e.mongodb.net/?retryWrites=true&w=majority"
)

db = client["LXS-IOT"]

mycol = db["po"]

{
    "EM05D000119": {
        "No.": "2",
        "P/O No": "EM05D000119",
        "Part No": "0ISWL-0594B",
        "Need By Date": "2022-08-29",
        "Scheduled Incoming Date": "",
        "Delay Reason": "",
        "Revised": "N",
        "Canceled": "N",
        "Revise Date": "2022-05-26",
        "Order Date": "2022-05-26 12:01:41",
        "Order Qty": "270000",
        "Remain Qty": "270000",
        "Shipping Qty": "0",
        "Hub Onhand Qty": "0",
        "Receipt Qty": "0",
        "Receiving Qty": "0",
        "UOM": "EA",
        "Unit Price": "1.582",
        "Tentative Price Flag": "N",
        "Amount": "427140",
        "Curr.": "USD",
        "Item Desc": "Source Drive IC ** IC, SiW, SW42, 35, 4PF, UPILEX V1, OPS18-02, 1.1, 15.03*1.27*0.205, Special, 14.612*19.184*25.54, TSMC 40NM, NPR34",
        "Maker Code": "KR021629",
        "Maker Name": "LGDVN_주식회사 LX세미콘_KR021629",
        "Inspection Report": "N",
        "HS Code": "85423100",
        "L/C No": "IDC30M0D000119Z",
        "Location": "Haipong.H05",
        "Location Desc": "Haipong Module Location(HW)",
        "Final Location": "",
        "Final Location Info.": "",
        "PO Creator": "Van Phu, Do",
        "Submission Title": "",
        "Import Po Type": "A",
        "mask/frame/stick ID": "",
        "Import Po Type Desc": "General Import PO",
        "Requestor Comments": "",
        "PO Source": "MPI_PO",
    }
}
