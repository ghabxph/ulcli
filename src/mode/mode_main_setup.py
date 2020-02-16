import lib
import requests
import json


class Mst:

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
        if Mst.__inst is None:
            Mst.__inst = Mst(lang)
        return Mst.__inst

    def setup(self, sp):
        """
        Initially sets up the class

        :param sp: Subparser instance from parser of argparse library
        :return:
        """

        self.__parser = sp.add_parser('main/setup', help=self.__lang.mst_prs_help)
        self.__parser.add_argument('-H', '--db-host', required=True, help=self.__lang.mst_prs_arg_dbhost_help)
        self.__parser.add_argument('-u', '--db-user', required=True, help=self.__lang.mst_prs_arg_dbuser_help)
        self.__parser.add_argument('-p', '--db-pass', required=True, help=self.__lang.mst_prs_arg_dbpass_help)
        self.__parser.add_argument('-P', '--db-name-prefix', required=True, help=self.__lang.mst_prs_arg_dbnapr_help)

        return self

    def run(self):
        """
        Runs the mode if triggered.

        :return:
        """
        url = lib.ulcli.args('url') + '/api/v1/environment'
        data = {
            "UL_DB_HOST": lib.ulcli.args('db_host'),
            "UL_DB_ROOT_USER": lib.ulcli.args('db_user'),
            "UL_DB_ROOT_PASS": lib.ulcli.args('db_pass'),
            "UL_DB_NAME_PREFIX": lib.ulcli.args('db_name_prefix'),
            "UL_TP_CHECK": 'false',
            "UL_TP_URL": '',
            "UL_TP_REQUEST_FORMAT": ''
        }
        res = requests.post(url, data=data)
        j_res = None

        try:
            # Tries to convert response to json
            j_res = res.json()
        except json.JSONDecodeError:
            # We set j_res to empty dict in case there's error in decoding the expected json response
            j_res = {}

        finally:
            # If request succeeds
            if j_res.get('type') == 'success' and j_res.get('msg') is not None:
                print(j_res.get('msg'))

            # If request didn't succeed
            elif j_res.get('type') == 'error' and j_res.get('msg') is not None:
                print('Error: %s' % j_res.get('msg'))

            # If we triggered server error, or url is not valid
            else:
                print('Url: %s' % url)
                print('Status Code: %s' % str(res.status_code))
                print(self.__lang.msg_err_insvr)
