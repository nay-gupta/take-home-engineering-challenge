import unittest
from CSVReader import TruckReader

class TestTruckReader(unittest.TestCase):

  def setUp(self) -> None:
    super()
    self.truckReader = TruckReader('csv_test_data.csv')

  def test_csvToTruckDicts(self):
    trucksByLine, idsByBlock, idsByLocation, line = self.truckReader.csvToTruckDicts()
    
    print("Testing all test trucks have been added")
    self.assertEqual(line, 10)
    self.assertEqual(trucksByLine[0]['locationid'], '751253')
    self.assertEqual(trucksByLine[9]['locationid'], '848185')
    print("Success")

    print("Testing the blocks map to the correct trucks")
    self.assertCountEqual(idsByBlock['3549'], [0, 9])
    print("Success")

    print("Testing the locations map to the correct trucks")
    self.assertCountEqual(idsByLocation['848185'], [8, 9])
    print("Success")


if __name__ == '__main__':
  unittest.main()