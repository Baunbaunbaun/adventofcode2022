from common import returnDataForDay, printLst, assertTuples
data = returnDataForDay(__file__)

def isDifferentChars(str:str):
    return len(set(str)) == len(str)

def scanStream(stream):
    for i in range(len(stream)):
        end = i+4
        window = stream[i:end]
        if (isDifferentChars(window)):  
            print(window, end)
            return end

testData = [(5, scanStream('bvwbjplbgvbhsrlpgdmjqwftvncz')),
            (6, scanStream('nppdvjthqldpwncqszvftbrmjlhg')), 
            (10, scanStream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')),
            (11, scanStream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))]

assertTuples(testData)

scanStream(data[0])