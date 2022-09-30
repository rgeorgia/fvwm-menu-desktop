"""
fvwm_menu_desktop_args.py
Handling of commandline argumenst are done here
"""

import argparse


def desktop_menu_argse():
    """ get the parames for desktop menu"""

    parser = argparse.ArgumentParser(description="Create fvwm desktop menu")
    # should use file type
    parser.add_argument('--install-prefix', dest='install_prefix', metavar="<DIR>",
            help="install prefix of the desktop menu files. Per default not set. For system wide menus use /etc/xdg/menus/.")
    parser.add_argument("--desktop", dest="desktop", metavar="<NAME>", help="use menus that include NAME in the file name: gnome, kde, xfce, lxde, debian, etc.")

    return parser.parse_args()
