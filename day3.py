import os
dataRoot = os.path.join(os.path.dirname(__file__), 'data')

def recGetItemTypes(elvesLst):
    length = len(elvesLst)
    # 1 team left
    if (length == 3):
        return getItemType(findBadge(popTeam(elvesLst)))
    # equal amount of teams left
    if (length % 2 == 0):
        firstHalf, secondHalf = splitInTwoElvesLst(elvesLst, length)
        return recGetItemTypes(firstHalf) + recGetItemTypes(secondHalf)
    else:
        first, second, third = splitInThreeElvesLst(elvesLst, length)
        return recGetItemTypes(first) + recGetItemTypes(second) + recGetItemTypes(third)

def iterativeGetItemTypes(elvesLst):
    sum = 0
    while (len(elvesLst)>0):
        team, elvesLst = popTeam(elvesLst)
        sum += getItemType(findBadge(team))
    return sum

def popTeam(elvesLst):
    team = [elvesLst.pop()[:-1], elvesLst.pop()[:-1], elvesLst.pop()[:-1]]
    return team, elvesLst

def findUniqueItemType(inputTuple:tuple) -> chr:
    compartmentOne, compartmentTwo = inputTuple
    return (set(compartmentOne) & set(compartmentTwo)).pop()

def findBadge(inputTuple:tuple) -> chr:
    compartmentOne, compartmentTwo, compartmentThree = inputTuple
    print(compartmentOne)
    return (set(compartmentOne) & 
            set(compartmentTwo) & 
            set(compartmentThree)).pop()

def splitRucksack(rucksack:str) -> tuple:
    half = int(len(rucksack)/2)
    return (rucksack[:half],rucksack[half:])

def splitInTwoElvesLst(elvesLst, length):
    half = int(length/2)
    return (elvesLst[:half],elvesLst[half:])

def splitInThreeElvesLst(elvesLst, length):
    third = int(length/3)
    return elvesLst[:third], elvesLst[third:2*third], elvesLst[2*third:] 

def assertTuple(testTuple):
    shouldBe, this = testTuple
    assert shouldBe == this, f"wrong! Got: {this} not {shouldBe}"

def getItemType(char:chr) -> int:
    charInt = ord(char)
    if charInt > 96:
        return charInt-96
    else:
        return charInt-38

team = ('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg')

testData = [(1, getItemType('a')),
            (16, getItemType('p')),
            (27, getItemType('A')),
            (52, getItemType('Z')),
            (('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), splitRucksack('vJrwpWtwJgWrhcsFMMfFFhFp')),
            ('p', findUniqueItemType(splitRucksack('vJrwpWtwJgWrhcsFMMfFFhFp'))),
            ('r', findBadge(team))
            ]

#for tst in testData:
 #   assertTuple(tst)

# test recursion
with open(f"{dataRoot}/testLst2_70.txt","r") as file:
    data = file.readlines()
    #assertTuple((70, iterativeGetItemTypes(data)))

# test recursion
with open(f"{dataRoot}/testLst4_140.txt","r") as file:
    data = file.readlines()
    #assertTuple((140, iterativeGetItemTypes(data)))

# test recursion
with open(f"{dataRoot}/testLst3_88.txt","r") as file:
    data = file.readlines()
    #assertTuple((88, iterativeGetItemTypes(data)))

 
with open(f"{dataRoot}/input3.txt","r") as file:
    data = file.readlines()
    print(iterativeGetItemTypes(data))
