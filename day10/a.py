class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:
    def __init__(self, file):
        self.points = []
        while(True):
            line = file.readline().strip()
            if(not line):
                break
            self.points.append([0 if letter == '.' else 1 for letter in line])
        self.height = len(self.points)
        self.width = len(self.points[0])
        self.edgePoints = []

        for i in range(self.width):
            self.edgePoints.append(Point(i, 0))
        for i in range(1, self.height):
            self.edgePoints.append(Point(self.width - 1, i))
        for i in range(self.width - 2, -1, -1):
            self.edgePoints.append(Point(i, self.height - 1))
        for i in range(self.height - 2, 0, -1):
            self.edgePoints.append(Point(0, i))

    def countVisibleAsteroids(self, refPoint):
        newMap = []
        for refY in range(self.height):
            newMap.append([])
            for refX in range(self.width):
                if(self.points[refY][refX] == 0):
                    newMap[refY].append('.')
                    continue

                sum = 0
                for edgePoint in self.edgePoints:
                    if(edgePoint.x == refX and edgePoint.y == refY):
                        continue
                    print('----\nedgepoint', edgePoint.x,
                          edgePoint.y, 'ref', refX, refY)
                    diffX = edgePoint.x - refX
                    diffY = edgePoint.y - refY
                    minDim = min(abs(diffX), abs(diffY))
                    if(minDim == 0):
                        stepX = 0 if diffX == 0 else -1 if diffX < 0 else 1
                        stepY = 0 if diffY == 0 else -1 if diffY < 0 else 1
                    else:
                        #print('min', minDim)
                        stepX, stepY = diffX / minDim, diffY / minDim
                    #print('diff', diffX, diffY, 'step', stepX, stepY)
                    x, y = edgePoint.x, edgePoint.y
                    while(True):
                        print('x,y', x, y)
                        if(x == refX and y == refY):
                            break
                        if(x < 0 or y < 0 or x > self.width or y > self.height):
                            print('breaking')
                            break
                        intx, inty = int(x), int(y)
                        print('intvals', intx == x and inty == y)
                        if(intx == x and inty == y and self.points[inty][intx] == 1):
                            print('asteroid found in', x, y)
                            sum += 1
                            break
                        x -= stepX
                        y -= stepY
                    #print('sum', tempsum)
                newMap[refY].append(sum)
                print('point', refX, refY, 'sum', sum)
        for l in newMap:
            print(l)


def main(file):
    map = Map(file)
    print('map', map.points)
    map.countVisibleAsteroids(None)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
