def isValidPassword(password):
    strPassword = str(password)
    dic = {}

    for idx in range(0, len(strPassword)):
        if(idx != 0 and strPassword[idx] < strPassword[idx - 1]):
            return False
        char = strPassword[idx]
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    for key in dic:
        if(dic[key] == 2):
            return True
    return False


def main(file):
    [start, stop] = [int(x.strip()) for x in file.readline().split("-")]
    print('start', start, 'stop', stop)
    count = 0
    for num in range(start, stop + 1):
        #print(num, 'is valid', isValidPassword(num))
        if(isValidPassword(num)):
            count += 1
    print('total valid passwords', count)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
