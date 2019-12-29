WIDTH = 25
HEIGHT = 6


class Layer:
    def __init__(self, bitmapStr):
        self.list = []
        self.zeroes = 0
        self.ones = 0
        self.twos = 0
        for letter in bitmapStr:
            if(letter == '0'):
                self.zeroes += 1
            if(letter == '1'):
                self.ones += 1
            if(letter == '2'):
                self.twos += 1


def main(file):
    inp = file.read()
    step = HEIGHT * WIDTH
    layers = [Layer(inp[idx:idx + step]) for idx in range(0, len(inp), step)]

    fewestZeroesLayer = layers[0]
    for idx in range(1, len(layers)):
        if(layers[idx].zeroes < fewestZeroesLayer.zeroes):
            fewestZeroesLayer = layers[idx]

    print(fewestZeroesLayer.ones, '*', fewestZeroesLayer.twos, ' = ',
          fewestZeroesLayer.ones * fewestZeroesLayer.twos)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
