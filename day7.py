from anytree import Node, RenderTree
from common import getData, assertTuples, printLst
data = getData(__file__)

#printLst(data)

fileStack = [('root', 0)]

class dirObject:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size
        self.children = []

    def getSize(self):
        if self.children == []:
            return self.size
        for c in self.children:
            self.size += c.getSize()
        return self.size

class dir(dirObject): 
    def __init__(self, name, parent):
        super().__init__(name, 0)
        self.parent = parent
        parent.children.append(self)

class file(dirObject): 
    def __init__(self, name, size, parent):
        super().__init__(name, size)
        self.size = size
        self.parent = parent
        parent.children.append(self)

root = dirObject('root', 0)
myFile0 = file('myFile', 10, root)
d1 = dir('d1', root)
myFile1 = file('myFile1', 10, d1)
myFile2 = file('myFile2', 10, d1)
print(d1.getSize())

d2 = dir('d2', root)
d3 = dir('d3', root)
myFile3 = file('myFile3', 10, d2)
myFile4 = file('myFile4', 10, d3)
print(root.getSize())
print(root.getSize())
for c in root.children:
    print(c.name, c.size)

"""
def cd(dir:dirFile, newDir):
    dir.children
    match newDir: 
        case '..':
            cd(dir, dir.parent)

def eval(dir, cmdStr, data):
    _, cmd, newDir = cmdStr.split(' ')
    match cmd: 
        case 'cd':
            cd(dir, newDir)
        case 'ls':
            ls(dir, lsOutput)

   """     
