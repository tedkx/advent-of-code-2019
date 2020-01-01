from point import Point
from utils import calcAngle
from asteroidmap import AsteroidMap


def getMostSuitableAsteroid(asteroidMap, printLOS=False):
    newMap = [['.' for x in range(asteroidMap.width)]
              for y in range(asteroidMap.height)] if printLOS else []
    best = {"count": 0, "point": None}
    for candidate in asteroidMap.asteroids:
        angles = {}
        sum = 0

        for asteroid in asteroidMap.asteroids:
            angle = calcAngle(candidate, asteroid)
            if (angle != None and angle not in angles):
                angles[angle] = True
                sum += 1

        if(printLOS):
            newMap[candidate.y][candidate.x] = sum

        if(sum > best["count"]):
            best["count"] = sum
            best["point"] = candidate

    if(printLOS):
        print('\nline of sight map\n------')
        for mapLine in newMap:
            print(' '.join([str(x).rjust(3) for x in mapLine]))

    return best["point"], best["count"]


def main(file):
    asteroidMap = AsteroidMap(file)

    bestPoint, bestCount = getMostSuitableAsteroid(asteroidMap, True)
    print('\nmost suitable asteroid is [', bestPoint.x, ',',
          bestPoint.y, '] with', bestCount, 'visible')


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
