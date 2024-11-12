from simple import *
import unittest

class TestAdd(unittest.TestCase):
  def test_twothree(self):
    self.assertEqual(addition(2,3), 5)


if __name__ == '__main__':
  unittest.main()
