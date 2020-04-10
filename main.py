# Load Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def show_character_box(character:dict) -> None:
  global win, current_box
  win.remove(current_box)
  from boxes import CharacterBox
  current_box = CharacterBox(character)
  win.add(current_box)
  win.show_all()

def on_activate(app:Gtk.Application) -> None:
  winsize = {
    'default-width': 400,
    'default-height': 600
  }
  global win, current_box
  win = Gtk.ApplicationWindow(application=app, title='D&D Companion', **winsize)
  from boxes import CharactersBox
  current_box = CharactersBox(show_character_box)
  win.add(current_box)
  win.show_all()

def main() -> None:
  app = Gtk.Application(application_id='org.dcrego.dnd-app')
  app.connect('activate', on_activate)
  app.run()

if __name__=='__main__':
  main()
