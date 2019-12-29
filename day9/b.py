from a import process


def main(file):
    lst = [int(str) for str in file.read().strip().split(',')]
    status, code = process(lst, 2)
    print(status, '-', code)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
