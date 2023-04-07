import os
dataRoot = os.path.join(os.path.dirname(__file__), 'data')

"""

from enum import Enum

class RockPaperScissors(Enum):
    A = 1
    B = 2
    C = 3

class XYZ(Enum):
    X = 1
    Y = 2
    Z = 3

class OutCome(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6

def scoreOfChoice(choice:chr) -> int:
    return XYZ[choice].value

def rockRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return OutCome.DRAW.value
    if other == RockPaperScissors.B.name:
        return OutCome.LOST.value
    else: 
        return OutCome.WIN.value
    
def scissorRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return OutCome.LOST.value
    if other == RockPaperScissors.B.name:
        return OutCome.WIN.value
    else: 
        return OutCome.DRAW.value
    
def paperRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return OutCome.WIN.value
    if other == RockPaperScissors.B.name:
        return OutCome.DRAW.value
    else: 
        return OutCome.LOST.value

def round(other:chr, me:chr) -> int:
    match me: 
        case 'X': return rockRound(other)+scoreOfChoice(me)
        case 'Y': return paperRound(other)+scoreOfChoice(me)
        case 'Z': return scissorRound(other)+scoreOfChoice(me)

with open("/Users/christianbaun/Projects/AdventOfCode/data/2a.txt","r") as file:
    data = file.readlines()
    result = 0
    for line in data:
        (other,me) = line.split()
        result = result + round(other, me)
    print(result)

def testTheCalculation(testTuple):
    shouldBe, this = testTuple
    assert shouldBe == this, f"wrong! Got: {this} not {shouldBe}"

testData1 = [(8, round('A','Y')),
            (1, round('B','X')),
            (6, round('C','Z')),
            (2, scoreOfChoice('Y')),
            (1, scoreOfChoice('X')),
            (3, scoreOfChoice('Z'))]

for tstTuple in testData1:
    testTheCalculation(tstTuple)


# assignment 2
# X means lose, 
# Y means draw, and 
# Z means win.

# A means rock
# B means paper
# C means scissors

# (X)
def loseRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return RockPaperScissors.C.value
    if other == RockPaperScissors.B.name:
        return RockPaperScissors.A.value
    else: 
        return RockPaperScissors.B.value

# (Y)
def drawRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return RockPaperScissors.A.value
    if other == RockPaperScissors.B.name:
        return RockPaperScissors.B.value
    else: 
        return RockPaperScissors.C.value

# (Z)
def winRound(other:chr) -> int:
    if other == RockPaperScissors.A.name:
        return RockPaperScissors.B.value
    if other == RockPaperScissors.B.name:
        return RockPaperScissors.C.value
    else: 
        return RockPaperScissors.A.value

class ABC(Enum):
    A = 1
    B = 2
    C = 3

class OutCome(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6

def scoreOfChoice(choice:chr) -> int:
    return XYZ[choice].value

 
def round2(other:chr, me:chr) -> int:
    match me: 
        case 'X': return OutCome.LOST.value + loseRound(other)
        case 'Y': return OutCome.DRAW.value + drawRound(other)
        case 'Z': return OutCome.WIN.value + winRound(other)


testData2 = [(4, round2('A','Y')),
            (1, round2('B','X')),
            (7, round2('C','Z')),

            (8, round2('A','Z')), # rock -> paper 2, win 6      = 8
            (5, round2('B','Y')), # paper 2, draw 3             = 5
            (2, round2('C','X'))] # scissors -> paper 2, lose 0 = 2

for tstTuple in testData2:
    print("Testing: " + str(tstTuple) )
    testTheCalculation(tstTuple)

"""

with open(f"{dataRoot}/2a.txt","r") as file:
    data = file.readlines()
    print(len(data.pop()))
    result = 0
    for line in data:
        #print(line)
        (other,me) = line.split()
        #result = result + round2(other, me)
    #print(result)