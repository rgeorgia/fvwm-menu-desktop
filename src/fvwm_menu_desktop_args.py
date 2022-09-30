"""
fvwm_menu_desktop_args.py
Handling of commandline argumenst are done here
"""

import argparse
from fvwm_menu_desktop_constants import (
    DEFAULT_ICON_DIR,
    DEFAULT_APP_NAME,
    DEFAULT_ICON_SIZE,
)


def desktop_menu_args():
    """get the parames for desktop menu"""

    parser = argparse.ArgumentParser(description="Create fvwm desktop menu")
    # should use file type
    parser.add_argument(
        "--install-prefix",
        dest="install_prefix",
        metavar="<DIR>",
        help="install prefix of the desktop menu files. Per default not set. "
        "For system wide menus use /etc/xdg/menus/.",
    )
    parser.add_argument(
        "--desktop",
        dest="desktop",
        metavar="<NAME>",
        help="use menus that include NAME in the file name: gnome, kde, xfce, lxde, debian, etc.",
    )
    parser.add_argument(
        "--theme",
        dest="theme",
        metavar="<NAME>",
        help="icon theme: gnome (default), oxygen, etc. Don't use hicolor. "
        "It's the default fallback theme if no icon is found.",
    )
    parser.add_argument(
        "-w",
        "--with-titles",
        dest="with_titles",
        help="Generate menus with titles. Default.",
    )
    # should be a true/false
    parser.add_argument(
        "--without-titles",
        dest="without_titles",
        type=bool,
        help="generate menus without titles.",
    )
    parser.add_argument(
        "--enable-mini-icons",
        dest="enable_mini_icons",
        type=bool,
        help="enable mini-icons in menu.",
    )

    parser.add_argument(
        "-s",
        "--size",
        dest="size",
        metavar="<NUM>",
        type=int,
        default=DEFAULT_ICON_SIZE,
        help="set size of mini-icons in menu. Default is 24.",
    )
    # should be file type
    parser.add_argument(
        "--mini-icon-dir",
        dest="mini_icon_dir",
        metavar="<DIR>",
        default=DEFAULT_ICON_DIR,
        help="set directory for mini-icons. Default is ~/.fvwm/icons.",
    )
    parser.add_argument(
        "--menu-type",
        dest="menu_type",
        metavar="<NAME>",
        help="use menus that include NAME in the file name: applications, settings, "
        "preferences, etc. When used with --desktop only menus whose file name "
        "matches '*desktop*menutype*' are used.",
    )
    parser.add_argument(
        "--app-icon",
        dest="app_icon",
        metavar="<NAME>",
        default=DEFAULT_APP_NAME,
        help="set default application icon if no others found. Default is 'gnome-applications'.",
    )
    # should be file type
    parser.add_argument(
        "--dir-icon",
        dest="dir_icon",
        metavar="<NAME>",
        help="set default directory icon if no others found.",
    )
    # parser.add_argument("", dest="", metavar="", help="")
    # parser.add_argument("", dest="", metavar="", help="")
    # parser.add_argument("", dest="", metavar="", help="")
    # parser.add_argument("", dest="", metavar="", help="")
    # parser.add_argument("", dest="", metavar="", help="")

    return parser.parse_args()
