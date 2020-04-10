from gi.repository import Gtk
from .. import characters


class Page:

  def __init__(self, appwin):
    super().__init__()
    self.appwin = appwin


class CharactersPage(Gtk.Box, Page):

  def __init__(self, appwin):
    Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
    Page.__init__(self, appwin)
    lbl = Gtk.Label(label='Characters')
    self.add(lbl)
    btns = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
    def create_on_clicked(character:characters.Character):
      def on_clicked(actionable):
        self.appwin.navigate(CharacterPage(self.appwin, character))
      return on_clicked
    for character_data in characters.get_characters():
      character=characters.Character(character_data)
      btn = Gtk.Button(label=character.alias)
      btn.connect('clicked', create_on_clicked(character))
      btns.add(btn)
    self.add(btns)


class CharacterPage(Gtk.Box, Page):

  def __init__(self, appwin, character:characters.Character):
    Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
    Page.__init__(self, appwin)
    btn = Gtk.Button(label='← back')
    def on_click(actionable):
      self.appwin.navigate_back()
    btn.connect('clicked', on_click)
    self.add(btn)
    lbl = Gtk.Label(label=character.alias)
    self.add(lbl)
    lbl = Gtk.Label(label=character.description)
    self.add(lbl)
