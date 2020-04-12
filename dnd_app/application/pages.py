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
    self.add(Gtk.Label(label='Characters'))
    btns = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
    def create_on_clicked(character:characters.Character):
      def on_clicked(actionable):
        self.appwin.navigate(CharacterPage(self.appwin, character))
      return on_clicked
    for character in characters.get_characters():
      btn = Gtk.Button()
      box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
      box.add(Gtk.Label(label=character.name))
      box.add(Gtk.Label(label=f'{character.description()} {character.class0}'))
      btn.add(box)
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
    self.add(Gtk.Label(label=character.name))
    self.add(Gtk.Label(label=character.description()))
    self.add(Gtk.Label(label=character.class0))
