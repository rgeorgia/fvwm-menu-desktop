#!/usr/pkg/bin/python3.9
"""
fvwm-menu-desktop_generate.py
A script which parses xdg menu definitions to build the corresponding fvwm menus.

For original Change Log data see ChangeLog.md
"""
from argparse import Namespace
from fvwm_menu_desktop_args import desktop_menu_args


def main(args: Namespace) -> None:
    print(args)


if __name__ == "__main__":
    main(args=desktop_menu_args())
