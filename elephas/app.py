# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gio, GLib, Gdk
from gettext import gettext as _

from elephas.utils import log
from elephas.window import Window


class Application(Gtk.Application):
    def __repr__(self):
        return '<Application>'

    @log
    def __init__(self):
        Gtk.Application.__init__(self, application_id='com.github.Elephas',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        GLib.set_application_name(_("Elephas"))
        GLib.set_prgname('elephas')
        self._settings = Gio.Settings.new('com.github.Elephas')
        self._init_style()
        self._window = None

    @log
    def _init_style(self):
        # TODO: this is unused atm:
        #     Failed to import: The resource at “/com/github/Elephas/application.css” does not exist
        css_provider_file = Gio.File.new_for_uri(
            'resource:///com/github/Elephas/application.css')
        css_provider = Gtk.CssProvider()
        css_provider.load_from_file(css_provider_file)
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    @log
    def _build_app_menu(self):
        action_entries = [
            ('about', self._about),
            ('help', self._help),
            ('quit', self.quit),
        ]

        for action, callback in action_entries:
            gio_action = Gio.SimpleAction.new(action, None)
            gio_action.connect('activate', callback)
        self.add_action(gio_action)

    @log
    def _help(self, action, param):
        Gtk.show_uri(None, "help:elephas", Gdk.CURRENT_TIME)

    @log
    def _about(self, action, param):
        def about_response(dialog, response):
            dialog.destroy()

        builder = Gtk.Builder()
        builder.add_from_resource('/com/github/Elephas/AboutDialog.ui')
        about = builder.get_object('about_dialog')
        about.set_transient_for(self._window)
        about.connect("response", about_response)
        about.show()

    @log
    def do_startup(self):
        Gtk.Application.do_startup(self)
        self._build_app_menu()

    @log
    def quit(self, action=None, param=None):
        self._window.destroy()

    @log
    def do_activate(self):
        if not self._window:
            self._window = Window(self)

        self._window.present()
