from common import returnDataForDay, printLst
data = returnDataForDay(__file__)

startData = data[:8]
rearrangementProcedure = data[10:]
stackLst = [[]]

def arrangeStartDataInStacks(startData):
    def getNLists(n:int):
        lst = []
        for i in range(n):
            lst.append([])
        return lst
    
    def removeEmptyLstAndReverseRemaining(lst:list[list]):
        out = []
        for l in lst: 
            if l != []:
                l.reverse()
                out.append(l)
        return out
    
    stackLstTemp = getNLists(36)
    
    for str in startData:
        for charIndex in range(len(str)):
            char = str[charIndex]
            if char.isalpha():
                stackLstTemp[charIndex].append(str[charIndex])

    return removeEmptyLstAndReverseRemaining(stackLstTemp)

def fromStrToMove(str):
    lst = str.split(' ')
    return (int(lst[1]),int(lst[3])-1,int(lst[5])-1)

def addToStack(stack:list, crates:list):
    copy = stack.copy()
    for c in crates: 
        copy.append(c)
    return copy

def removeFromStack(stack, amount):
    crates = []
    for i in range(amount):
        crates.append(stack.pop())
    return stack, crates  

def moveCrates(ship, move):
    shipCopy = ship.copy()
    amount, fromStack, toStack = move
    stack = ship[fromStack].copy()

    ship[fromStack], crates = removeFromStack(stack, amount)
    ship[toStack] = addToStack(shipCopy[toStack], crates)

    return shipCopy

def printTop(ship):
    shipCopy = ship.copy()
    out = ""
    for stack in shipCopy:
        out = out + stack[-1:][0]
    print(out)

ship = arrangeStartDataInStacks(startData)

for str in rearrangementProcedure:
    move = fromStrToMove(str)
    moveCrates(ship,move)

printLst(ship)
print()
printTop(ship)