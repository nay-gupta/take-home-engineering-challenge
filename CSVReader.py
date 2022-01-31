import csv

class TruckReader:

  def __init__(self, filename) -> None:
    self.filename = filename


  def csvToTruckDicts(self) -> int:
    trucksByLine = {}
    idsByBlock = {}
    idsByLocation = {}

    with open(self.filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', )
      line = 0
      for row in reader:
        location = row[0]
        block = row[7]
        if line != 0:
          trucksByLine[line] = row
          if idsByBlock[block]:
            idsByBlock[block].append(line)
          else:
            idsByBlock[block] = [line]

          if idsByLocation[location]:
            idsByLocation[location].append(line)
          else:
           idsByLocation[location] = [line]

        line += 1

    return [trucksByLine, idsByBlock, idsByLocation, line]
    
