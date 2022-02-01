from CSVReader import TruckReader

class FoodTrucks:

  def __init__(self, csvReader: TruckReader) -> None:
    self.trucksByLine, self.idsByBlock, self.idsByLocation, self.count = csvReader.csvToTruckDicts()
    self.count -= 1

  def getTrucksByBlock(self, block) -> list:
    if block in self.idsByBlock:
      truckIds = self.idsByBlock
      trucks = []
      for id in truckIds:
        trucks.append(self.trucksByLine[id])
      return trucks