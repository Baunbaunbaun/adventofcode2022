

def top3lst(lst:list[int], no) -> list[int]:
    lst.sort()
    lst.reverse()
    a = lst.pop()
    b = lst.pop()
    c = lst.pop()

    if no > c: 
        if no > b: 
            if no > a: 
                a = no
            else: 
                b = no
        else: 
            c = no

    return [c,b,a]

with open("/Users/christianbaun/Projects/AdventOfCode/data/input1a.txt","r") as file:
    data = file.readlines()
    cal = 0
    elvNo = 0
    maxLst = [0,0,0]
    calLst = []
    for line in data:
        if len(line) > 1:
            cal = cal + int(line)
        else: 
            calLst.append(cal)
            maxLst = top3lst(maxLst, cal)
            elvNo = elvNo + 1
            cal = 0
    
    print(maxLst.pop()+maxLst.pop()+maxLst.pop())
    calLst.sort()
    calLst.reverse()
    print(calLst[0]+calLst[1]+calLst[2])
    