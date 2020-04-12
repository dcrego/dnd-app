import unittest
from dnd_app import races


class TestDefaultRace(unittest.TestCase):

  __race = races.Race()

  def test_name(self):
    race = type(self).__race
    assert repr(race) == 'Race(None)', repr(race)
    assert race.name == None, race.name

  def test_ability_mods_str(self):
    race = type(self).__race
    assert race.ability_mods.str == 0, race.ability_mods.str

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert race.ability_mods.dex == 0, race.ability_mods.dex

  def test_ability_mods_con(self):
    race = type(self).__race
    assert race.ability_mods.con == 0, race.ability_mods.con

  def test_ability_mods_int(self):
    race = type(self).__race
    assert race.ability_mods.int == 0, race.ability_mods.int

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert race.ability_mods.wis == 0, race.ability_mods.wis

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert race.ability_mods.cha == 0, race.ability_mods.cha

  def test_size(self):
    race = type(self).__race
    assert race.size == 'medium', race.size

  def test_speed(self):
    race = type(self).__race
    assert race.speed == 30, race.speed


class TestRaceLoader(unittest.TestCase):

  __loader = races.RaceLoader()

  def test_race_loader_singleton(self):
    loader1 = races.RaceLoader()
    index1 = loader1._RaceLoader__index
    loader2 = races.RaceLoader()
    index2 = loader2._RaceLoader__index
    assert id(loader1) == id(loader2), (id(loader1), id(loader2))
    assert id(index1) == id(index2), (id(index1), id(index2))

  def test_keys_len(self):
    loader = type(self).__loader
    assert len(loader.keys()) >= 4, len(loader.keys())

  def test_load_dwarf(self):
    loader = type(self).__loader
    assert 'dwarf' in loader.keys()
    race = loader.load('dwarf')
    assert repr(race) == "Race('dwarf')", repr(race)
    assert race.name == 'dwarf', race.name

  def test_load_elf(self):
    loader = type(self).__loader
    assert 'elf' in loader.keys()
    race = loader.load('elf')
    assert repr(race) == "Race('elf')", repr(race)
    assert race.name == 'elf', race.name

  def test_load_halfling(self):
    loader = type(self).__loader
    assert 'halfling' in loader.keys()
    race = loader.load('halfling')
    assert repr(race) == "Race('halfling')", repr(race)
    assert race.name == 'halfling', race.name

  def test_load_human(self):
    loader = type(self).__loader
    assert 'human' in loader.keys()
    race = loader.load('human')
    assert repr(race) == "Race('human')", repr(race)
    assert race.name == 'human', race.name


class TestDwarfRace(unittest.TestCase):

  __race = races.load_race('dwarf')

  def test_name(self):
    race = type(self).__race
    assert repr(type(self).__race) == "Race('dwarf')", repr(type(self).__race)
    assert race.name == 'dwarf', race.name

  def test_ability_mods_str(self):
    race = type(self).__race
    assert race.ability_mods.str == 0, race.ability_mods.str

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert race.ability_mods.dex == 0, race.ability_mods.dex

  def test_ability_mods_con(self):
    race = type(self).__race
    assert race.ability_mods.con == 2, race.ability_mods.con

  def test_ability_mods_int(self):
    race = type(self).__race
    assert race.ability_mods.int == 0, race.ability_mods.int

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert race.ability_mods.wis == 0, race.ability_mods.wis

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert race.ability_mods.cha == -2, race.ability_mods.cha

  def test_size(self):
    race = type(self).__race
    assert race.size == 'medium', race.size

  def test_speed(self):
    race = type(self).__race
    assert race.speed == 20, race.speed


class TestElffRace(unittest.TestCase):

  __race = races.load_race('elf')

  def test_name(self):
    race = type(self).__race
    assert repr(type(self).__race) == "Race('elf')", repr(type(self).__race)
    assert race.name == 'elf', race.name

  def test_ability_mods_str(self):
    race = type(self).__race
    assert race.ability_mods.str == 0, race.ability_mods.str

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert race.ability_mods.dex == 2, race.ability_mods.dex

  def test_ability_mods_con(self):
    race = type(self).__race
    assert race.ability_mods.con == -2, race.ability_mods.con

  def test_ability_mods_int(self):
    race = type(self).__race
    assert race.ability_mods.int == 0, race.ability_mods.int

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert race.ability_mods.wis == 0, race.ability_mods.wis

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert race.ability_mods.cha == 0, race.ability_mods.cha

  def test_size(self):
    race = type(self).__race
    assert race.size == 'medium', race.size

  def test_speed(self):
    race = type(self).__race
    assert race.speed == 30, race.speed


class TestHalflingfRace(unittest.TestCase):

  __race = races.load_race('halfling')

  def test_name(self):
    race = type(self).__race
    assert repr(type(self).__race) == "Race('halfling')", repr(type(self).__race)
    assert race.name == 'halfling', race.name

  def test_ability_mods_str(self):
    race = type(self).__race
    assert race.ability_mods.str == -2, race.ability_mods.str

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert race.ability_mods.dex == 2, race.ability_mods.dex

  def test_ability_mods_con(self):
    race = type(self).__race
    assert race.ability_mods.con == 0, race.ability_mods.con

  def test_ability_mods_int(self):
    race = type(self).__race
    assert race.ability_mods.int == 0, race.ability_mods.int

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert race.ability_mods.wis == 0, race.ability_mods.wis

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert race.ability_mods.cha == 0, race.ability_mods.cha

  def test_size(self):
    race = type(self).__race
    assert race.size == 'small', race.size

  def test_speed(self):
    race = type(self).__race
    assert race.speed == 20, race.speed


class TestHumanRace(unittest.TestCase):

  __race = races.load_race('human')

  def test_name(self):
    race = type(self).__race
    assert repr(type(self).__race) == "Race('human')", repr(type(self).__race)
    assert race.name == 'human', race.name

  def test_ability_mods_str(self):
    race = type(self).__race
    assert race.ability_mods.str == 0, race.ability_mods.str

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert race.ability_mods.dex == 0, race.ability_mods.dex

  def test_ability_mods_con(self):
    race = type(self).__race
    assert race.ability_mods.con == 0, race.ability_mods.con

  def test_ability_mods_int(self):
    race = type(self).__race
    assert race.ability_mods.int == 0, race.ability_mods.int

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert race.ability_mods.wis == 0, race.ability_mods.wis

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert race.ability_mods.cha == 0, race.ability_mods.cha

  def test_size(self):
    race = type(self).__race
    assert race.size == 'medium', race.size

  def test_speed(self):
    race = type(self).__race
    assert race.speed == 30, race.speed


if __name__=='__main__':
  unittest.main()
