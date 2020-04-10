def main() -> None:
  import gi
  gi.require_version('Gtk', '3.0')
  from gi.repository import Gtk
  from dnd_app.application import Application
  Application().run()

if __name__=='__main__':
  main()
