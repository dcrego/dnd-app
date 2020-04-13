def compare_equal(left, right) -> bool:
  return bool(left == right)

def assertion(f0:callable):
  def f(*args, **kwargs):
    assert f0(*args, **kwargs), f'{f0.__name__}(*{args}, **{kwargs}) failed'
  f.__name__ = f0.__name__
  return f

@assertion
def assert_compare(left, comparator:callable, right):
  return comparator(left, right)
