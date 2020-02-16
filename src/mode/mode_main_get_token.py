from lib.util import response
import lib
import requests


class Mgt:

    __inst = None
    __parser = None
    __lang = None

    def __init__(self, lang):
        """
        Class constructor

        :param lang: Language instance.
        """
        # Sets language set by ulcli
        self.__lang = lang

    @staticmethod
    def inst(lang=None):
        """
        Returns singleton instance of this class

        :return:
        """
        if Mgt.__inst is None:
            Mgt.__inst = Mgt(lang)
        return Mgt.__inst

    def setup(self, sp):
        """
        Initially sets up the class

        :param sp: Subparser instance from parser of argparse library
        :return:
        """

        self.__parser = sp.add_parser('main/get-token', help=self.__lang.mgt_prs_help)
        self.__parser.add_argument('-u', '--username', required=True)
        self.__parser.add_argument('-p', '--password', required=True)

        return self

    def run(self):
        """
        Runs the mode if triggered.

        :return:
        """
        url = lib.ulcli.args('url') + '/api/v1/admin/token'
        l_res = lib.login(self.__lang, lib.ulcli.args('username'), lib.ulcli.args('password'))
        g_res = response(self.__lang, requests.post(url, headers={'Authorization': 'Bearer %s' % l_res.get('jws')}))
        print('Token: %s' % g_res.get('token'))
