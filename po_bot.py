from po_crawl import auto_po
from config import yt_id, yt_pw, vh_id, vh_pw

overseas_client_dict = {
    "lgd_yeontai": {"id": yt_id, "pw": yt_pw, "identity": "yeontai"}, 
    "lgd_vh": {"id": vh_id, "pw": vh_pw, "identity": "vaihong"}
}


def michael_schumacher():
    ##best driver...code there is
    auto_po(overseas_client_dict["lgd_yeontai"]["id"], overseas_client_dict["lgd_yeontai"]["pw"], overseas_client_dict["lgd_yeontai"]["identity"])
    auto_po(overseas_client_dict["lgd_vh"]["id"], overseas_client_dict["lgd_vh"]["pw"], overseas_client_dict["lgd_vh"]["identity"])

michael_schumacher()