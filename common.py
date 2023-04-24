import os

def getData(filePath:str, test:str = ''):
    dir = os.path.join(os.path.dirname(__file__), 'data')
    fileNameWithType = filePath.split('/')[-1]
    fileName = fileNameWithType.split('.')[0]
    with open(f"{dir}{test}/{fileName}.txt","r") as file:
        data = file.readlines()
        return data

def assertTuple(testTuple):
    shouldBe, this = testTuple
    assert shouldBe == this, f"wrong! Got: {this} not {shouldBe}"

def assertTuples(testData):
    for tup in testData:
        assertTuple(tup)

def printLst(lst):
    for l in lst: 
        print(l)

def mapCounter(array, func):
    count = 0
    for line in array:  
        if func(line):
            count += 1
    return count

def removeNewLine(data:list):
    newData = data.copy()
    for index in range(len(data)):
        for c in newData[index]:
            if ord(c) == 10:
                newData[index] = newData[index][:-1]
    return newData



