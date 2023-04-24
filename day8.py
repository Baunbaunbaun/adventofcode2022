from common import getData, printLst, removeNewLine
import numpy as np

#data = removeNewLine(getData(__file__))
data = removeNewLine(getData(__file__, 'test'))

# PART 1 ###################################################

w = len(data[0])
h = len(data)
print(w, ' X ', h)

def fromStrToIntArray(str):
    out = []
    for c in str:
        out.append(int(c))
    return out

def fromStrToNpData(data):
    npData = []
    for line in data:
        npData.append(fromStrToIntArray(line))
    return np.asarray(npData)

npData = fromStrToNpData(data)

def getVisibleTreesInLine(treeLine):
    visibleTrees = []
    visibleHeight = -1
    for t in treeLine:
        if t > visibleHeight:
            visibleHeight = t
            visibleTrees.append(1)
        else: 
            visibleTrees.append(0)
    return visibleTrees

def getVisibleTreesFromOneDirection(forrest):
    boolForrest = []
    for l in forrest: 
        boolForrest.append(getVisibleTreesInLine(l))
    return boolForrest

def getAllVisibleTreesInForrest(forrest):
    boolForrest4Directions = []
    for direction in range(4):
        boolForrest = getVisibleTreesFromOneDirection(np.rot90(forrest, direction+1))
        boolForrest4Directions.append(np.rot90(boolForrest, -1*direction+1))
    return np.asarray(boolForrest4Directions)


x = getAllVisibleTreesInForrest(npData)
bool0and1 = np.logical_and(x[0],x[1])
bool2and3 = np.logical_and(x[2],x[3])
boolAll = np.logical_and(bool0and1, bool2and3)
print(boolAll.sum())


# PART 2 ###################################################

