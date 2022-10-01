"""
fvwm_menu_desktop_args.py
Handling of commandline argumenst are done here
"""

import argparse
from fvwm_menu_desktop_constants import (
    DEFAULT_ICON_DIR,
    DEFAULT_APP_NAME,
    DEFAULT_ICON_SIZE,
    DEFAULT_GNOME_FS_DIR,
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
        action=argparse.BooleanOptionalAction,
        help="Generate menus with titles. Default.",
    )
    parser.add_argument(
        "--without-titles",
        dest="without_titles",
        action=argparse.BooleanOptionalAction,
        help="generate menus without titles.",
    )
    parser.add_argument(
        "--enable-mini-icons",
        dest="enable_mini_icons",
        action=argparse.BooleanOptionalAction,
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
        default=DEFAULT_GNOME_FS_DIR,
        help="set default directory icon if no others found. Default is 'gnome-fs-directory'.",
    )
    parser.add_argument(
        "-t",
        "--title",
        dest="title",
        metavar="<NAME>",
        type=str,
        help="menu title of the top menu used by Popup command. Default is XDGMenu.",
    )
    parser.add_argument(
        "--insert-in-menu",
        dest="insert_in_menu",
        metavar="<NAME>",
        type=str,
        help="generates a menu to place it in the root level of the menu NAME.",
    )
    parser.add_argument(
        "--get-menus",
        dest="get_menus",
        choices=["all", "desktop"],
        help="Prints a space separated list of full menu paths. "
        "'all' is all menus on the system except empty ones. "
        "'desktop' list the menus that would have been generated. "
        "No menu generation is done.",
    )
    parser.add_argument(
        "--set-menus",
        dest="set_menu",
        metavar="<MENU PATHS>",
        help="expects a space separated list of full menu paths to generate user specified menus.",
    )
    parser.add_argument(
        "--all-menus",
        dest="all_menus",
        action=argparse.BooleanOptionalAction,
        help="Generate all menus found",
    )

    parser.add_argument(
        "--include-items",
        dest="include_items",
        choices=["config", "regenerate", "both", None],
        default="both",
        help="include additional menu items NAME in top level menu. "
        "NAME can be 'config', 'regenerate', 'both' or 'none'. Default both.",
    )
    parser.add_argument(
        "--regen-cmd",
        dest="regen_cmd",
        metavar="<ACTION>",
        type=str,
        default="PipeRead `fvwm-menu-desktop`",
        help="The fvwm ACTION for the 'Regenerate' menu item. "
        "Default: 'PipeRead `fvwm-menu-desktop`'",
    )
    parser.add_argument(
        "--term-cmd",
        dest="term_cmd",
        metavar="<CMD>",
        type=str,
        default="xterm -e",
        help="Terminal emulator CMD used on terminal entries. Default: xterm -e",
    )

    parser.add_argument(
        "--dynamic",
        dest="dynamic",
        action=argparse.BooleanOptionalAction,
        help="used with dynamic menus",
    )
    parser.add_argument(
        "-e",
        "--menu-error",
        dest="menu_error",
        action=argparse.BooleanOptionalAction,
        help="out python-xdg not found error in menu.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action=argparse.BooleanOptionalAction,
        help="run and display debug info on STDERR",
    )

    return parser.parse_args()
