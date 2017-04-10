# -*- coding: utf-8 -*-
import logging
import argparse
import sys
import signal
import gi
import os
import locale
import gettext

gi.require_version('Gtk', '3.0')  # noqa
from gi.repository import Gtk, Gio
from elephas.app import Application
from elephas.pkg_config import localedir, pkgdatadir


def install_excepthook():
    """ Make sure we exit when an unhandled exception occurs. """

    old_hook = sys.excepthook

    def new_hook(etype, evalue, etb):
        old_hook(etype, evalue, etb)
        while Gtk.main_level():
            Gtk.main_quit()
        sys.exit()
    sys.excepthook = new_hook


def main():
    install_excepthook()

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', "--debug", action="store_true", default=False, dest="debug")
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s\t%(message)s',
                            datefmt='%H:%M:%S')
        # Gtk hates "-d" switch, so lets drop it
        if '-d' in sys.argv:
            sys.argv.remove("-d")
        if '--debug' in sys.argv:
            sys.argv.remove("--debug")
    else:
        logging.basicConfig(level=logging.WARN,
                            format='%(asctime)s %(levelname)s\t%(message)s',
                            datefmt='%H:%M:%S')

    locale.bindtextdomain('elephas', localedir)
    locale.textdomain('elephas')
    gettext.bindtextdomain('elephas', localedir)
    gettext.textdomain('elephas')

    resource = Gio.resource_load(os.path.join(pkgdatadir, 'elephas.gresource'))
    Gio.Resource._register(resource)

    app = Application()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == "__main__":
    main()
