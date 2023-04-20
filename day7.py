from common import getData

data = getData(__file__)[1:]
testData = getData(__file__, 'test')[1:]
dirStack = []

def getDirInStack(name:str, parentName:str=''):
    if name == 'root':
        return dirStack[0]

    for d in dirStack:
        if d.name == name and d.parent.name == parentName:
            return d

class dirObject:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size
        self.parentName = '' 
        self.children = []
        dirStack.append(self)

    def getSize(self):
        if self.children == []:
            return self.size
        self.size = 0
        for c in self.children:
            self.size += int(c.getSize())
        return self.size

presentDir = dirObject('root', 0)

class dir(dirObject): 
    
    def __init__(self, name, parent):
        super().__init__(name, 0)
        self.parent = self.setParent(parent)
        self.parent.children.append(self)
        self.isDir = True
    
    def setParent(self, parent:dirObject):
        self.parentName = parent.name
        self.parent = parent
        return parent

class file(dirObject): 
    def __init__(self, name, size, parent):
        super().__init__(name, size)
        self.size = size
        self.parent = parent
        self.parent.children.append(self)
        self.isDir = False

def cd(name:str, parent:dirObject):
    match name: 
        case '..':
            globals()['presentDir'] = parent.parent
        case '/':
            globals()['presentDir'] = getDirInStack('root', '')
        case _:
            globals()['presentDir'] = getDirInStack(name, parent.name)

def evalLine(str):
    token = str.split(' ')
    presentDir = globals()['presentDir']
    match token[0], token[1]: 
        case '$', 'cd':
            #print('CD: ', token[2])
            cd(name=token[2], parent=presentDir)
        case '$', 'ls':
            #print('LS: pass')
            pass
        case 'dir', _:
            #print('DIR: ', token[1], globals()['presentDir'].name)
            dir(name=token[1], parent=presentDir)
        case _, _:
            #print('FILE: ', token[1], token[0], globals()['presentDir'].name)
            file(name=token[1], size=token[0], parent=presentDir)


for line in data: 
    evalLine(line[:-1])

r = getDirInStack('root')

print('root size = ',getDirInStack('root').getSize())
print('root children = ', len(getDirInStack('root').children))

count = 0
sum = 0
for d in dirStack[1:]:
    if (int(d.size) <= 100000 and 
        d.isDir):
        count += 1
        sum += d.getSize()
        print(d.name, d.getSize(), d.parent.name, len(d.children))  

print('Items max 100K = ', count)
print('SUM = ', sum)