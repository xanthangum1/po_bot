from pymongo import MongoClient, DESCENDING
from config import mongo_pass
import certifi

client = MongoClient(
    f"mongodb+srv://lxs-adrian:{mongo_pass}@lxs-iot.htx5e.mongodb.net/?retryWrites=true&w=majority&tlsInsecure=true",
)


db = client["LXS-IOT"]

# mycol = db[""]

mppo = db["mp_po"]
devpo = db["dev_po"]

# first_po= {
#     "No.": "2",
#     "P/O No": "EM05D000119",
#     "Part No": "0ISWL-0594B",
#     "Need By Date": "2022-08-29",
#     "Scheduled Incoming Date": "",
#     "Delay Reason": "",
#     "Revised": "N",
#     "Canceled": "N",
#     "Revise Date": "2022-05-26",
#     "Order Date": "2022-05-26 12:01:41",
#     "Order Qty": "270000",
#     "Remain Qty": "270000",
#     "Shipping Qty": "0",
#     "Hub Onhand Qty": "0",
#     "Receipt Qty": "0",
#     "Receiving Qty": "0",
#     "UOM": "EA",
#     "Unit Price": "1.582",
#     "Tentative Price Flag": "N",
#     "Amount": "427140",
#     "Curr.": "USD",
#     "Item Desc": "Source Drive IC ** IC, SiW, SW42, 35, 4PF, UPILEX V1, OPS18-02, 1.1, 15.03*1.27*0.205, Special, 14.612*19.184*25.54, TSMC 40NM, NPR34",
#     "Maker Code": "KR021629",
#     "Maker Name": "LGDVN_주식회사 LX세미콘_KR021629",
#     "Inspection Report": "N",
#     "HS Code": "85423100",
#     "L/C No": "IDC30M0D000119Z",
#     "Location": "Haipong.H05",
#     "Location Desc": "Haipong Module Location(HW)",
#     "Final Location": "",
#     "Final Location Info.": "",
#     "PO Creator": "Van Phu, Do",
#     "Submission Title": "",
#     "Import Po Type": "A",
#     "mask/frame/stick ID": "",
#     "Import Po Type Desc": "General Import PO",
#     "Requestor Comments": "",
#     "PO Source": "MPI_PO",
# }

# dev_po_my = {
#     "번호": "1",
#     "조직": "M01",
#     "부품번호": "0ISWL-0831B",
#     "발주 유형명": "G",
#     "주문 번호": "6145901-17-1",
#     "Work Order": "",
#     "납기일자": "2022-09-21",
#     "납품예정일자": "",
#     "지연사유": "",
#     "납선": "1",
#     "사용자 품목유형": "PU",
#     "납품 유형": "G",
#     "Project Code": "",
#     "주문 수량": "10000",
#     "주문 잔량": "10000",
#     "출발 수량": "0",
#     "입고 수량": "0",
#     "취소 여부": "N",
#     "품명": "Power Integration IC ** IC, SW52036B, SILICONWORKS, NB21PM1, NBPC, 2.5V~5V, PVDD BOOST + NVDD BUCK BOOST + IO BUCK + CORE BUCK + VGH VGL2 SIBO + PVCOM + OPAMP + VGL1 LDO + AL",
#     "규격": "IC, SW52036B, SILICONWORKS, NB21PM1, NBPC, 2.5V~5V, PVDD BOOST + NVDD BUCK BOOST + IO BUCK + CORE BUCK + VGH VGL2 SIBO + PVCOM + OPAMP + VGL1 LDO + AL",
#     "단위": "EA",
#     "통화": "USD",
#     "단가": "0.9445",
#     "주문일자": "2022-05-31",
#     "Location": "Gumi.M01",
#     "위치 정보": "M1 Plant Location",
#     " 요청자": "김성진(856-0901)",
#     "요청팀": "중형 회로설계3팀",
#     "S/P 긴급 주문 여부": "N",
#     "PO Creator": "염아누.A Nu Yeom",
#     "Mask Serial No": "",
#     "Mask Id": "",
#     "Serial No": "",
#     "공급자 Serial No": "",
#     "긴급조치서 번호": "",
#     "긴급조치서 Status": "",
#     "출발처리 가능일": "2022-08-24",
#     "mask/frame/stick ID": "",
#     "출발처리 가능일자": "28",
#     "Requestor Comments": "",
#     "PO Source": "MPI_DEV",
# }

# db["mp_po"].create_index(
#     [("P/O No", DESCENDING)],
#     unique=True
# )

# db["dev_po"].create_index(
#     [('주문번호', DESCENDING)],
#     unique=True
# )

# db["mp_po"].insert_one(first_po)
# db["dev_po"].insert_one(dev_po_my)