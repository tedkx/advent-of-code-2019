from point import Point
from utils import calcAngle
from asteroidmap import AsteroidMap
from a import getMostSuitableAsteroid


def populateAngles(asteroidMap, cannon):
    angles = {}

    for asteroid in asteroidMap.asteroids:
        angle = calcAngle(cannon, asteroid)
        if(angle == None):
            continue
        if (angle not in angles):
            angles[angle] = []

        angles[angle].append(asteroid)

    for angle in angles:
        # sort asteroids in each line. nearest first
        angles[angle].sort(key=lambda p: abs(
            cannon.x - p.x) + abs(cannon.y - p.y))

    return angles


def vaporizeTehSpace(anglePoints):
    i = 1
    while(len(anglePoints) > 0):
        # sort by angle, smallest first
        for angle in sorted(anglePoints):
            alderaan = anglePoints[angle][0]
            if(i == 200):
                return alderaan

            if(len(anglePoints[angle]) == 1):
                del anglePoints[angle]
            else:
                anglePoints[angle] = anglePoints[angle][1:]

            i += 1

    return Point(-1, -1)


def main(file):
    asteroidMap = AsteroidMap(file)
    cannon, _ = getMostSuitableAsteroid(asteroidMap)
    print('setting pewpew to [', cannon.x, ',', cannon.y, ']')
    anglePoints = populateAngles(asteroidMap, cannon)
    bet = vaporizeTehSpace(anglePoints)
    print('the 200th asteroid to be vaporized is [', bet.x, ',', bet.y, '], answer: ',
          bet.x * 100 + bet.y)


if __name__ == "__main__":
    file = open("input.txt", mode="r", encoding="utf-8")
    main(file)
