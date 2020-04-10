from gi.repository import Gtk
from . import pages

class Application(Gtk.Application):

  def __init__(self):
    options = {
      'application_id': 'org.dcrego.dnd-app'
    }
    super().__init__(**options)
    def on_activate(app:Application):
      appwin = ApplicationWindow(app)
      appwin.navigate(pages.CharactersPage(appwin))
    self.connect('activate', on_activate)


class ApplicationWindow(Gtk.ApplicationWindow):

  def __init__(self, app:Application):
    options = {
      'application': app,
      'title': 'D&D Companion',
      'default-width': 400,
      'default-height': 600
    }
    super().__init__(**options)
    self.current_page=None

  def navigate(self:Gtk.ApplicationWindow, target_page:pages.Page):
    if (self.current_page):
      self.remove(self.current_page)
    self.add(target_page)
    self.current_page = target_page
    self.show_all()
