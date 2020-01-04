from robot import Robot
from intcodeprogram import IntCodeProgram
from point import Point
from hull import Hull


def main(file):
    hull = Hull()
    robot = Robot(Point(0, 0))
    program = IntCodeProgram(file.read().strip().split(','))

    while(True):
        currentColor = hull.getColor(robot.position)
        status, color, direction = program.process(currentColor)
        hull.paint(robot.position, color)
        robot.move(direction)

        if(status != 'OUTPUT'):
            break

    print('unique paints:', len(hull.grid))


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
