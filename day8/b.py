WIDTH = 25
HEIGHT = 6


class Image:
    def __init__(self, width, height, bitmapStr):
        step = width * height
        self.width = width
        self.height = height
        self.layers = [Layer(width, height, bitmapStr[idx:idx + step])
                       for idx in range(0, len(bitmapStr), step)]

    def compose(self):
        bitmap = []
        layersLength = len(self.layers)
        for y in range(self.height):
            for x in range(self.width):
                if(len(bitmap) <= y):
                    bitmap.append([])
                for i in range(layersLength):
                    color = self.layers[i].pixels[y][x]
                    if(color != 2):
                        bitmap[y].append('8' if color == 1 else '.')
                        break
        return bitmap


class Layer:
    def __init__(self, width, height, bitmapStr):
        self.pixels = []
        for y in range(height):
            for x in range(width):
                if(len(self.pixels) <= y):
                    self.pixels.append([])
                base = y * width
                self.pixels[y].append(int(bitmapStr[base + x:base + x + 1]))


def main(file):
    image = Image(WIDTH, HEIGHT, file.read())

    for line in image.compose():
        print(' '.join(line))


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
