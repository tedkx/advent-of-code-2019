class SpaceObject:
    def __init__(self, name, parent=None):
        self.name = name
        self.moons = []
        self.parent = parent

    def add(self, spaceObject):
        self.moons.append(spaceObject)

    def setParent(self, spaceObject):
        self.parent = spaceObject

    def setLevel(self, level):
        self.level = level


def parseNode(nodes, orbit):
    [starName, moonName] = orbit.split(')')

    if(starName not in nodes):
        nodes[starName] = SpaceObject(starName)
    star = nodes[starName]

    if(moonName not in nodes):
        nodes[moonName] = SpaceObject(moonName, star)
    elif(not nodes[moonName].parent):
        nodes[moonName].setParent(star)

    star.add(nodes[moonName])


def traverse(node, level=0):
    node.setLevel(level)
    for moon in node.moons:
        traverse(moon, level + 1)


def getParentNames(node):
    lst = []
    parent = node.parent
    while(parent and parent.name != 'COM'):
        lst.append(parent.name)
        parent = parent.parent
    return lst


def findCommonParent(allNodes, node1, node2):
    for name1 in getParentNames(node1):
        for name2 in getParentNames(node2):
            if name1 == name2:
                return allNodes[name1]

    return None


def main(file):
    orbits = file.read().split('\n')
    nodes = {}

    for orbit in orbits:
        parseNode(nodes, orbit)

    traverse(nodes['COM'])

    you = nodes['YOU']
    santa = nodes['SAN']
    parentStar = findCommonParent(nodes, you, santa)

    print('number of orbital transfers',
          you.level - parentStar.level - 1 +
          santa.level - parentStar.level - 1)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
