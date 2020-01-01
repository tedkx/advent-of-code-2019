def calcAngle(referencePoint, otherPoint):
    if(referencePoint.x == otherPoint.x and referencePoint.y == otherPoint.y):
        return None
    opposite = otherPoint.y - referencePoint.y
    tangent = otherPoint.x - referencePoint.x
    if(opposite == 0):
        return 3 if tangent < 0 else 1
    if(tangent == 0):
        return 0 if opposite < 0 else 2
    hypotenuse = (opposite ** 2 + tangent ** 2)**(1/2)

    # set quadrant coefficients so angles are ever increasing,
    # starting with the top right
    # 3 | 0
    # -------
    # 2 | 1
    if opposite < 0 and tangent > 0:
        quadrant = 0
    elif opposite > 0 and tangent > 0:
        quadrant = 1
    elif opposite > 0 and tangent < 0:
        quadrant = 2
    else:
        quadrant = 3

    # enforce angles being ever increasing and within quadrant bounds
    if(opposite * tangent < 0):
        return round(quadrant + 1 - abs(opposite / hypotenuse), 6)
    else:
        return round(quadrant + abs(opposite / hypotenuse), 6)
