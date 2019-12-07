import math


def calculateFuelRecursiveReq(mass):
    req = math.floor(int(mass) / 3) - 2
    if req > 0:
        req += calculateFuelRecursiveReq(req)
    else:
        req = 0
    return req


def main():
    file = open("input.txt", mode="r", encoding="utf-8")
    sum = 0
    while True:
        line = file.readline()
        if not line:
            break
        fuel = calculateFuelRecursiveReq(line)
        print("fuel for", int(line), "->", fuel)
        sum += fuel
    print("sum", sum)


if __name__ == "__main__":
    main()
