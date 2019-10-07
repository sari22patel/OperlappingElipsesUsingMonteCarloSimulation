from ellipse import Point
from ellipse import Rectangle
from ellipse import Ellipse
from numpy.random import uniform

def getRectangle(e1, e2):
    """
    Compute the lowerLeftX, lowerLeftY, upperRightX, and upperRightY value for Rectangle using the information from ellipse 1 and ellipse 2 and return a rectangle.

    Parameters:
        e1 (Ellipse): First instance of Ellipse class
        e2 (Ellipse): Second instance of Ellipse class

    Returns:
        r (Rectangle): an nstance of Rectangle class
    """
    minX = min(e1.getFocalPoint1().getX(), e1.getFocalPoint2().getX(), e1.getFocalPoint1().getX(), e1.getFocalPoint2().getX())
    maxX = max(e1.getFocalPoint1().getX(), e1.getFocalPoint2().getX(), e1.getFocalPoint1().getX(), e1.getFocalPoint2().getX())
    minY = min(e1.getFocalPoint1().getY(), e1.getFocalPoint2().getY(), e1.getFocalPoint1().getY(), e1.getFocalPoint2().getY())
    maxY = max(e1.getFocalPoint1().getY(), e1.getFocalPoint2().getY(), e1.getFocalPoint1().getY(), e1.getFocalPoint2().getY())
    maxWidth = max(e1.getWidth(), e2.getWidth())

    r = Rectangle(minX - maxWidth, minY - maxWidth, maxX + maxWidth, maxY + maxWidth)

    return r

def computeAreaOfOverlap(e1, e2, rect):
    """
    Compute the area of overlap using the Monte Carlo Simulation technique. The inputs are two instance of Ellipse (whose area of overlap needs to be find) and the rectangle who embeds these two Ellipse.

    Parameters:
        e1 (Ellipse): First instance of Ellipse class
        e2 (Ellipse): Second instance of Ellipse class
        rect (Rectangle): Instance of Rectangle class

    Returns:
        area (float): Area of overlap between two Ellipse.
    """
    n = int(rect.getArea()*1000)
    magnifiedArea = 0
    for i in range(0,n):
        xCoord = uniform(rect.getLowerLeftX(), rect.getUpperRightX())
        yCoord = uniform(rect.getLowerLeftY(), rect.getUpperRightY())
        randomPoint = Point(xCoord, yCoord)
        sumOfDistToEclipse1Foci = randomPoint.getDistanceTo(e1.getFocalPoint1()) + randomPoint.getDistanceTo(e1.getFocalPoint2())
        sumOfDistToEclipse2Foci = randomPoint.getDistanceTo(e2.getFocalPoint1()) + randomPoint.getDistanceTo(e2.getFocalPoint2())
        if (sumOfDistToEclipse1Foci <= e1.getWidth()) and (sumOfDistToEclipse2Foci <= e2.getWidth()):
            magnifiedArea +=1

        area = round(((magnifiedArea * rect.getArea())/n), 4)

    return area

def getAreaOfOverlap(e1, e2):
    """
    Calculates a rectangle that embeds both the Ellipse and calls the computeAreaOfOverlap method to calculate the area of overlap between two Ellipse passed as parametersself.

    Parameters:
        e1 (Ellipse): First instance of Ellipse class
        e2 (Ellipse): Second instance of Ellipse class

    Returns:
        area (float): Area of overlap between two Ellipse.
    """
    rect = getRectangle(e1, e2)
    area = computeAreaOfOverlap(e1, e2, rect)
    return area

if __name__ == '__main__':
    eclipse1FocalPoint1 = Point(-2.236, 0)
    eclipse1FocalPoint2 = Point(2.236, 0)
    e1 = Ellipse(eclipse1FocalPoint1, eclipse1FocalPoint2, 6)
    eclipse2FocalPoint1 = Point(-1.8284, -0.5)
    eclipse2FocalPoint2 = Point(3.8284, -0.5)
    e2 = Ellipse(eclipse2FocalPoint1, eclipse2FocalPoint2, 6)
    print(e1)
    print(e2)
    print("Area of overlap = {}".format(getAreaOfOverlap(e1, e2)))
