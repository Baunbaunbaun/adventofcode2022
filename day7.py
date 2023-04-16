from anytree import Node, RenderTree
from common import getData, assertTuples, printLst
# data = getData(__file__)
testData = getData(__file__, 'test')[1:]

#printLst(data)

dirStack = []
def getDirInStack(name:str):
    for d in dirStack:
        if d.name == name:
            return d

class dirObject:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size
        self.children = []
        dirStack.append(self)
        presentDir = self

    def getSize(self):
        print('getting size of ', len(self.children), ' children!')
        if self.children == []:
            print('no children')
            return self.size
        for c in self.children:
            self.size += c.getSize()
        return self.size

class dir(dirObject): 
    def __init__(self, name, parent):
        super().__init__(name, 0)
        self.parent = parent
        parent.children.append(self)
        dirStack.append(self)

class file(dirObject): 
    def __init__(self, name, size, parent):
        super().__init__(name, size)
        self.size = size
        self.parent = parent
        parent.children.append(self)

def cd(name:str):
    presentDir = getDirInStack(name)

def evalLine(str):
    token = str.split(' ')
    printLst(token)
    print()
    match token[0], token[1]: 
        case '$', 'cd':
            cd(name=token[2])
        case '$', 'ls':
            pass
        case 'dir', _:
            dir(name=token[1], parent=presentDir)
        case _, _:
            file(name=token[1], size=token[0], parent=presentDir)

presentDir = dirObject('root', 0)
print(getDirInStack('root').size)

for line in testData: 
    evalLine(line[:-1])

r = getDirInStack('root')

for c in r.children:
    print(c.name, c.getSize(), c.parent.name)