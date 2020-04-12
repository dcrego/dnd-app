import unittest

from dnd_app.abilities import Ability

class TestAbilities(unittest.TestCase):

  abilities=None

  def __new__(cls, testname:str):
    from dnd_app.abilities import AbilityLoader
    if not cls.abilities:
      cls.abilities = AbilityLoader().abilities
    return unittest.TestCase.__new__(cls)

  def test_abilities(self):
    assert len(self.abilities) == 6, len(self.abilities)

  def test_str(self):
    assert type(self.abilities[0]) == Ability, type(self.abilities[0])
    key = 'STR'
    assert repr(self.abilities[0]) == f'Ability({key})', repr(self.abilities[0])
    assert str(self.abilities[0]) == key, str(self.abilities[0])
    assert self.abilities[0].key == key, self.abilities[0].key
    assert self.abilities[0].name == 'strength', self.abilities[0].name

  def test_dex(self):
    assert type(self.abilities[1]) == Ability, type(self.abilities[1])
    key = 'DEX'
    assert repr(self.abilities[1]) == f'Ability({key})', repr(self.abilities[1])
    assert str(self.abilities[1]) == key, str(self.abilities[1])
    assert self.abilities[1].key == key, self.abilities[1].key
    assert self.abilities[1].name == 'dexterity', self.abilities[1].name

  def test_con(self):
    assert type(self.abilities[2]) == Ability, type(self.abilities[0])
    key = 'CON'
    assert repr(self.abilities[2]) == f'Ability({key})', repr(self.abilities[2])
    assert str(self.abilities[2]) == key, str(self.abilities[2])
    assert self.abilities[2].key == key, self.abilities[2].key
    assert self.abilities[2].name == 'constitution', self.abilities[2].name

  def test_int(self):
    assert type(self.abilities[3]) == Ability, type(self.abilities[0])
    key = 'INT'
    assert repr(self.abilities[3]) == f'Ability({key})', repr(self.abilities[3])
    assert str(self.abilities[3]) == key, str(self.abilities[3])
    assert self.abilities[3].key == key, self.abilities[3].key
    assert self.abilities[3].name == 'intelligence', self.abilities[3].name

  def test_wis(self):
    assert type(self.abilities[4]) == Ability, type(self.abilities[0])
    key = 'WIS'
    assert repr(self.abilities[4]) == f'Ability({key})', repr(self.abilities[4])
    assert str(self.abilities[4]) == key, str(self.abilities[4])
    assert self.abilities[4].key == key, self.abilities[4].key
    assert self.abilities[4].name == 'wisdom', self.abilities[4].name

  def test_cha(self):
    assert type(self.abilities[5]) == Ability, type(self.abilities[0])
    key = 'CHA'
    assert repr(self.abilities[5]) == f'Ability({key})', repr(self.abilities[5])
    assert str(self.abilities[5]) == key, str(self.abilities[5])
    assert self.abilities[5].key == key, self.abilities[5].key
    assert self.abilities[5].name == 'charisma', self.abilities[5].name


if __name__=='__main__':
  unittest.main()