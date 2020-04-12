def roll(rolls:int, dice:int):
  if rolls >= 1:
    for a in range(1, dice+1):
      if rolls == 1:
        yield [a]
      else:
        for b in roll(rolls-1, dice):
          yield [a, *b]
    return

def create_trim(target_len:int):
  def trim(values:list) -> list:
    if len(values)>target_len:
      values.sort()
      values = values[-target_len:]
      return values
  return trim


class Distribution(dict):

  def __init__(self):
    super().__init__()

  def __repr__(self):
    return f'Distribution( total={self.total()}, avg={self.average()}, {dict.__repr__(self)} )'

  def __getitem__(self, key):
    if key in self:
      return dict.__getitem__(self, key)
    return 0

  def __truediv__(self, roperand:float):
    result = Distribution()
    total = self.total()
    for key in self:
      result[key] = self[key]/total
    return result

  def total(self) -> float:
    return sum(self.values())

  def normalize(self):
    return self/self.total()

  def average(self) -> float:
    total = self.total()
    return sum(map(lambda key: key*self[key]/total, self.keys()))


def distribution(totals):
  d = Distribution()
  for total in totals:
    d[total]+=1
  return d

results = roll(3, 6) # 3d6
totals = map(sum, results)
dist = distribution(totals)
print('3d6', round(dist.average(), 2), sep='\t')

results = roll(4, 6) # 4d6
results = map(create_trim(3), results) # 4d6 discard 1
totals = map(sum, results)
dist = distribution(totals)
print('4d6 discard 1', round(dist.average(), 2), sep='\t')

results = roll(5, 6) # 5d6
results = map(create_trim(3), results) # 5d6 discard 2
totals = map(sum, results)
dist = distribution(totals)
print('5d6 discard 2', round(dist.average(), 2), sep='\t')

totals = (15, 14, 13, 12, 10, 8) # Elite array
dist = distribution(totals)
print('Elite array', round(dist.average(), 2), sep='\t')
