import os
import sys
from tabulate import tabulate
from collections import OrderedDict

from network_tools import request
from tools import get_pubkeys_from_id
from constants import *


def received_sent_certifications(ep, id):
    """
    check id exist
    many identities could exist
    retrieve the one searched
    get id of received and sent certifications
    display on a chart the result with the numbers
    """
    if get_pubkeys_from_id(ep, id) == NO_MATCHING_ID:
        print(NO_MATCHING_ID)
        sys.exit(1)
    certs = request(ep, "wot/lookup/" + id)["results"]
    for cert in certs:
        if cert["uids"][0]["uid"].lower() == id.lower():
            certs = cert
    certifications = OrderedDict()
    certifications["received"] = list()
    certifications["sent"] = list()
    if certs["uids"]:
        for received, cert in enumerate(certs["uids"][0]["others"]):
            certifications["received"].append(cert["uids"][0])
        received += 1;
    else:
        received = 0
    if certs["signed"]:
        for sent, cert in enumerate(certs["signed"]):
            certifications["sent"].append(cert["uid"])
        sent += 1;
    else:
        sent = 0
    os.system("clear")
    print("{0} received {1} and sent {2} certifications:\n{3}"
    .format(id, received, sent, tabulate(certifications, headers="keys", tablefmt="orgtbl", stralign="center")))
