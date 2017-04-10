# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gio
from gettext import gettext as _

from elephas.utils import log


class Window(Gtk.ApplicationWindow):

    def __repr__(self):
        return '<Window>'

    @log
    def _restore_window(self):
        size_setting = self.settings.get_value('window-size')
        if isinstance(size_setting[0], int) and isinstance(size_setting[1], int):
            self.resize(size_setting[0], size_setting[1])

        position_setting = self.settings.get_value('window-position')
        if len(position_setting) == 2 \
           and isinstance(position_setting[0], int) \
           and isinstance(position_setting[1], int):
            self.move(position_setting[0], position_setting[1])

        if self.settings.get_value('window-maximized'):
            self.maximize()

        self.window_size_update_timeout = None
        self.connect("window-state-event", self._on_window_state_event)

    @log
    def _on_window_state_event(self, widget, event):
        event_names = event.new_window_state.value_names
        self.settings.set_boolean('window-maximized',
                                  'GDK_WINDOW_STATE_MAXIMIZED' in event_names)

    @log
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       application=app,
                                       title=_("Elephas"))
        self.settings = Gio.Settings.new('com.github.Elephas')

        self._restore_window()
