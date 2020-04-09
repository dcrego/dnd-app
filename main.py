# Hello-world from https://www.gtk.org/
# Load Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# When the application is launched…
def on_activate(app):
    # … create a new window…
    win = Gtk.ApplicationWindow(application=app)
    # … with a button in it…
    btn = Gtk.Button(label='Hello, World!')
    # … which closes the window when clicked
    btn.connect('clicked', lambda x: win.destroy())
    win.add(btn)
    win.show_all()

def main():
    # Create a new application
    app = Gtk.Application(application_id='com.example.GtkApplication')
    app.connect('activate', on_activate)

    # Run the application
    app.run(None)

if __name__=='__main__':
    main()
