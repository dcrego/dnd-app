from typing import Dict, Any


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

  def __str__(self):
    return self.name


class RaceLoader:

  __instance = None

  def __new__(cls):
    if not cls.__instance:
      cls.__instance = object.__new__(cls)
      import pkg_resources, yaml
      with pkg_resources.resource_stream(__package__, 'index.yaml') as index_stream:
        cls.__instance.__index = yaml.load(index_stream, Loader=yaml.SafeLoader)
      cls.__instance.keys = cls.__instance.__index.keys
    return cls.__instance

  def load(self, key:str) -> Race:
    import pkg_resources, yaml
    with pkg_resources.resource_stream(__package__, self.__index[key]) as race_stream:
      race_data = yaml.load(race_stream, Loader=yaml.SafeLoader)
    return Race(race_data)


def load_race(key:str) -> Race:
  return RaceLoader().load(key)

def load_all_races() -> Dict[str, Race]:
  loader = RaceLoader()
  races = {}
  for key in loader.keys():
    races[key] = loader.load(key)
  return races
