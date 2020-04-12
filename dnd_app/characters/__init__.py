from typing import Iterable
import pkg_resources, yaml


class Character:

  def __init__(self, file:str):
    super().__init__()
    character_data = dict()
    with pkg_resources.resource_stream(__package__, file) as character_stream:
      character_data = yaml.full_load(character_stream)
    self.name = character_data['name']
    self.gender = character_data['description']['gender']
    from ..races import load_race
    self.race = load_race(character_data['description']['race'])
    self.class0 = character_data['class']
    self.ability_scores = character_data['ability scores']

  def description(self):
    return f'{self.gender} {self.race}'


def get_characters() -> Iterable[Character]:
  with pkg_resources.resource_stream(__package__, 'preset-characters.yaml') as characters_stream:
    character_files = yaml.full_load(characters_stream)
  for character_file in character_files:
    yield Character(character_file)
