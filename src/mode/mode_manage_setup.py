from lib.util import response
import lib
import requests


class Mtp:

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
        if Mtp.__inst is None:
            Mtp.__inst = Mtp(lang)
        return Mtp.__inst

    def setup(self, sp):
        """
        Initially sets up the class

        :param sp: Subparser instance from parser of argparse library
        :return:
        """

        self.__parser = sp.add_parser('manage/setup', help=self.__lang.mtp_prs_help)
        self.__parser.add_argument('-u', '--username', required=True)
        self.__parser.add_argument('-p', '--password', required=True)
        self.__parser.add_argument('-t', '--admin-token', required=True)
        self.__parser.add_argument('-m', '--main-url', required=True)

        return self

    def run(self):
        """
        Runs the mode if triggered.

        :return:
        """
        url = lib.ulcli.args('url') + '/api/v1/admin/manage'
        l_res = lib.login(self.__lang, lib.ulcli.args('username'), lib.ulcli.args('password'))
        res = response(self.__lang, requests.post(url, data={
            "url": lib.ulcli.args('main_url'),
            "key": lib.ulcli.args('admin_token')
        }, headers={'Authorization': 'Bearer %s' % l_res.get('jws')}))
        print(res)
