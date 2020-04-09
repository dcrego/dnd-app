# Load Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_on_clicked(n:int):
    def on_clicked(btn):
        print('on_clicked')
        print('n:', n)
        print('btn:', btn)
    return on_clicked

def on_activate(app:Gtk.Application):
    winsize = {
        'default-width': 400,
        'default-height': 600
    }
    win = Gtk.ApplicationWindow(application=app, title='D&D Companion', **winsize)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    lbl = Gtk.Label('Characters')
    box.add(lbl)
    btns = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
    for n in range(1, 5):
        btn = Gtk.Button(label='Character %d'%n)
        btn.connect('clicked', create_on_clicked(n))
        btns.add(btn)
    box.add(btns)
    win.add(box)
    win.show_all()

def main():
    app = Gtk.Application(application_id='org.dcrego.dnd-app')
    app.connect('activate', on_activate)
    app.run()

if __name__=='__main__':
    main()
