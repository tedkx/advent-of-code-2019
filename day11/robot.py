from point import Point

directions = [
    Point(0, -1),
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0)
]
dirlength = len(directions)


class Robot:
    def __init__(self, position: Point):
        self.direction = 0
        self.position = position

    def move(self, arg: int):
        self.direction += -1 if arg == 0 else 1

        if(self.direction < 0):
            self.direction = dirlength - 1
        elif(self.direction >= dirlength):
            self.direction = 0

        self.position = Point(self.position.x + directions[self.direction].x,
                              self.position.y + directions[self.direction].y)
