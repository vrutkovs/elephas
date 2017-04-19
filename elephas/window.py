# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gio
from gettext import gettext as _

from elephas.utils import log
from elephas.widgets.toolbar import Toolbar, ToolbarState
from elephas.widgets.toots_list import TootsList


class Window(Gtk.ApplicationWindow):

    def __repr__(self):
        return '<Window>'

    @log
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       application=app,
                                       title=_("Elephas"))
        self.settings = Gio.Settings.new('com.github.Elephas')

        self._restore_window()
        self._setup_view()

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
    def _setup_view(self):
        self._box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.toolbar = Toolbar()
        self.set_titlebar(self.toolbar.header_bar)
        self.toolbar.set_state(ToolbarState.HOME_TIMELINE)
        self.toolbar.header_bar.show()

        self._box.pack_start(self.toolbar.viewswitcher, False, True, 0)
        self.toolbar.viewswitcher.show()

        self.tootslist = TootsList()
        self._box.pack_end(self.tootslist.listbox, True, True, 0)
        self.tootslist.listbox.show()

        self._box.set_homogeneous(False)
        self._box.show()

        self.add(self._box)
        self.show()
