# Boston Mansheim
# Lab 3
# Question 1 Part A

def circleArea(radius) -> float:
    '''
    Calculates the area of a circle when given the radius
    :param radius: positive number
    :return: returns answer as float or error as string
    '''
    try:
        radius = float(radius)
    except:
        if type(radius) != int and type(radius) != float:
            return 'enter a number'
        else:
            raise Exception('Unknown ERROR Occurred')

    if radius <= 0:
        return 'positive numbers only'

    return float(3.1416 * (radius * radius))


def rectangleArea (length, width) -> float:
    '''
    Calculates the area of a rectangle when give length and width
    :param length: positive number
    :param width: positive number
    :return: returns answer as float or error as string
    '''
    try:
        length = float(length)
        width = float(width)
    except:
        if type(length) != int and type(length) != float:
            return 'enter a number'
        elif type(width) != int and type(width) != float:
            return 'enter a number'
        else:
            raise Exception('Unknown ERROR Occurred')

    if length <= 0 or width <=0:
        return 'positive numbers only'

    return float(length * width)


def squareArea (length) -> float:
    '''
    Calculates the area of a square when given a side length
    :param length: positive number
    :return: returns answer as float or error as string
    '''
    try:
        length = float(length)
    except:
        if type(length) != int and type(length) != float:
            return 'enter a number'
        else:
            raise Exception('Unknown ERROR Occurred')

    if length <= 0:
        return 'positive numbers only'

    return float(length * length)


def triangleArea (length, width) -> float:
    '''
    Calculates the area of a triangle when given the length and width
    :param length: positive number
    :param width: positive number
    :return: returns answer as float or error as string
    '''
    try:
        length = float(length)
        width = float(width)
    except:
        if type(length) != int and type(length) != float:
            return 'enter a number'
        elif type(width) != int and type(width) != float:
            return 'enter a number'
        else:
            raise Exception('Unknown ERROR Occurred')

    if length <= 0 or width <=0:
        return 'positive numbers only'

    return float(.5 * length * width)

