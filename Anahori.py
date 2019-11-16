import copy
import random

def PrintRoute(route):
    dictionary = {'S':'S', 'G':'G', '0':'□', '1':'■', '2':'+'}
    for road in route:
        content = ''
        for element in road:
            content += dictionary[element]
        print(content)
    return

def PrintRouteCode(route):
    dictionary = {'S':'S', 'G':'G', '0':'0', '1':'1'}
    for road in route:
        content = ''
        for element in range(0, len(road)):
            if element == len(road) - 1:
                content += dictionary[road[element]]
            else:
                content += dictionary[road[element]] + " "
        print(content)
    return

def CreateRoute(startPosition, x, y):
    route = []
    for j in range(0, y):
        row = []
        for k in range(0, x):
            row.append('1')
        route.append(row)
    route[startPosition[0]][startPosition[1]] = '0'
    return route

def allFalse(available):
    for element in available:
        if element:
            return False
    return True

def makeDirection(route, position):
    available = [True, True, True, True] # up, down, right, left
    if position[0] + 2 > len(route)-1:
        available[1] = False
    if position[0] - 2 < 0:
        available[0] = False
    if position[1] + 2 > len(route[0])-1:
        available[2] = False
    if position[1] - 2 < 0:
        available[3] = False

    if available[0]:
        if not route[position[0] - 2][position[1]] == '1':
            available[0] = False
    if available[1]:
        if not route[position[0] + 2][position[1]] == '1':
            available[1] = False
    if available[2]:
        if not route[position[0]][position[1] + 2] == '1':
            available[2] = False
    if available[3]:
        if not route[position[0]][position[1] - 2] == '1':
            available[3] = False

    # すべて行き止まりだったら
    if allFalse(available):
        # print(" -- Route -- ")
        # PrintRoute(route)
        return []

    value = []
    while not allFalse(available):
        val = random.randrange(4)
        if available[val]:
            value.append(val)
            available[val] = False
    
    direction = []
    for val in value:
        if val == 0:
            direction.append([position[0]-2, position[1]])
        if val == 1:
            direction.append([position[0]+2, position[1]])
        if val == 2:
            direction.append([position[0], position[1]+2])
        if val == 3:
            direction.append([position[0], position[1]-2])
    return direction

def paintMap(route, previous, nowPosition):
    if nowPosition == []:
        return route
    if previous[0] == nowPosition[0]:
        if nowPosition[1] - previous[1] > 0:
            route[nowPosition[0]][nowPosition[1]-1] = '0'
        else:
            route[nowPosition[0]][nowPosition[1]+1] = '0'
    else:
        if nowPosition[0] - previous[0] > 0:
            route[nowPosition[0]-1][nowPosition[1]] = '0'
        else:
            route[nowPosition[0]+1][nowPosition[1]] = '0'
    route[nowPosition[0]][nowPosition[1]] = '0'
    return route

def searchRoute(route, position):
    newPos = makeDirection(route, position)
    for element in newPos:
        if route[element[0]][element[1]] == '0':
            return route
        paintMap(route, position, element)
        # return searchRoute(route, element)
        route = searchRoute(route, element)
    return route


if __name__ == "__main__":
    x = int(input("X: "))
    y = int(input("Y: "))
    #x = 29
    #y = 29

    xPosition = 0
    yPosition = 0
    while xPosition <= 0 or xPosition >= x-1:
        xPosition = random.randrange(1, x, 2)
    while yPosition <= 0 or yPosition >= y-1:
        yPosition = random.randrange(1, y, 2)

    # print(xPosition)
    # print(yPosition)

    route = CreateRoute([yPosition, xPosition], x, y)
    # PrintRoute(route)
    route = searchRoute(route, [yPosition, xPosition])
    print(" -- Route -- ")
    PrintRoute(route)
    print(" -- Code -- ")
    PrintRouteCode(route)
