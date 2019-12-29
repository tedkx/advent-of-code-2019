HALT_CODE = 'HALT'


def getParam(lst, param, mode):
    return param if mode == 1 else lst[param]


def getParams(lst, idx, modes, max):
    length = len(modes)
    return [getParam(lst, idx + x + 1, modes[x] if length > x else 0) for x in range(max)]


opParamCounts = [None, 3, 3, 1, 1, 2, 2, 3, 3]


class Amplifier:
    def __init__(self, lst, phase):
        self.phase = phase
        self.usedPhaseAsInput = False
        self.lst = lst.copy()
        self.idx = 0
        self.done = False

    def process(self, _input):
        try:
            while True:
                if self.idx >= len(self.lst):
                    break

                raw = str(self.lst[self.idx])
                op = int(raw[-2:])
                if(op == 99):
                    self.done = True
                    return HALT_CODE

                paramCount = opParamCounts[op]
                instruction = ",".join([str(x)
                                        for x in self.lst[self.idx:self.idx + paramCount + 1]])

                paramModes = []
                for x in range(0, paramCount):
                    temp = raw[0 - x - 3:0 - x - 2]
                    paramModes.append(0 if not temp else int(temp))

                params = getParams(self.lst, self.idx, paramModes, paramCount)

                if(op == 1):
                    self.lst[params[2]] = self.lst[params[0]] + \
                        self.lst[params[1]]
                elif(op == 2):
                    self.lst[params[2]] = self.lst[params[0]] * \
                        self.lst[params[1]]
                elif(op == 3):
                    self.lst[params[0]
                             ] = _input if self.usedPhaseAsInput else self.phase
                    self.usedPhaseAsInput = True
                elif(op == 4):
                    output = self.lst[params[0]]
                    self.idx += paramCount + 1
                    return output
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
                else:
                    print("invalid instruction", instruction)

                self.idx += paramCount + 1
        except Exception as e:
            print('Invalid phase?', e)
        return 0
