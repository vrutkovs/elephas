from gi.repository import Gtk, GObject

from elephas.utils import log
import logging
logger = logging.getLogger(__name__)


class TootsList(GObject.GObject):
    def __repr__(self):
        return '<TootsList>'

    @log
    def __init__(self):
        GObject.GObject.__init__(self)
        self._ui = Gtk.Builder()
        self._ui.add_from_resource('/com/github/Elephas/tootslist.ui')

        self.listbox = self._ui.get_object('toots')
