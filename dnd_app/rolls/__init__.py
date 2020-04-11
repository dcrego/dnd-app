from typing import Generator, Tuple, Union

class Roll:

  def __len__(self) -> int:
    raise NotImplementedError(f'{type(self)}.__len__')

  def __radd__(self, loperand:Union[int]):
    if (loperand == 0):
       return SumRoll(self)
    raise NotImplementedError(f'{type(self)}.__radd__')

  def __rmul__(self, loperand:int):
    return MultiRoll(self, loperand)

  def __iter__(self) -> int:
    raise NotImplementedError(f'{type(self)}.__iter__')

  def roll(self) -> Generator[int, None, None]:
    '''Returns a genarator that iterates over the results of each internal roll.'''
    raise NotImplementedError(f'{type(self)}.roll')

  def sort(self):
    '''Returns a Roll that will yield the same results as self but sorted'''
    return SortedRoll(self)

  def limit(self, limit:int):
    '''Limit the amount of results.
If limit >= 0, the new amount will be equal to the limit.
If limit < 0, the new amount will be realtive to the original (original amount - abs(limit)).'''
    return LimitedRoll(self, limit)

  def reroll(self, until:callable):
    '''Reroll until condition is fulfilled'''
    return ReRoll(self, until)


class Die(Roll):

  def __init__(self, sides:int):
    super().__init__()
    self.sides=sides

  def __repr__(self) -> str:
    return f'Die(d{self.sides})'

  def __len__(self) -> int:
    return 1

  def roll(self) -> Generator[int, None, None]:
    from random import randint
    yield randint(1, self.sides)


class CustomRoll(Roll):

  def __init__(self, subroll:Roll):
    super().__init__()
    self.subroll = subroll

  def __iter__(self):
    return iter((self,))


class MultiRoll(CustomRoll):

  def __init__(self, subroll:Roll, times:int):
    super().__init__(subroll)
    self.times = times

  def __repr__(self):
    return f'MultiRoll( ({self.times})*({self.subroll}) )'
 
  def __len__(self) -> int:
    return self.times * len(self.subroll)

  def roll(self) -> Generator[int, None, None]:
    for i in range(self.times):
      for res in self.subroll.roll():
        yield res


class SortedRoll(CustomRoll):

  def __init__(self, subroll:Roll):
    super().__init__(subroll)

  def __repr__(self):
    return f'SortedRoll( {self.subroll} )'

  def roll(self) -> Generator[int, None, None]:
    rolls = list(self.subroll.roll())
    rolls.sort()
    for roll in rolls:
      yield roll

  def __len__(self) -> int:
    return len(self.subroll)


class LimitedRoll(CustomRoll):

  def __init__(self, subroll:Roll, limit:int):
      super().__init__(subroll)
      self.limit = limit

  def __repr__(self):
    return f'LimitedRoll( ({self.subroll}), limit={self.limit} )'

  def __len__(self):
    limit = self.limit
    if (limit<0):
      limit = len(self.subroll)+limit
    return limit

  def roll(self) -> Generator[int, None, None]:
      result = self.subroll.roll()
      for i in range(len(self)):
        yield next(result)


class SumRoll(CustomRoll):

  def __init__(self, subroll:Roll):
    super().__init__(subroll)

  def __repr__(self):
    return f'SumRoll( {self.subroll} )'

  def __len__(self) -> int:
    return 1

  def roll(self) -> Generator[int, None, None]:
    yield sum(self.subroll.roll())


class ReRoll(CustomRoll):

  def __init__(self, subroll, until:callable):
    super().__init__(subroll)
    self.until = until

  def __repr__(self):
    return f'ReRoll( ({self.subroll}), until={self.until} )'

  def __len__(self) -> int:
    return len(self.subroll)

  def roll(self) -> Generator[int, None, None]:
    while True:
      results = tuple(self.subroll.roll())
      if all(map(self.until, results)):
        break
    for result in results:
      yield result


class MinRollModifier():

  def __init__(self, times:int=1):
    super().__init__()
    self.times = times

  def __rmul__(self, loperand):
    return MinRollModifier(loperand * self.times)

  def __rsub__(self, loperand:Roll) -> Roll:
    if (self.times == 0):
      return loperand
    # TODO: if (self.times < 0)
    return loperand.sort().limit(-self.times)

  def __repr__(self):
    return f'{self.times}min'


STD_SIDES=(4, 6, 8, 10, 12, 20, 100)

for sides in STD_SIDES:
  vars()[f'D{sides}'] = Die(sides)
