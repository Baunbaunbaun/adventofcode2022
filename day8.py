from common import getData, printLst, removeNewLine
import numpy as np

data = removeNewLine(getData(__file__))
# data = removeNewLine(getData(__file__, 'test'))

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

#print('Visible trees: ', countVisibleTrees(forrest=npData))

# PART 2 ###################################################

def getScenicScoreForTreesInLine(treeLine):
    treeScores = []
    for i in range(len(treeLine)):
        tree = treeLine[i]
        treeScores.append(getScenicScoreForOneTree(tree=tree, index=i, treeLine=treeLine))
    return treeScores

def getScenicScoreForOneTree(tree:int, index:int, treeLine:list):
    lookLeft = list(treeLine[:index])
    lookLeft.reverse()
    lookRight = list(treeLine[index+1:])
    leftScore = getScenicScoreOneDirection(tree, lookLeft)
    rightScore = getScenicScoreOneDirection(tree, lookRight)
    return leftScore * rightScore

def getScenicScoreOneDirection(tree:int, treeLineSegment:list):
    visibleTreesSum = 0
    for t in treeLineSegment:
        if int(t) >= int(tree): 
            visibleTreesSum = visibleTreesSum + 1
            break   
        visibleTreesSum = visibleTreesSum + 1
    return visibleTreesSum

def getScenicScore(row, column, forrest):
    tree = int(forrest[row][column])  
    def getVerticalScore(tree, row, column, forrest):
        rotatedForrest = np.rot90(np.asarray(forrest), 1)
        flippedAndRotatedForrest = rotatedForrest[::-1]
        # now rows and columns are switched!
        verticalTreeLine = flippedAndRotatedForrest[column]
        return getScenicScoreForOneTree(tree, row, verticalTreeLine)
    
    horizontalScore = getScenicScoreForOneTree(tree, column, forrest[row])    
    return horizontalScore * getVerticalScore(tree, row, column, forrest)

def getAllScenicScores(forrest):
    w = len(forrest[0])
    h = len(forrest)

    scenicScores = []

    for row in range(h):
        for column in range(w):
            score = getScenicScore(row, column, forrest)
            scenicScores.append(score)
    return scenicScores

printLst(npData)
print()
visibleTreeValues = getAllScenicScores(npData)
print()
print(np.max(getAllScenicScores(npData)))

# TESTING ###################################################

visibleTreesStr = ''
for i in range(len(visibleTreeValues)):
    if (i % w == 0):
        visibleTreesStr = visibleTreesStr + '\n'
    visibleTreesStr = visibleTreesStr + str(visibleTreeValues[i])

#print(visibleTreesStr)