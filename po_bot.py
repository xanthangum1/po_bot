from po_crawl import auto_po
from config import yt_id, yt_pw, vh_id, vh_pw, lc_id, lc_pw
from retriever import retriever_art


### Make sure location is capitalized. I know its lazy
overseas_client_list = [
    {"id": yt_id, "pw": yt_pw, "identity": "yeontai", "location": "Overseas"}, 
    {"id": vh_id, "pw": vh_pw, "identity": "vaihong", "location": "Overseas"},
    {"id": lc_id, "pw": lc_pw, "identity": "dev", "location": "Local"}
]


def michael_schumacher():
    ##best driver...code there is
    retriever_art()
    for client in overseas_client_list:
        auto_po(client["id"], client["pw"], client["identity"], client["location"])
    # auto_po(overseas_client_dict["lgd_yeontai"]["id"], overseas_client_dict["lgd_yeontai"]["pw"], overseas_client_dict["lgd_yeontai"]["identity"])
    # auto_po(overseas_client_dict["lgd_vh"]["id"], overseas_client_dict["lgd_vh"]["pw"], overseas_client_dict["lgd_vh"]["identity"])

michael_schumacher()