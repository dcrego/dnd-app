class Ability:

  name=None
  key=None

  def __init__(self, name:str):
    super().__init__()
    self.name = name.lower()
    self.key = name[:3].upper()

  def __repr__(self):
    return f'Ability({self})'

  def __str__(self):
    return self.key


class AbilityLoader:

  __instance=None
  abilities=[]

  def __new__(cls):
    if not cls.__instance:
      cls.__instance = object.__new__(cls)
      import pkg_resources, yaml
      with pkg_resources.resource_stream(__package__, 'abilities.yaml') as abilities_stream:
        data = yaml.load(abilities_stream, Loader=yaml.SafeLoader)
      for item in data:
        cls.__instance.abilities.append(Ability(item))
    return cls.__instance
