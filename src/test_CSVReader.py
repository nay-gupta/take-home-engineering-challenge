import unittest
from CSVReader import TruckReader

class TestTruckReader(unittest.TestCase):

  def setUp(self) -> None:
    super()
    self.truckReader = TruckReader('csv_test_data.csv')

  def test_csvToTruckDicts(self):
    trucksByLine, idsByBlock, idsByLocation, line = self.truckReader.csvToTruckDicts()
    self.assertEqual(line, 10)
    self.assertEqual(trucksByLine[0]['locationid'], '751253')
    self.assertEqual(trucksByLine[9]['locationid'], '848185')

    self.assertCountEqual(idsByBlock['3549'], [0, 9])


if __name__ == '__main__':
  unittest.main()