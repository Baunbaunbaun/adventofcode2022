from common import getData, printLst, removeNewLine
import numpy as np

#data = removeNewLine(getData(__file__))
data = removeNewLine(getData(__file__, 'test'))

# PART 1 ###################################################

w = len(data[0])
h = len(data)

print(w, ' X ', h)

#printLst(data)

def fromStrToIntArray(str):
    out = []
    for c in str:
        out.append(int(c))
    return out

def fromStrToIntNpArray(str):
    out = []
    for c in str:
        out.append(int(c))
    return np.asarray(out)

def staircaseArray(arr):
    indexArr = np.zeros(9)

    for i in range(9):
        indexArr[i] = arr.find(str(i))
    return indexArr

def getDifMatrix(data):
    out = []
    previousRow = np.zeros(w)

    for line in data:
        row = fromStrToIntNpArray(line) 
        print(previousRow)
        print(row)
        dif = row > previousRow
        print(dif)     
        out.append(dif)
        previousRow = row
        #print(out)     

    return out

def getSingleVisibleTreeIndex(treeLine):
    treeLine = fromStrToIntArray(treeLine)
    maxTreeHeight = max(treeLine)
    indexesOfMaxTrees = [i for (y, i) in zip(treeLine, range(len(treeLine))) if maxTreeHeight == y]

    if len(indexesOfMaxTrees) > 1:
        return -1
    return indexesOfMaxTrees[0]

def getVisibleTree(treeLine):
    treeIndex = getSingleVisibleTreeIndex(treeLine)
    treeLineBool = np.zeros(len(treeLine))
    if treeIndex < 0:
        return treeLineBool
    treeLineBool[treeIndex] = 1
    return treeLineBool

def get2dArrayWithVisibleTrees(forrest):
    array2dWithMaxTrees = []
    for treeLine in forrest:
        array2dWithMaxTrees.append(getVisibleTree(treeLine))
    return np.asarray(array2dWithMaxTrees)

def fromStrToNpData(data):
    npData = []
    for line in data:
        npData.append(fromStrToIntArray(line))
    return np.asarray(npData)

npData = fromStrToNpData(data)
#printLst(data)
rotData = np.rot90(npData)

def getNumberOfVisibleTrees(forrest):
    horizontalVisible = get2dArrayWithVisibleTrees(data)
    verticalVisible = np.rot90(get2dArrayWithVisibleTrees(rotData), k=1, axes=(1,0))
    return (np.logical_and(horizontalVisible, verticalVisible)).sum()


print(getNumberOfVisibleTrees(data))

# PART 2 ###################################################

