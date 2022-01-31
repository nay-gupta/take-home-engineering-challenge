import csv
""" 
This class reads in a CSV file containing data about
San Fransisco's food trucks
"""
class TruckReader:

  def __init__(self, filename) -> None:
    self.filename = filename

  """
  This function indexes the trucks by three categories.
    1. The number of trucks inserted
    2. By Block number
    3. By LocationID

  The actual truck data is only contained in the first Dictionary.
  The other two Dictionaries only point to the identifiers of the first Dictionary.
  This way, we aren't duplicating all Truck data 3x.

  This makes getting trucks from the REST API O(1).
  This also makes adding new trucks via the REST API O(1)
  """
  def csvToTruckDicts(self) -> int:
    trucksByLine = {} # 1. The number of trucks inserted
    idsByBlock = {} # 2. By Block number
    idsByLocation = {} # 3. By LocationID

    line = 0

    with open(self.filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', )
      for row in reader:

        # Based on headers
        location = row[0]
        block = row[7]

        # First row contains only the headers
        if line != 0: 

          # 1. The number of trucks inserted
          trucksByLine[line] = row 

          # 2. By Block number
          # One block can have multiple food trucks
          if block in idsByBlock:
            idsByBlock[block].append(line)
          else:
            idsByBlock[block] = [line]

          # 3. By LocationID
          # One Location can have multiple food trucks
          if location in idsByLocation:
            idsByLocation[location].append(line)
          else:
           idsByLocation[location] = [line]

        line += 1

    line -= 1
    # Also return the line number to get the count of trucks
    return [trucksByLine, idsByBlock, idsByLocation, line]
    
