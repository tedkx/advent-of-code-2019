INPUT = 1


def getParam(lst, param, mode):
    return param if mode == 1 else lst[param]


def getParams(lst, idx, modes, max):
    length = len(modes)
    return [getParam(lst, idx + x + 1, modes[x] if length > x else 0) for x in range(max)]


def printLst(lst):
    pr = ['(' + str(i) + '): ' + str(lst[i])
          for i in [0, 1, 2, 3, 4, 5, 6, 104, 223, 224, 225]]
    return '\n' + ','.join(pr) + '\n'


opParamCounts = [None, 3, 3, 1, 1, 2, 2, 3, 3]


def processList(lst):
    idx = 0
    lastOutput = None
    instructions = []
    record = []
    while True:
        if idx >= len(lst):
            break

        raw = str(lst[idx])
        op = int(raw[-2:])
        if(op == 99):
            break

        paramCount = opParamCounts[op]
        instruction = ",".join([str(x) for x in lst[idx:idx + paramCount + 1]])
        instructions.append(instruction)

        paramModes = []
        for x in range(0, paramCount):
            temp = raw[0 - x - 3:0 - x - 2]
            paramModes.append(0 if not temp else int(temp))

        params = getParams(lst, idx, paramModes, paramCount)

        if(op == 1):
            txt = instruction + ': adding ' + str(lst[params[0]]) + ' + ' + \
                str(lst[params[1]]) + ' = ' + str(lst[params[0]] + lst[params[1]]) + \
                ' to position ' + str(params[2]) + \
                ' | modes ' + str(paramModes)
            lst[params[2]] = lst[params[0]] + lst[params[1]]
            record.append(txt + printLst(lst))
        elif(op == 2):
            txt = instruction + ': multiplying ' + str(lst[params[0]]) + ' * ' + \
                str(lst[params[1]]) + ' = ' + str(lst[params[0]] * lst[params[1]]) + \
                ' to position ' + str(params[2]) + \
                ' | modes ' + str(paramModes)
            lst[params[2]] = lst[params[0]] * lst[params[1]]
            record.append(txt + printLst(lst))
        elif(op == 3):
            txt = instruction + ': inputting ' + \
                str(INPUT) + ' to position ' + str(params[0])
            lst[params[0]] = INPUT
            record.append(txt + printLst(lst))
        elif(op == 4):
            txt = instruction + ': outputing ' + \
                str(lst[params[0]]) + ', param ' + str(params)
            lastOutput = lst[params[0]]
            record.append(txt + printLst(lst))
            if(lastOutput != 0):
                print('NON-ZERO OUTPUT', lastOutput,
                      ', \n\n--- INSTRUCTIONS ---\n', "\n".join(instructions))
                print('\n--- RECORD ---')
                print("\n".join('instr ' + str(i) + ': ' +
                                record[i] for i in range(len(record))))
                break
            else:
                instructions = []
                record = []
        else:
            print("invalid instruction", instruction)

        idx += paramCount + 1
    return lastOutput


def main(file):
    inp = file.read()
    lst = [int(num) for num in inp.split(",")]
    result = processList(lst)
    print("output", result)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
