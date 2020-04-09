# Load Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_on_clicked(character:dict):
    def on_clicked(evt_source):
        print('on_clicked')
        print('character:', character)
        print('evt_source:', evt_source)
    return on_clicked

def on_activate(app:Gtk.Application) -> None:
    winsize = {
        'default-width': 400,
        'default-height': 600
    }
    win = Gtk.ApplicationWindow(application=app, title='D&D Companion', **winsize)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    lbl = Gtk.Label(label='Characters')
    box.add(lbl)
    btns = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
    import characters
    for character in characters.get_characters():
        btn = Gtk.Button(label=character['alias'])
        btn.connect('clicked', create_on_clicked(character))
        btns.add(btn)
    box.add(btns)
    win.add(box)
    win.show_all()

def main() -> None:
    app = Gtk.Application(application_id='org.dcrego.dnd-app')
    app.connect('activate', on_activate)
    app.run()

if __name__=='__main__':
    main()
