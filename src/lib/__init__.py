from lib.ulcli import ULCLI
from lib.login import Login

# ulcli instance
ulcli = ULCLI.inst()


def login(lang, username, password, debug=False):
    """
    Helper function that logs you in to ul server

    :param lang:
    :param username:
    :param password:
    :param debug:
    :return:
    """
    return Login.inst(lang).login(username, password, debug)
