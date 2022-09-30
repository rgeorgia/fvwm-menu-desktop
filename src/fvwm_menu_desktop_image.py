"""
fvwm_menu_desktop_image.py
Handles all the imaage and icon stuff for menus
"""

import PIL
import os
import sys


class BaseIconScaleTool:
    size = 32
    icon_dir = ""
    enable_icon = True

    def __init__(self, filename):
        self.filename = filename

    def _do_check(self):
        sys.stderr.write(
            f"Cannot find ImageMagick binaries or PIL module. Skipping scaling icon {self.filename}\n"
        )
        return True

    def check_size(self):
        if self.filename.endswith(".svg"):
            return False
        try:
            return self._do_check()
        except:
            # Always try to convert if check_size() fails.
            # Worst case convert() would fail and ignore the icon.
            return False

    def convert(self, theme_changed):
        # FVWM knows how to render SVGs
        if self.filename.endswith(".svg"):
            return "{0}:{1}x{1}".format(self.filename, self.size)

        output = self._output_path()

        if (
            theme_changed
            or not os.path.isfile(output)
            or os.path.getmtime(self.filename) > os.path.getmtime(output)
        ):
            try:
                self._do_convert(output)
            except:
                sys.stderr.write("Fail to convert %s.\n" % self.filename)
                return None

        return output

    def _output_path(self):
        if not os.path.isdir(os.path.expanduser(self.icon_dir)):
            os.makedirs(os.path.expanduser(self.icon_dir))
        return os.path.join(
            os.path.expanduser(self.icon_dir),
            "%ix%i-" % (self.size, self.size) + os.path.basename(self.filename),
        )


class ImageMagickIconScaleTool(BaseIconScaleTool):
    def _do_check(self):
        with os.popen("identify -format %%w '%s'" % self.filename, "r") as p:
            return int(p.read()) == self.size

    def _do_convert(self, output):
        if (
            os.system(
                "convert '%s'[0] -resize %i '%s'" % (self.filename, self.size, output)
            )
            != 0
        ):
            raise ValueError("convert process return non-zero status code")


class PILIconScaleTool(BaseIconScaleTool):
    def _do_check(self):
        with PIL.Image.open(self.filename) as f:
            return f.size[0] == self.size

    def _do_convert(self, output):
        with PIL.Image.open(self.filename) as f:
            f.thumbnail((self.size, self.size))
            f.save(output, "PNG")
