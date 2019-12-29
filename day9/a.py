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


def process(lst, _input):
    idx = 0
    relativeBase = 0
    outputs = []

    try:
        while True:
            if idx >= len(lst):
                return 'INVALID INDEX:' + str(idx), -1

            raw = str(lst[idx])
            op = int(raw[-2:])
            if(op == 99):
                return 'HALT', ','.join([str(o) for o in outputs])

            paramCount = opParamCounts[str(op)]
            instruction = ",".join([str(x)
                                    for x in lst[idx:idx + paramCount + 1]])

            paramModes = []
            for x in range(0, paramCount):
                temp = raw[0 - x - 3:0 - x - 2]
                paramModes.append(0 if not temp else int(temp))

            params = getParams(lst, idx, relativeBase, paramModes, paramCount)

            if(op == 1):
                lst[params[2]] = lst[params[0]] + lst[params[1]]
            elif(op == 2):
                lst[params[2]] = lst[params[0]] * lst[params[1]]
            elif(op == 3):
                lst[params[0]] = _input
            elif(op == 4):
                output = lst[params[0]]
                outputs.append(output)
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
            elif(op == 9):
                relativeBase += lst[params[0]]
            else:
                return 'INVALID INSTRUCTION: ' + instruction, -1

            idx += paramCount + 1
    except Exception as e:
        print('exception', e)
        return 'EXCEPTION', -1


def main(file):
    lst = [int(str) for str in file.read().strip().split(',')]
    status, code = process(lst, 1)
    print(status, '-', code)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
