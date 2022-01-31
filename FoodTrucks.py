from CSVReader import TruckReader

class FoodTrucks:

  def __init__(self, csvReader: TruckReader) -> None:
    self.trucksByLine, self.idsByBlock, self.idsByLocation, self.count = csvReader.csvToTruckDicts()
    self.count -= 1
