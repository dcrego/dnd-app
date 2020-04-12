from typing import Dict, Any
import pkg_resources, yaml


class Race:

  class AbilityMods:

    def __loadattr(self, name:str, data:Dict[str, int], default=0):
      setattr(self, name, data.get(name, default))

    def __init__(self, data:Dict[str, int]):
      super().__init__()
      self.__loadattr('str', data)
      self.__loadattr('dex', data)
      self.__loadattr('con', data)
      self.__loadattr('int', data)
      self.__loadattr('wis', data)
      self.__loadattr('cha', data)


  def __init__(self, data:Dict[str, Any]={}):
    super().__init__()
    setattr(self, 'name', data.get('name'))
    setattr(self, 'ability_mods', type(self).AbilityMods(data.get('ability score modifiers', {})))
    setattr(self, 'size', data.get('size', 'medium'))
    setattr(self, 'speed', data.get('speed', 30))

  def __repr__(self):
    return f'Race({repr(self.name)})'


def load_index() -> Dict[str, str]:
  with pkg_resources.resource_stream(__package__, 'index.yaml') as index_stream:
    return yaml.full_load(index_stream)

def load_all_races() -> Dict[str, Race]:
  index = load_index()
  races = dict()
  for key in index:
    races[key] = load_race(key)
  return races

def load_race(key:str, index:Dict[str, str]=None) -> Race:
  if not index:
    index = load_index()
  with pkg_resources.resource_stream(__package__, index[key]) as race_stream:
    race_data = yaml.full_load(race_stream)
  return Race(race_data)
