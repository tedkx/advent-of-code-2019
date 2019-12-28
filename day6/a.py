class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.moons = []

    def add(self, spaceObject):
        self.moons.append(spaceObject)


def parseNode(nodes, orbit):
    [starName, moonName] = orbit.split(')')

    for name in [starName, moonName]:
        if(name not in nodes):
            nodes[name] = SpaceObject(name)

    nodes[starName].add(nodes[moonName])


def traverse(node, level=0):
    sum = level
    for moon in node.moons:
        sum += traverse(moon, level + 1)
    return sum


def main(file):
    orbits = file.read().split('\n')
    nodes = {}

    for orbit in orbits:
        parseNode(nodes, orbit)

    total = traverse(nodes['COM'])
    print('total orbits', total)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
