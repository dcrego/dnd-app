# dnd-app

Companion Gnome app for D&D written in [Python 3][py]

- [Preset characters](#preset-characters)
  - [Preset character milestones](#preset-character-milestones)
- [Abilities](#abilities)
  - [Ability score generation methods](#ability-score-generation-methods)
  - [Preset characters ability scores](#preset-characters-ability-scores)
- [Links](#links)

## Preset characters

Planned one character for each basic class according to [SRD][srd]

\# | Class     | Gender | Race     | Roles
---|-----------|--------|----------|-------
1  | Barbarian | Male   | Half-Orc | melee, tank, skilled
2  | Bard      | Male   | Gnome    | arcane magic, divine magic, skilled
3  | Cleric    | Female | Human    | divine magic, tank
4  | Druid     | Female | Elf      | divine magic, skilled
5  | Fighter   | Male   | Dwarf    | tank, melee, perky
6  | Monk      | Female | Human    | melee, skilled
7  | Paladin   | Male   | Human    | tank, melee, divine magic
8  | Ranger    | Male   | Elf      | ranged, melee, skilled
9  | Rogue     | Male   | Halfling | melee, ranged, skilled
10 | Sorcerer  | Female | Half-Elf | arcane magic
11 | Wizard    | Female | Elf      | arcane magic, perky

### Preset character milestones

- First milestone:
  - Dwarf Fighter
  - Human Cleric
  - Halfling Rogue
  - Elf Wizard

## Abilities

- Strength (STR)
- Dexterity (DEX)
- Constitution (CON)
- Intelligence (INT)
- Wisdom (WIS)
- Charisma (CHA)

### Ability score generation methods

There are many methods to analyze:

- Standard character
  - 4d6 discard 1, reorder and assign
- Organic character
  - 4d6 discard 1, assign in place
- Average character
  - 3d6, reorder and assign
- Random average character
  - 3d6, assign in place
- Powerful character
  - 5d6 discard 2, reorder and assign
- Random powerful character
  - 5d6 discard 2, assign in place
- Low-powered campaign point buy
  - 15 points
- Challenging campaign point buy
  - 22 points
- Standard campaign point buy
  - 25 points
- Tougher campaign point buy
  - 28 points
- High-powered campaign point buy
  - 32 points
- Elite array
  - 15, 14, 13, 12, 10, 8

-| 3d6 | 4d6 discard 1 | 5d6 discard 2 | Elite array
-|-|-|-|-
min | 3 | 3 | 3 | 8
max | 18 | 18 | 18 | 15
avg | 10.5 | 12.24 | 13.43 | 12

### Preset characters ability scores

The elite array is the most reasonable choice for preset characters:

Character      | STR | DEX | CON | INT | WIS | CHA
---------------|-----|-----|-----|-----|-----|-----
Dwarf Fighter  | 14  | 10  | 15  | 13  | 12  |  8
Human Cleric   | 12  | 10  | 13  |  8  | 15  | 14
Halfling Rogue | 10  | 15  |  8  | 14  | 12  | 13
Elf Wizard     |  8  | 13  | 14  | 15  | 12  | 10

## Links

- [Gnome ToolKit][gtk]
  - [Gnome ToolKit 3 documentation][gtk3-doc]
- [Python 3][py]
- [d20 SRD][srd]

[gtk]: https://www.gtk.org/
[gtk3-doc]: https://developer.gnome.org/gtk3/stable/
[py]: https://www.python.org/
[srd]: https://www.d20srd.org/
