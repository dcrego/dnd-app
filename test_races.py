import unittest
from dnd_app.races import *
from assertions import *


class TestDefaultRace(unittest.TestCase):

  __race = Race()

  def test_name(self):
    race = type(self).__race
    assert_compare(repr(race) , compare_equal, 'Race(None)')
    assert_compare(race.name , compare_equal, None)

  def test_ability_mods_str(self):
    race = type(self).__race
    assert_compare(race.ability_mods.str , compare_equal, 0)

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert_compare(race.ability_mods.dex , compare_equal, 0)

  def test_ability_mods_con(self):
    race = type(self).__race
    assert_compare(race.ability_mods.con , compare_equal, 0)

  def test_ability_mods_int(self):
    race = type(self).__race
    assert_compare(race.ability_mods.int , compare_equal, 0)

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert_compare(race.ability_mods.wis , compare_equal, 0)

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert_compare(race.ability_mods.cha , compare_equal, 0)

  def test_size(self):
    race = type(self).__race
    assert_compare(race.size , compare_equal, 'medium')

  def test_speed(self):
    race = type(self).__race
    assert_compare(race.speed , compare_equal, 30)


class TestRaceLoader(unittest.TestCase):

  __loader = RaceLoader()

  def test_race_loader_singleton(self):
    loader1 = RaceLoader()
    index1 = loader1._RaceLoader__index
    loader2 = RaceLoader()
    index2 = loader2._RaceLoader__index
    assert_compare(id(loader1) , compare_equal, id(loader2))
    assert_compare(id(index1) , compare_equal, id(index2))

  def test_keys_len(self):
    loader = type(self).__loader
    assert_compare(len(loader.keys()), int.__ge__, len(loader.keys()))

  def test_load_dwarf(self):
    loader = type(self).__loader
    assert_compare('dwarf', lambda l,r: l in r, loader.keys())
    race = loader.load('dwarf')
    assert_compare(repr(race) , compare_equal, "Race('dwarf')")
    assert_compare(race.name , compare_equal, 'dwarf')
    assert_compare(str(race) , compare_equal, 'dwarf')

  def test_load_elf(self):
    loader = type(self).__loader
    assert_compare('elf', lambda l,r: l in r, loader.keys())
    race = loader.load('elf')
    assert_compare(repr(race) , compare_equal, "Race('elf')")
    assert_compare(race.name , compare_equal, 'elf')
    assert_compare(str(race) , compare_equal, 'elf')

  def test_load_halfling(self):
    loader = type(self).__loader
    assert_compare('halfling', lambda l,r: l in r, loader.keys())
    race = loader.load('halfling')
    assert_compare(repr(race) , compare_equal, "Race('halfling')")
    assert_compare(race.name , compare_equal, 'halfling')
    assert_compare(str(race) , compare_equal, 'halfling')

  def test_load_human(self):
    loader = type(self).__loader
    assert_compare('human', lambda l,r: l in r, loader.keys())
    race = loader.load('human')
    assert_compare(repr(race) , compare_equal, "Race('human')")
    assert_compare(race.name , compare_equal, 'human')
    assert_compare(str(race) , compare_equal, 'human')


class TestDwarfRace(unittest.TestCase):

  __race = load_race('dwarf')

  def test_name(self):
    race = type(self).__race
    assert_compare(repr(type(self).__race) , compare_equal, "Race('dwarf')")
    assert_compare(race.name , compare_equal, 'dwarf')
    assert_compare(str(race) , compare_equal, 'dwarf')

  def test_ability_mods_str(self):
    race = type(self).__race
    assert_compare(race.ability_mods.str , compare_equal, 0)

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert_compare(race.ability_mods.dex , compare_equal, 0)

  def test_ability_mods_con(self):
    race = type(self).__race
    assert_compare(race.ability_mods.con , compare_equal, 2)

  def test_ability_mods_int(self):
    race = type(self).__race
    assert_compare(race.ability_mods.int , compare_equal, 0)

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert_compare(race.ability_mods.wis , compare_equal, 0)

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert_compare(race.ability_mods.cha , compare_equal, -2)

  def test_size(self):
    race = type(self).__race
    assert_compare(race.size , compare_equal, 'medium')

  def test_speed(self):
    race = type(self).__race
    assert_compare(race.speed , compare_equal, 20)


