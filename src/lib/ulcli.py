import lang
import argparse
import mode


class ULCLI:

    __lang = None
    __args = None
    __inst = None
    __parser = None
    __description = '''
                       GhabXPH (c) 2020
                    Universal Login CLI Tool
         -----------------------------------------------
         $$\   $$\ $$\       $$$$$$\  $$\       $$$$$$\ 
         $$ |  $$ |$$ |     $$  __$$\ $$ |      \_$$  _|
         $$ |  $$ |$$ |     $$ /  \__|$$ |        $$ |  
         $$ |  $$ |$$ |     $$ |      $$ |        $$ |  
         $$ |  $$ |$$ |     $$ |      $$ |        $$ |  
         $$ |  $$ |$$ |     $$ |  $$\ $$ |        $$ |  
         \$$$$$$  |$$$$$$$$\\$$$$$$  |$$$$$$$$\ $$$$$$\ 
         \______/ \________|\______/ \________|\______|
         -----------------------------------------------

         Github: https://github.com/ghabxph/ulcli.git
         Docker: https://hub.docker.com/u/ghabxph/ulcli
 
%s
'''

    def __init__(self, _lang):
        """
        Class constructor

        :param _lang: Language to use

        Note: Currently, we only support english this time. I will post a guide how to
              modify language of this program
        """
        # Sets the default language
        self.__lang = lang.init(_lang)

        # Initializes description
        self.__description = self.__description % self.__lang.ulcli_description

    @staticmethod
    def inst(_lang='en'):
        """
        Returns ULCLI singleton instance

        Basic usage:
        Simply call ULCLI.inst().{method_name}() that you wish to call
        :return:
        """
        if ULCLI.__inst is None:
            ULCLI.__inst = ULCLI(_lang)
        return ULCLI.__inst

    def args(self, key):
        """
        Returns the value of args put by the user

        :param key:
        :return:
        """
        return getattr(self.__args, key)

    def parser(self):
        """
        Returns the parser instance

        :return:
        """
        return self.__parser

    def run(self):
        """
        Starts the ULCLI program

        This program has three main starting steps
            1. Initialize the argument parser
            2. On mode, it replaces / and - into underscore (to dynamically call desired mode)
            3. Dynamically runs the mode
        """

        # Initialize / prepares the arg parser
        self.__init_arg_parser()

        # Replaces / and - with underscore
        mode_class = self.__args.mode.replace('/', '_').replace('-', '_')

        # Dynamically call the module requested by the user
        getattr(mode, 'mode_%s' % mode_class).run()

    def __init_arg_parser(self):
        """
        Step 1 of ULCLI Program (Initializing argument parser)
        """

        # Creates new instance of parser
        self.__parser = argparse.ArgumentParser(description=self.__description,
                                                formatter_class=argparse.RawTextHelpFormatter)

        # --url argument
        self.__parser.add_argument('-u', '--url', help=self.__lang.ulcli_arg_url_help, required=True)

        # Initializes the modes
        mode.init(
            self.__lang,
            self.__parser.add_subparsers(
                title='Modes',
                description=self.__lang.ulcli_sub_mode_desc,
                help=self.__lang.ulcli_sub_mode_help,
                dest='mode'))

        # Initializes the parser arguments
        self.__args = self.__parser.parse_args()
