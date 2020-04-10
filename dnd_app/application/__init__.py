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
    self.page_stack=[]

  def navigate(self, target_page:pages.Page):
    if (self.page_stack):
      self.remove(self.page_stack[-1])
    self.add(target_page)
    self.page_stack.append(target_page)
    self.show_all()
  
  def navigate_back(self):
    current_page= self.page_stack.pop()
    self.remove(current_page)
    self.add(self.page_stack[-1])
    self.show_all()
