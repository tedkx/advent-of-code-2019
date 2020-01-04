from point import Point

BLACK = 0
WHITE = 1


class Hull:
    @staticmethod
    def createKey(point: Point):
        return '{},{}'.format(point.x, point.y)

    def __init__(self, startColor=BLACK):
        self.grid = {}
        self.startColor = startColor
        self.movedFromStart = False
        self.topLeft = Point(0, 0)
        self.bottomRight = Point(0, 0)

    def paint(self, panel: Point, color: str):
        self.grid[Hull.createKey(panel)] = color
        if(panel.x < self.topLeft.x):
            self.topLeft.x = panel.x
        if(panel.y < self.topLeft.y):
            self.topLeft.y = panel.y
        if(panel.x > self.bottomRight.x):
            self.bottomRight.x = panel.x
        if(panel.y > self.bottomRight.y):
            self.bottomRight.y = panel.y

    def getColor(self, panel: Point) -> int:
        key = Hull.createKey(panel)
        if(key not in self.grid):
            if(self.movedFromStart):
                return BLACK
            else:
                self.movedFromStart = True
                return self.startColor
        return self.grid[key]
