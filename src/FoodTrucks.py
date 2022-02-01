from CSVReader import TruckReader

""" 
This class handles the backend getting and adding of trucks
from/to the in-memory data structures
"""
class FoodTrucks:

  def __init__(self, csvReader: TruckReader) -> None:
    # Get initial trucks from the csv
    self.trucksByLine, self.idsByBlock, self.idsByLocation, self.count = csvReader.csvToTruckDicts()

  """ 
  Retrieves a list of trucks based on the Block
  """
  def getTrucksByBlock(self, block) -> list:
    if block in self.idsByBlock:
      truckIds = self.idsByBlock
      trucks = []
      for id in truckIds:
        trucks.append(self.trucksByLine[id])
      return trucks
  
  """ 
  Retrieves a list of trucks based on the LocationID
  """
  def getTrucksByLocation(self, location) -> list:
    if location in self.idsByLocation:
      truckIds = self.idsByLocation
      trucks = []
      for id in truckIds:
        trucks.append(self.trucksByLine[id])
      return trucks