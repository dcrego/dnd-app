from gi.repository import Gtk

class CharactersBox(Gtk.Box):
  def __init__(self, show_character_box):
    super().__init__(orientation=Gtk.Orientation.VERTICAL)
    lbl = Gtk.Label(label='Characters')
    self.add(lbl)
    btns = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
    def create_on_clicked(character:dict):
      def on_clicked(evt_source):
        show_character_box(character)
      return on_clicked
    import characters
    for character in characters.get_characters():
      btn = Gtk.Button(label=character['alias'])
      btn.connect('clicked', create_on_clicked(character))
      btns.add(btn)
    self.add(btns)

class CharacterBox(Gtk.Box):
  def __init__(self, character:dict):
    super().__init__(orientation=Gtk.Orientation.VERTICAL)
    lbl = Gtk.Label(label=character['alias'])
    self.add(lbl)
    lbl = Gtk.Label(label=character['description'])
    self.add(lbl)
