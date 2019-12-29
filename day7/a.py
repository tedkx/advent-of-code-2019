from amplifier import Amplifier


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
    for permutation in generatePhasePermutation(5, [0, 1, 2, 3, 4]):
        amplifiers = [Amplifier(phase) for phase in permutation]
        io = 0
        for amplifier in amplifiers:
            io = amplifier.process(lst, io)
        if(best['output'] < io):
            best['output'] = io
            best['permutation'] = permutation
    print('best:', best['permutation'], best['output'])


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
