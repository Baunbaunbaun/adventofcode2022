from common import getData, assertTuples
data = getData(__file__)[0]

def isDifferentChars(str:str):
    return len(set(str)) == len(str)

def scanStream(stream, windowSize):
    for i in range(len(stream)):
        end = i+windowSize
        window = stream[i:end]
        if (isDifferentChars(window)):  
            print(window, end)
            return end

testData = [(5, scanStream('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)),
            (6, scanStream('nppdvjthqldpwncqszvftbrmjlhg', 4)), 
            (10, scanStream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)),
            (11, scanStream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4))]

assertTuples(testData)

scanStream(data, 4)

# PART 2 ###################################################

scanStream(data, 14)
