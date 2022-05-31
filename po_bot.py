from config import yt_id, yt_pw, vh_id, vh_pw, lc_id, lc_pw
from po_crawl import auto_po
from retriever import retriever_art
import sentry_sdk

sentry_sdk.init(
    "https://5271eee5bbe24a4483ec62717d7cdf21@o1268698.ingest.sentry.io/6456488",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


### Make sure location is capitalized. I know its lazy
overseas_client_list = [
    {"id": yt_id, "pw": yt_pw, "identity": "yt", "location": "Overseas"},
    {"id": vh_id, "pw": vh_pw, "identity": "vn", "location": "Overseas"},
    {"id": lc_id, "pw": lc_pw, "identity": "dev", "location": "Local"},
]


def michael_schumacher():
    ##best driver...code there is
    retriever_art()
    for client in overseas_client_list:
        auto_po(client["id"], client["pw"], client["identity"], client["location"])


michael_schumacher()
