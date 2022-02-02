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
      truckIds = self.idsByBlock[block]
      trucks = []
      for id in truckIds:
        trucks.append(self.trucksByLine[id])
      return trucks
    return []
  
  """ 
  Retrieves a list of trucks based on the LocationID
  """
  def getTrucksByLocation(self, location) -> list:
    if location in self.idsByLocation:
      truckIds = self.idsByLocation[location]
      trucks = []
      for id in truckIds:
        trucks.append(self.trucksByLine[id])
      return trucks
    return []

  """
  Adds a new truck to the in memory states. Validation checks for block, locationid, and Applicant
  are included.
  """
  def addTruck(self, truck) -> str:
    
    # Invalid Truck
    if 'block' not in truck or 'locationid' not in truck or 'Applicant' not in truck:
      return "Truck not added. Need block id, location id, and Applicant", False

    # Valid Truck
    else:
      # 1. The number of trucks inserted
      self.trucksByLine[self.count] = truck

      # 2. By Block number
      if truck['block'] in self.idsByBlock:
        self.idsByBlock[truck['block']].append(self.count)
      else:
        self.idsByBlock[truck['block']] = [self.count]

      # 3. By LocationID
      if truck['locationid'] in self.idsByLocation:
        self.idsByLocation[truck['locationid']].append(self.count)
      else:
        self.idsByLocation[truck['locationid']] = [self.count]

      # Increase total number of trucks
      self.count += 1
      return "Successfully added truck", True