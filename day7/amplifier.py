def getParam(lst, param, mode):
    return param if mode == 1 else lst[param]


def getParams(lst, idx, modes, max):
    length = len(modes)
    return [getParam(lst, idx + x + 1, modes[x] if length > x else 0) for x in range(max)]


opParamCounts = [None, 3, 3, 1, 1, 2, 2, 3, 3]


class Amplifier:
    def __init__(self, phase):
        self.phase = phase
        self.usedPhaseAsInput = False

    def process(self, lst, _input):
        idx = 0

        try:
            while True:
                if idx >= len(lst):
                    break

                raw = str(lst[idx])
                op = int(raw[-2:])
                if(op == 99):
                    break

                paramCount = opParamCounts[op]
                instruction = ",".join([str(x)
                                        for x in lst[idx:idx + paramCount + 1]])

                paramModes = []
                for x in range(0, paramCount):
                    temp = raw[0 - x - 3:0 - x - 2]
                    paramModes.append(0 if not temp else int(temp))

                params = getParams(lst, idx, paramModes, paramCount)

                if(op == 1):
                    lst[params[2]] = lst[params[0]] + lst[params[1]]
                elif(op == 2):
                    lst[params[2]] = lst[params[0]] * lst[params[1]]
                elif(op == 3):
                    lst[params[0]] = _input if self.usedPhaseAsInput else self.phase
                    self.usedPhaseAsInput = True
                elif(op == 4):
                    output = lst[params[0]]
                    if(output != 0):
                        return output
                elif(op == 5):
                    if(lst[params[0]] != 0):
                        idx = lst[params[1]]
                        continue
                elif(op == 6):
                    if(lst[params[0]] == 0):
                        idx = lst[params[1]]
                        continue
                elif(op == 7):
                    lst[params[2]] = 1 if lst[params[0]] < lst[params[1]] else 0
                elif(op == 8):
                    lst[params[2]] = 1 if lst[params[0]] == lst[params[1]] else 0
                else:
                    print("invalid instruction", instruction)

                idx += paramCount + 1
        except Exception as e:
            print('Invalid phase?', e)
        return 0
