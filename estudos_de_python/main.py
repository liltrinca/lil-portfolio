from random import randrange
from random import randint

def randomizer(randomizeList: list) -> int:
    listRange = len(randomizeList)
    a = randrange(listRange)
    print(randomizeList[a])

def mergeSort(mergeSortList: list) -> list:
    rightList = []
    leftList = []
    half = len(mergeSortList) // 2
    end = len(mergeSortList)

    for i in mergeSortList[0:half]:
        leftList.append(i)
    for j in mergeSortList[half:end]:
        rightList.append(j)

    print(leftList)
    print(rightList)

def hexToRGB(hexCode: str) -> tuple:
    print("RGB =", tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4)))

def rgbToHex(rgbCode: tuple) -> str:
    hexstr = hex(rgbCode[0])[2:], hex(rgbCode[1])[2:], hex(rgbCode[2])[2:]
    print("#" + hexstr[0] + hexstr[1] + hexstr[2])

def randomizerTeams(names: list, teamMax: int) -> list:
    maxrdm = len(names)-1
    team1 = []

    while len(team1) != teamMax:
        rdmindex = randint(0, maxrdm)
        if (names[rdmindex] not in team1):
            team1.append(names[rdmindex])

    team2 = [i for i in names if i not in team1]
    print ("Team 1 %s" % team1, "Team 2 %s" % team2)

def isOddEven(number: int) -> bool:
    if (number % 2 == 0):
        return "Even"
    else:
        return "Odd"

def isOddEvenArray(vArray: list) -> tuple:
    resultList = []
    for i in range(len(vArray)):
        res = [vArray[i], isOddEven(vArray[i])]
        resultList.append(res)
    return tuple(resultList)

def randomAllocator(listLength = 10, intMin = 0, intMax = 100) -> list:
    odd = []
    even = []
    allocatedList = []
    i = 0

    while (i < listLength):
        try:
            currentInt = randint(intMin, intMax)
        except:
            return print('intMin must be lower than intMax')
        if (currentInt % 2 == 0):
            even.append(currentInt)
        else :
            odd.append(currentInt)
        i += 1

    even.sort()
    odd.sort()
    allocatedList.append(even)
    allocatedList.append(odd)

    return allocatedList