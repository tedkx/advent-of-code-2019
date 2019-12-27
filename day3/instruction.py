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
