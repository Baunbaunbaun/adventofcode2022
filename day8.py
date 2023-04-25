from common import getData, printLst, removeNewLine
import numpy as np

data = removeNewLine(getData(__file__))
#data = removeNewLine(getData(__file__, 'test'))

# PART 1 ###################################################

w = len(data[0])
h = len(data)
print('Forrest size: ', w, ' X ', h)

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
    boolForrestAllDirections = []
    for direction in range(4):
        forrestRotated = np.rot90(forrest, direction)
        boolForrest = getVisibleTreesFromOneDirection(forrestRotated)
        boolForrestNormal = np.rot90(boolForrest, -1*direction)
        boolForrestAllDirections.append(boolForrestNormal)
    return np.asarray(boolForrestAllDirections)

def countVisibleTrees(forrest):
    visibleTreesInForrest = getAllVisibleTreesInForrest(forrest)

    bool0and1 = np.logical_or(visibleTreesInForrest[0],visibleTreesInForrest[1])
    bool2and3 = np.logical_or(visibleTreesInForrest[2],visibleTreesInForrest[3])
    boolAll = np.logical_or(bool0and1, bool2and3)

    return boolAll.sum()

print('Visible trees: ', countVisibleTrees(npData))

# PART 2 ###################################################

