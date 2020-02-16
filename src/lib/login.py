from lib.util import response
import requests
import lib


class Login:

    __lang = None
    __inst = None

    def __init__(self, lang):
        self.__lang = lang

    @staticmethod
    def inst(lang):
        if Login.__inst is None:
            Login.__inst = Login(lang)
        return Login.__inst

    def login(self, username, password, debug=False):
        """
        Perform login to ul server

        :param username:
        :param password:
        :param debug:
        :return: Dict containing response from the server.
        """
        url = lib.ulcli.args('url') + '/api/v1/login'
        return response(self.__lang, requests.post(url, data={
            "username": username,
            "password": password
        }), debug)
