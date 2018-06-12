import webbrowser
from pydoc import pager
from sys import exit

def license_approval(currency):
    if currency != "g1":
        return
    language = input("In which language would you like to display Ğ1 license [en/fr]? ")
    if (language == "en"):
        if not webbrowser.open("https://duniter.org/en/get-g1/"):
            pager(open("licence-G1/license/license_g1-en.rst").read())
    else:
        if not webbrowser.open("https://duniter.org/fr/wiki/licence-g1/"):
            pager(open("licence-G1/license/license_g1-fr-FR.rst").read())

    if (input("Do you approve Ğ1 license [yes/no]? ") != "yes"):
        exit(1)
