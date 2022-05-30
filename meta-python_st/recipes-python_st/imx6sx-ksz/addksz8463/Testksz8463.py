import unittest
from ksz8463 import ksz

class Testksz8463(unittest.TestCase):
  def setUp(self):
    self.ksz = ksz()
  def test_spi(self):
      self.assertEqual(self.ksz.spitest(), 'X8443')
if __name__ == "__main__":
  unittest.main()