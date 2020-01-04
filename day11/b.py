from robot import Robot
from intcodeprogram import IntCodeProgram
from point import Point
from hull import Hull, BLACK, WHITE


def main(file):
    hull = Hull(WHITE)
    robot = Robot(Point(0, 0))
    program = IntCodeProgram(file.read().strip().split(','))

    while(True):
        currentColor = hull.getColor(robot.position)
        status, color, direction = program.process(currentColor)
        hull.paint(robot.position, color)
        robot.move(direction)

        if(status != 'OUTPUT'):
            break

    x = hull.topLeft.x
    y = hull.topLeft.y
    line = ''
    while(x <= hull.bottomRight.x and y <= hull.bottomRight.y):
        color = hull.getColor(Point(x, y))
        line += '.' if color == BLACK else '#'
        x += 1
        if(x >= hull.bottomRight.x):
            print(line)
            line = ''
            y += 1
            x = hull.topLeft.x


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