class TestElffRace(unittest.TestCase):

  __race = load_race('elf')

  def test_name(self):
    race = type(self).__race
    assert_compare(repr(type(self).__race) , compare_equal, "Race('elf')")
    assert_compare(race.name , compare_equal, 'elf')
    assert_compare(str(race) , compare_equal, 'elf')

  def test_ability_mods_str(self):
    race = type(self).__race
    assert_compare(race.ability_mods.str , compare_equal, 0)

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert_compare(race.ability_mods.dex , compare_equal, 2)

  def test_ability_mods_con(self):
    race = type(self).__race
    assert_compare(race.ability_mods.con , compare_equal, -2)

  def test_ability_mods_int(self):
    race = type(self).__race
    assert_compare(race.ability_mods.int , compare_equal, 0)

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert_compare(race.ability_mods.wis , compare_equal, 0)

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert_compare(race.ability_mods.cha , compare_equal, 0)

  def test_size(self):
    race = type(self).__race
    assert_compare(race.size , compare_equal, 'medium')

  def test_speed(self):
    race = type(self).__race
    assert_compare(race.speed , compare_equal, 30)


class TestHalflingfRace(unittest.TestCase):

  __race = load_race('halfling')

  def test_name(self):
    race = type(self).__race
    assert_compare(repr(type(self).__race) , compare_equal, "Race('halfling')")
    assert_compare(race.name , compare_equal, 'halfling')
    assert_compare(str(race) , compare_equal, 'halfling')

  def test_ability_mods_str(self):
    race = type(self).__race
    assert_compare(race.ability_mods.str , compare_equal, -2)

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert_compare(race.ability_mods.dex , compare_equal, 2)

  def test_ability_mods_con(self):
    race = type(self).__race
    assert_compare(race.ability_mods.con , compare_equal, 0)

  def test_ability_mods_int(self):
    race = type(self).__race
    assert_compare(race.ability_mods.int , compare_equal, 0)

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert_compare(race.ability_mods.wis , compare_equal, 0)

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert_compare(race.ability_mods.cha , compare_equal, 0)

  def test_size(self):
    race = type(self).__race
    assert_compare(race.size , compare_equal, 'small')

  def test_speed(self):
    race = type(self).__race
    assert_compare(race.speed , compare_equal, 20)


class TestHumanRace(unittest.TestCase):

  __race = load_race('human')

  def test_name(self):
    race = type(self).__race
    assert_compare(repr(type(self).__race) , compare_equal, "Race('human')")
    assert_compare(race.name , compare_equal, 'human')
    assert_compare(str(race) , compare_equal, 'human')

  def test_ability_mods_str(self):
    race = type(self).__race
    assert_compare(race.ability_mods.str , compare_equal, 0)

  def test_ability_mods_dex(self):
    race = type(self).__race
    assert_compare(race.ability_mods.dex , compare_equal, 0)

  def test_ability_mods_con(self):
    race = type(self).__race
    assert_compare(race.ability_mods.con , compare_equal, 0)

  def test_ability_mods_int(self):
    race = type(self).__race
    assert_compare(race.ability_mods.int , compare_equal, 0)

  def test_ability_mods_wis(self):
    race = type(self).__race
    assert_compare(race.ability_mods.wis , compare_equal, 0)

  def test_ability_mods_cha(self):
    race = type(self).__race
    assert_compare(race.ability_mods.cha , compare_equal, 0)

  def test_size(self):
    race = type(self).__race
    assert_compare(race.size , compare_equal, 'medium')

  def test_speed(self):
    race = type(self).__race
    assert_compare(race.speed , compare_equal, 30)


if __name__=='__main__':
  unittest.main()
