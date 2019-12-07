def main(input):
    lst = [int(num) for num in input.split(",")]
    idx = 0
    lst[1] = 12
    lst[2] = 2
    print("START", lst)
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
    print("OUTPUT", lst[0])


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file.read())
