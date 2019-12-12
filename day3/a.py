class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def key(self):
        return str(self.x) + ',' + str(self.y)


class Instruction:
    def __init__(self, str):
        self.operation = str[0]
        self.count = int(str[1:])

    def mutatePos(self, pos):
        if(self.operation == "U"):
            pos.y += 1
        elif(self.operation == "D"):
            pos.y -= 1
        elif(self.operation == "R"):
            pos.x += 1
        elif(self.operation == "L"):
            pos.x -= 1
        return pos


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
