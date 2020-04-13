import unittest
from assertions import *

class TestAssertCompare(unittest.TestCase):

  def test_assert_compare_equals(self):
    assert_compare(None, compare_equal, None)
    try:
      assert_compare(None, compare_equal, 0)
      assert False
    except AssertionError as err:
      pass

if __name__ == "__main__":
    unittest.main()
