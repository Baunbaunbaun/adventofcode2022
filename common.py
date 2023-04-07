import os

def returnDataForDay(filePath:str):
    dir = os.path.join(os.path.dirname(__file__), 'data')
    fileNameWithType = filePath.split('/')[-1]
    fileName = fileNameWithType.split('.')[0]
    with open(f"{dir}/{fileName}.txt","r") as file:
        data = file.readlines()
        return data

def assertTuple(testTuple):
    shouldBe, this = testTuple
    assert shouldBe == this, f"wrong! Got: {this} not {shouldBe}"

def assertTuples(testData):
    for tup in testData:
        assertTuple(tup)