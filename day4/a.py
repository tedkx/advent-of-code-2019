def isValidPassword(password):
    foundAdjacent = False
    strPassword = str(password)
    for idx in range(1, len(strPassword)):
        current = strPassword[idx]
        previous = strPassword[idx - 1]
        if(current < previous):
            return False
        if(current == previous):
            foundAdjacent = True
    return foundAdjacent


def main(file):
    [start, stop] = [int(x.strip()) for x in file.readline().split("-")]
    print('start', start, 'stop', stop)
    count = 0
    for num in range(start, stop + 1):
        if(isValidPassword(num)):
            count += 1
    print('total valid passwords', count)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
