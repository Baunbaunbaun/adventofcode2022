import numpy as np
from common import returnDataForDay
from common import assertTuples

data = returnDataForDay(__file__)

def splitInTwoElves(string:str):
    return string[:-1].split(',')

def split2ElvesIn4Sections(elfTuple:str):
    elf1, elf2 = elfTuple
    return np.array(elf1.split('-'), dtype=np.uint16), np.array(elf2.split('-'), dtype=np.uint16)

def doSectionsOverlap(elfTuple) -> bool:
    elf1, elf2 = elfTuple
    row1 = elf1 > elf2
    row2 = elf1 < elf2
    return row1.all() != True and row2.all() != True

def countOverLaps(dataInput):
    count = 0
    for line in dataInput:  
        if doSectionsOverlap(split2ElvesIn4Sections(splitInTwoElves(line))):
            count += 1
    return count

print(countOverLaps(data))
    






###################################################

testData = [((7,8), '7-50,8-33')]

#assertTuples(testData)


