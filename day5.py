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

stackLst = arrangeStartDataInStacks(startData)

printLst(stackLst)