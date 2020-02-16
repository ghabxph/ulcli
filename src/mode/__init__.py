from mode.mode_main_get_token import Mgt
from mode.mode_main_setup import Mst
from mode.mode_manage import Man
from mode.mode_manage_setup import Mtp

mode_main_get_token = None
mode_main_setup = None
mode_manage = None
mode_manage_setup = None


def init(lang, sp):
    """
    Initializes the modes

    :param sp: Subparser instance
    :return:
    """
    global mode_main_get_token, mode_main_setup, mode_manage, mode_manage_setup

    mode_main_get_token = Mgt.inst(lang).setup(sp)
    mode_main_setup = Mst.inst(lang).setup(sp)
    mode_manage = Man.inst(lang).setup(sp)
    mode_manage_setup = Mtp.inst(lang).setup(sp)
