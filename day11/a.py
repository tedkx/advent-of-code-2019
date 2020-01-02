from robot import Robot
from intcodeprogram import IntCodeProgram
from point import Point

BLACK = 0
WHITE = 1


class Hull:
    @staticmethod
    def createKey(point: Point):
        return '{},{}'.format(point.x, point.y)

    def __init__(self):
        self.grid = {}

    def paint(self, panel: Point, color: str):
        self.grid[Hull.createKey(panel)] = color

    def getColor(self, panel: Point) -> int:
        key = Hull.createKey(panel)
        return BLACK if key not in self.grid else self.grid[key]


def main(file):
    hull = Hull()
    robot = Robot(Point(0, 0))
    program = IntCodeProgram(file.read().strip().split(','))

    while(True):
        fromPosition = robot.position

        currentColor = hull.getColor(robot.position)
        status, color, direction = program.process(currentColor)
        hull.paint(robot.position, color)
        robot.move(direction)

        print(color, direction, 'left ' if direction == 0 else 'right',
              'supplied', 'black' if currentColor == BLACK else 'white',
              'painted', 'black' if color == BLACK else 'white',
              'and moved',
              '[{},{}] -> [{},{}]'.format(fromPosition.x, fromPosition.y,
                                          robot.position.x, robot.position.y))
        #   '\n',
        #   ','.join([key + ' ' + str(hull.grid[key]) for key in sorted(hull.grid)]))

        if(status != 'OUTPUT'):
            break

    print('unique paints:', len(hull.grid))


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
