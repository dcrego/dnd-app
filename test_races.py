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


class TestLoadRaces(unittest.TestCase):

  __index = races.load_index()
  __all_races = races.load_all_races()

  def test_len(self):
    index = type(self).__index
    all_races = type(self).__all_races
    assert len(index) >= 4, len(index)
    assert len(all_races) >= 4, len(all_races)
    assert len(index) == len(all_races), {'index': len(index), 'all races': len(all_races)}

  def test_dwarf(self):
    index = type(self).__index
    all_races = type(self).__all_races
    assert 'dwarf' in index
    assert 'dwarf' in all_races
    assert index['dwarf'] == 'dwarf.yaml' , index['dwarf']
    assert repr(all_races['dwarf']) == "Race('dwarf')", repr(all_races['dwarf'])
    assert all_races['dwarf'].name == 'dwarf', all_races['dwarf'].name

  def test_elf(self):
    index = type(self).__index
    all_races = type(self).__all_races
    assert 'elf' in index
    assert 'elf' in all_races
    assert index['elf'] == 'elf.yaml' , index['elf']
    assert repr(all_races['elf']) == "Race('elf')", repr(all_races['elf'])
    assert all_races['elf'].name == 'elf', all_races['elf'].name

  def test_halfling(self):
    index = type(self).__index
    all_races = type(self).__all_races
    assert 'halfling' in index
    assert 'halfling' in all_races
    assert index['halfling'] == 'halfling.yaml' , index['halfling']
    assert repr(all_races['halfling']) == "Race('halfling')", repr(all_races['halfling'])
    assert all_races['halfling'].name == 'halfling', all_races['halfling'].name

  def test_human(self):
    index = type(self).__index
    all_races = type(self).__all_races
    assert 'human' in index
    assert 'human' in all_races
    assert index['human'] == 'human.yaml' , index['human']
    assert repr(all_races['human']) == "Race('human')", repr(all_races['human'])
    assert all_races['human'].name == 'human', all_races['human'].name


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
