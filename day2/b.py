target = 19690720


def runInstructions(lst):
    idx = 0
    while True:
        if idx >= len(lst):
            break
        if(lst[idx] == 99):
            break
        num1 = lst[lst[idx + 1]]
        num2 = lst[lst[idx + 2]]
        pos = lst[idx + 3]
        if(lst[idx] == 1):
            lst[pos] = num1 + num2
        elif(lst[idx] == 2):
            lst[pos] = num1 * num2
        idx += 4
    return lst[0]


def getTargetInputs(lst):
    for noun in range(100):
        for verb in range(100):
            program = [lst[0], noun, verb] + lst[3:]
            output = runInstructions(program)
            if(output == target):
                return 100 * noun + verb
    return 0


def main(input):
    lst = [int(num) for num in input.split(",")]
    print("anwser", getTargetInputs(lst))


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file.read())
