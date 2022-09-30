# Modification History

Changed on 06/01/20 by Dominique Michel:
- Fix converting of multi-images icon files;
use the first one.

Changed on 18/03/19 by Jaimos Skriletz:
- Updated script for and require Python 3.
- Drop support for Python 2.
- Added support for xdg.Menu.Separator.
- Added option --term-cmd to state the terminal emulator command
to use with Terminal=True .desktop entries. Default: xterm -e

Changed on 16/12/31 by Jaimos Skriletz:
- Added check for FVWM_USERDIR env variable.
- Added check for python-xdg module to print less errors if not found.
- Added option -e/--menu-error to output phython-xdg not found as
a menu for the default-config.

Changed on 16/10/27 by Jaimos Skrietz:
- Renamed default menu to XDGMenu and changed the name of the
FvwmForm to FvwmForm-XDGMenu-Config
- Modified the FvwmForm and added the abilty to load defaults from
the Form's data file.
- Changed default to generate menu titles. Disable with --without-titles
- The top level menu now has two additional items:
'Regenerate' - Regenerates menu.
'Configure' - Opens up FvwmForm-XDGMenu-Config.
- Added --regen-cmd "CMD" for a fvwm CMD to use on the Regenerate item.
Default: PipeRead `fvwm-menu-desktop`
- Added --include-items [config|regenerate|both|none] option
to control if the additional items are included in the menu.
- Added --dynamic option to be used with dynamic menus.
- Added --all-menus option to generate all menus and not try to determine
which one is best
- Changed default behavior to include menu titles.
- Added new option --without-titles

Changed on 25/02/14 by Thomas Funk:
- Converting of icons always to png

Changed on 06/10/13 by Thomas Funk:
Some Bugfixes:
- DecodeEncodeErrors in menu names
- no output appears with 'fvwm-menu-desktop --get-menus all|desktop'
- No entry "Regenerate XDG menu(s)" appears with
'fvwm-menu-desktop --insert-in-menu MenuRoot'
- exchange all tabs with spaces to prevent indention errors
- add two new options: --app-icon --dir-icon
to handle default icons for not available app/dir icons
- fix bug in convert icon routine that background of svg icons are
transparent
Changed on 15/06/13 by Thomas Funk:
support for python-xdg > 0.19.
add gettext localization.

Changed on 10/01/12 by Thomas Funk:
Unicode support.
Changed on 01/26/12 by Dan Espen (dane):
Make compatible with fvwm-menu-desktop.
Restored DestroyMenu, needed for reload menus.
Remove bug, was printing iconpath on converted icons
Replace obsolete optparse, use getopt instead
Change from command line arg for applications.menu
change to using ?$XDG_MENU_PREFIX or theme? fixme
- use "Exec exec" for all commands, remove option.

fixme, fix documentation, FvwmForm-Desktop, usage prompt is wrong
change, mini icons are enabled by default.
there are rescalable icons.

Author: Piotr Zielinski (http://www.cl.cam.ac.uk/~pz215/)
Licence: GPL 2
Date: 03.12.2005

This script takes names of menu files conforming to the XDG Desktop
Menu Specification, and outputs their FVWM equivalents to the
standard output.

http://standards.freedesktop.org/menu-spec/latest/

This script requires the python-xdg module, which in Debian can be
installed by typing

apt-get install python3-xdg

On Fedora, python-xdg is installed by default.
