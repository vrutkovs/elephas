from gi.repository import Gtk, GObject
from gettext import gettext as _

from elephas.utils import log
import logging
logger = logging.getLogger(__name__)


class ToolbarState:
    HOME_TIMELINE = 0
    TOOT_DETAILS = 1
    NOTIFICATIONS = 2
    LOCAL_TIMELINE = 3
    FEDERATED_TIMELINE = 4


class Toolbar(GObject.GObject):
    def __repr__(self):
        return '<Toolbar>'

    @log
    def __init__(self):
        GObject.GObject.__init__(self)
        self._stack_switcher = Gtk.StackSwitcher(can_focus=False,
                                                 halign="center")
        self._stack_switcher.show()
        self._headerbar_ui = Gtk.Builder()
        self._headerbar_ui.add_from_resource('/com/github/Elephas/headerbar.ui')
        self.header_bar = self._headerbar_ui.get_object('header-bar')
        self._back_button = self._headerbar_ui.get_object('back-button')

        self._viewswitcher_ui = Gtk.Builder()
        self._viewswitcher_ui.add_from_resource('/com/github/Elephas/viewswitcher.ui')
        self.viewswitcher = self._viewswitcher_ui.get_object('viewswitcher')
        self.home_btn = self._viewswitcher_ui.get_object('home-timeline-button')
        self.notifications_btn = self._viewswitcher_ui.get_object('notifications-button')
        self.local_timeln_btn = self._viewswitcher_ui.get_object('local-timeline-button')
        self.federated_timeln_btn = self._viewswitcher_ui.get_object('federated-timeline-button')

    @log
    def set_state(self, state):
        self._state = state
        self._update()

    @log
    def _update(self):
        self.reset_header_title()
        self._back_button.set_visible(self._state == ToolbarState.TOOT_DETAILS)

    @log
    def reset_header_title(self):
        self.header_bar.set_title(_("Elephas"))
        self.header_bar.set_custom_title(self._stack_switcher)
