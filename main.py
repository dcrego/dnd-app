# Load Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_activate(app:Gtk.Application) -> None:
  winsize = {
    'default-width': 400,
    'default-height': 600
  }
  win = Gtk.ApplicationWindow(application=app, title='D&D Companion', **winsize)
  from boxes import CharactersBox
  win.add(CharactersBox())
  win.show_all()

def main() -> None:
  app = Gtk.Application(application_id='org.dcrego.dnd-app')
  app.connect('activate', on_activate)
  app.run()

if __name__=='__main__':
  main()
