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
    steps = 0
    dic = {}
    for idx in range(len(wire1)):
        instr = Instruction(wire1[idx])
        current = instr.count
        while current > 0:
            steps += 1
            instr.mutatePos(pos)
            dic[pos.key()] = steps
            current -= 1

    pos = Point(1, 1)
    closest = -1
    steps = 0
    for idx in range(len(wire2)):
        instr = Instruction(wire2[idx])
        current = instr.count
        while current > 0:
            steps += 1
            current -= 1
            instr.mutatePos(pos)
            if(pos.key() in dic):
                totalSteps = dic[pos.key()] + steps
                print('intersection steps, a ',
                      dic[pos.key()], 'b ', steps, 'total', totalSteps)
                if(closest == -1 or closest > totalSteps):
                    closest = totalSteps
    print('least steps to intersection', closest)


if __name__ == "__main__":
    main()
