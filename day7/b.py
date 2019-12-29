from interminent_amplifier import Amplifier, HALT_CODE


def generatePhasePermutation(n, elems):
    if(n == 1):
        yield elems
    else:
        for i in range(n - 1):
            for perm in generatePhasePermutation(n - 1, elems):
                yield perm
            j = 0 if (n % 2) == 1 else i
            elems[j], elems[n - 1] = elems[n - 1], elems[j]
        for perm in generatePhasePermutation(n - 1, elems):
            yield perm


def main(file):
    lst = [int(item) for item in file.read().split(',')]
    best = {"permutation": None, "output": 0}
    for permutation in generatePhasePermutation(5, [5, 6, 7, 8, 9]):
        amplifiers = [Amplifier(lst, phase) for phase in permutation]
        io = 0
        while(True):
            doneAmplifiers = [a for a in amplifiers if a.done == True]
            if(len(doneAmplifiers) == len(amplifiers)):
                break

            for amplifier in amplifiers:
                tempIo = amplifier.process(io)
                if(tempIo != HALT_CODE):
                    io = tempIo
            if(best['output'] < io):
                best['output'] = io
                best['permutation'] = permutation

    print('best:', best['permutation'], best['output'])


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
