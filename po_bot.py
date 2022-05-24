from po_crawl import auto_po
from config import yt_id, yt_pw, vh_id, vh_pw, lc_id, lc_pw
from retriever import retriever_art


### Make sure location is capitalized. I know its lazy
overseas_client_list = [
    {"id": yt_id, "pw": yt_pw, "identity": "yt", "location": "Overseas"}, 
    {"id": vh_id, "pw": vh_pw, "identity": "vn", "location": "Overseas"},
    {"id": lc_id, "pw": lc_pw, "identity": "dev", "location": "Local"}
]


def michael_schumacher():
    ##best driver...code there is
    retriever_art()
    for client in overseas_client_list:
        auto_po(client["id"], client["pw"], client["identity"], client["location"])

michael_schumacher()