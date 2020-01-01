from point import Point


class AsteroidMap:
    def __init__(self, file):
        self.asteroids = []
        y = 0
        while(True):
            line = file.readline().strip()
            if(not line):
                break
            for x in range(len(line)):
                if(line[x] == '#'):
                    self.asteroids.append(Point(x, y))
            y += 1

        self.height = y
        self.width = x + 1
