import lib
import requests


class Man:

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
        if Man.__inst is None:
            Man.__inst = Man(lang)
        return Man.__inst

    def setup(self, sp):
        """
        Initially sets up the class

        :param sp: Subparser instance from parser of argparse library
        :return:
        """

        self.__parser = sp.add_parser('manage', help=self.__lang.man_prs_help)
        self.__parser.add_argument('-u', '--username', required=True)
        self.__parser.add_argument('-p', '--password', required=True)

        return self

    def run(self):
        """
        Runs the mode if triggered.

        :return:
        """
        pass
