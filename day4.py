import numpy as np
from common import returnDataForDay
data = returnDataForDay(__file__)

def splitInTwoElves(string:str):
    return string[:-1].split(',')

def split2ElvesIn4Sections(elfTuple:str):
    elf1, elf2 = elfTuple
    return np.array(elf1.split('-'), dtype=np.uint16), np.array(elf2.split('-'), dtype=np.uint16)

def doSectionsTotallyOverlap(elfTuple) -> bool:
    elf1, elf2 = elfTuple
    row1 = elf1 > elf2
    row2 = elf1 < elf2
    return row1.all() != True and row2.all() != True

def countOverLaps(dataInput):
    count = 0
    for line in dataInput:  
        if doSectionsTotallyOverlap(split2ElvesIn4Sections(splitInTwoElves(line))):
            count += 1
    return count

print('In how many assignment pairs does one range fully contain the other? ', countOverLaps(data))
    
# PART 2 ###################################################

def doSectionsOverlap(elfTuple) -> bool:
    elf1, elf2 = elfTuple
    return not ((elf1[0] < elf2[0] and elf1[1] < elf2[0]) or 
                (elf1[0] > elf2[1] and elf1[1] > elf2[1]))
    
def countAllOverLaps(data):
    count = 0
    for line in data:  
        if doSectionsOverlap(split2ElvesIn4Sections(splitInTwoElves(line))):
            count += 1
    return count
 
print('In how many assignment pairs do the ranges overlap? ', countAllOverLaps(data))