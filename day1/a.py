import math


def calculateFuelReq(mass):
    return math.floor(int(mass) / 3) - 2


def main():
    file = open("input.txt", mode="r", encoding="utf-8")
    sum = 0
    while True:
        line = file.readline()
        if not line:
            break
        sum += calculateFuelReq(line)
    print("sum", sum)


if __name__ == "__main__":
    main()
