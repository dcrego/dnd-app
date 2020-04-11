import rolls

if __name__ == '__main__':

  def test_roll(roll:rolls.Roll):
    print(f'test repr(roll:{type(roll)}):', repr(roll), sep='\t')
    print(f'test len({roll}):', len(roll), sep='\t')
    print(f'test ({roll}).roll() 5 times:', tuple(tuple(roll.roll()) for _ in range(5)), sep='\t')

  for sides in rolls.STD_SIDES:
    roll = eval(f'rolls.D{sides}')
    test_roll(roll)
    print(f'test ({roll}).sides:', roll.sides, sep='\t')

  from rolls import D6
  roll = 5*D6
  test_roll(roll)
  roll = roll - 2*rolls.MinRollModifier()
  test_roll(roll)
  roll = sum(roll)
  test_roll(roll)
  roll = roll.reroll(lambda result: result>=8)
  test_roll(roll)
  roll = 6*roll
  test_roll(roll)

  while(roll):
    print(f'\t{roll}\t{type(roll)}')
    try:
      roll = roll.subroll
    except AttributeError:
      roll = None

  # TODO: test default implementations in superclasses
