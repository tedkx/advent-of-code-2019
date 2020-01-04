opParamCounts = {
    "0": None,
    "1": 3,
    "2": 3,
    "3": 1,
    "4": 1,
    "5": 2,
    "6": 2,
    "7": 3,
    "8": 3,
    "9": 1
}


def resizeList(lst, idx):
    while(len(lst) <= idx):
        lst.append(0)


def getParam(lst, param, relativeBase, mode):
    if(mode == 1):
        return param

    resizeList(lst, param)

    if(mode == 0):
        resizeList(lst, lst[param])
        return lst[param]

    value = lst[param] + relativeBase
    resizeList(lst, value)
    return value


def getParams(lst, idx, relativeBase, modes, max):
    length = len(modes)
    return [getParam(lst, idx + x + 1, relativeBase, modes[x] if length > x else 0) for x in range(max)]


class IntCodeProgram:
    def __init__(self, lst):
        self.idx = 0
        self.relativeBase = 0
        self.lst = [int(x) for x in lst]

    def process(self, _input: int):
        outputs = []

        try:
            while True:
                if self.idx >= len(self.lst):
                    return 'INVALID INDEX:' + str(self.idx), -1, -1

                raw = str(self.lst[self.idx])
                op = int(raw[-2:])
                if(op == 99):
                    return 'HALT', ','.join([str(o) for o in outputs]), -1

                paramCount = opParamCounts[str(op)]
                instruction = ",".join([str(x)
                                        for x in self.lst[self.idx:self.idx + paramCount + 1]])

                paramModes = []
                for x in range(0, paramCount):
                    temp = raw[0 - x - 3:0 - x - 2]
                    paramModes.append(0 if not temp else int(temp))

                params = getParams(self.lst, self.idx, self.relativeBase,
                                   paramModes, paramCount)

                if(op == 1):
                    self.lst[params[2]] = self.lst[params[0]] + \
                        self.lst[params[1]]
                elif(op == 2):
                    self.lst[params[2]] = self.lst[params[0]] * \
                        self.lst[params[1]]
                elif(op == 3):
                    self.lst[params[0]] = _input
                elif(op == 4):
                    output = self.lst[params[0]]
                    outputs.append(output)
                elif(op == 5):
                    if(self.lst[params[0]] != 0):
                        self.idx = self.lst[params[1]]
                        continue
                elif(op == 6):
                    if(self.lst[params[0]] == 0):
                        self.idx = self.lst[params[1]]
                        continue
                elif(op == 7):
                    self.lst[params[2]] = 1 if self.lst[params[0]
                                                        ] < self.lst[params[1]] else 0
                elif(op == 8):
                    self.lst[params[2]] = 1 if self.lst[params[0]
                                                        ] == self.lst[params[1]] else 0
                elif(op == 9):
                    self.relativeBase += self.lst[params[0]]
                else:
                    return 'INVALID INSTRUCTION: ' + instruction, -1, -1

                self.idx += paramCount + 1
                if(len(outputs) >= 2):
                    return 'OUTPUT', outputs[0], outputs[1]
        except Exception as e:
            print('exception', e, 'raw', raw, 'idx', self.idx)
            return 'EXCEPTION', -1, -1
