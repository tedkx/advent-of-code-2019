from instruction import Instruction
from point import Point


def main():
    file = open("input.txt", mode="r", encoding="utf-8")
    wire1 = file.readline().strip().split(',')
    wire2 = file.readline().strip().split(',')

    pos = Point(1, 1)
    dic = {}
    for idx in range(len(wire1)):
        instr = Instruction(wire1[idx])
        current = instr.count
        while current > 0:
            instr.mutatePos(pos)
            dic[pos.key()] = "1"
            current -= 1
    pos = Point(1, 1)
    closest = -1
    for idx in range(len(wire2)):
        instr = Instruction(wire2[idx])
        current = instr.count
        while current > 0:
            current -= 1
            instr.mutatePos(pos)
            if(pos.key() in dic):
                distance = abs(pos.x - 1) + abs(pos.y - 1)
                print('intersection distance', distance, 'on', pos.key())
                if(closest == -1 or closest > distance):
                    closest = distance
    print('closest intersection', closest)


if __name__ == "__main__":
    main()
