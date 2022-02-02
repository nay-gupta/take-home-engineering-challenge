import unittest

from CSVReader import TruckReader
from FoodTrucks import FoodTrucks

class TestFoodTrucks(unittest.TestCase):
  def setUp(self) -> None:
    super()
    self.foodTrucks = FoodTrucks(TruckReader('csv_test_data.csv'))

  def test_getTrucksByBlock(self):
    print("Testing getting trucks by the block")
    trucksByBlock = self.foodTrucks.getTrucksByBlock('3549')
    self.assertEqual(len(trucksByBlock), 2)
    print("Success")

  def test_getTrucksByLocation(self):
    print("Testing getting trucks by the location")
    trucksByBlock = self.foodTrucks.getTrucksByLocation('848185')
    self.assertEqual(len(trucksByBlock), 2)
    print("Success")

  def test_addTruck(self):
    failedText = "Need block id, location id, and Applicant"
    successText = "Successfully added truck"

    print("Adding invalid trucks (no block, no locationid, no Applicant")
    truckToAdd = {
      'locationid': '9999'
    }
    self.assertEqual(failedText, self.foodTrucks.addTruck(truckToAdd))
    truckToAdd = {
      'block': '9999'
    }
    self.assertEqual(failedText, self.foodTrucks.addTruck(truckToAdd))
    truckToAdd = {
      'Applicant': '9999'
    }
    self.assertEqual(failedText, self.foodTrucks.addTruck(truckToAdd))
    print("Success")

    print("Adding valid truck")
    truckToAdd = {
      'locationid': '9999',
      'block': '9999',
      'Applicant': "Nayan's Food Truck"
    }
    self.assertEqual(successText, self.foodTrucks.addTruck(truckToAdd))
    self.assertEqual(self.foodTrucks.count, 11)
    print("Success")

if __name__ == '__main__':
  unittest.main()