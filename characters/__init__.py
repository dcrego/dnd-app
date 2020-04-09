def get_characters() -> list:
  import yaml
  import pkg_resources
  with pkg_resources.resource_stream(__package__, 'characters.yaml') as characters_stream:
    characters_list = yaml.full_load(characters_stream)
  return characters_list
