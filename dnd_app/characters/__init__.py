
def get_characters() -> list:
  import yaml
  import pkg_resources
  with pkg_resources.resource_stream(__package__, 'preset-characters.yaml') as characters_stream:
    characters_list = yaml.full_load(characters_stream)
  return characters_list


class Character:

  def __init__(self, data:dict):
    super().__init__()
    self.alias = data['alias']
    self.description = data['description']
