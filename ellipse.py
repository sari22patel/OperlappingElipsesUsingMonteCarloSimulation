#Point Class for cal distance

from math import sqrt
from math import pi

class Point:
    """
    This class store information about a point in a catersian coordinate system and perform operations on these points.

    Attributes:
        x (int): x coordinate of point
        y (int): y coordinate of point
    """
    def __init__(self, x=0, y=0):
        """
        The constructor of Point class.

        Parameters:
            x (int): x coordinate of point
            y (int): y coordinate of point
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        The string representation of Point class.

        Returns:
            st: String representation of Point class.
        """
        st = "Point({}, {})".format(self.x, self.y)

        return st

    def setX(self, x):
        """
        Class method to set x coordinate of Point.

        Parameters:
            x (int): x coordinate of point
        """
        self.x = x

    def setY(self, y):
        """
        Class method to set x coordinate of Point.

        Parameters:
            y (int): y coordinate of point
        """
        self.y = y

    def getX(self):
        """
        Class method to return x coordinate of Point.

        Returns:
            x (int): x coordinate of point
        """
        return self.x

    def getY(self):
        """
        Class method to return y coordinate of Point.

        Returns:
            y (int): y coordinate of point
        """
        return self.y

    def getDistanceTo(self, b):
        """
        This method calculates teh distance between the point and an another point passed to the method as parameter.

        Parameters:
            b (Point): Point to compute distance to.

        Returns:
            dist (float): distance of given point to another point
        """
        dist = sqrt((((b.getX() - self.getX())**2) + ((b.getY() - self.getY())**2)))
        return round(dist, 4)

class Rectangle:
    """
    This class store information about a Rectance object and returns imoprtant properties of a Rectangle.

    Attributes:
        lowerLeftX (int): x coordinate of the lower left point of Rectagle
        lowerLeftY (int): y coordinate of the lower left point of Rectagle
        upperRightX (int): x coordinate of the upper right point of Rectagle
        upperRightY (int): y coordinate of the upper right point of Rectagle
    """
    def __init__(self, lowerLeftX=0, lowerLeftY=0, upperRightX=1, upperRightY=1):
        """
        The constructor of Rectangle class.

        Parameters:
            lowerLeftX (int): x coordinate of the lower left point of Rectagle
            lowerLeftY (int): y coordinate of the lower left point of Rectagle
            upperRightX (int): x coordinate of the upper right point of Rectagle
            upperRightY (int): y coordinate of the upper right point of Rectagle
        """
        self.lowerLeftX = lowerLeftX
        self.lowerLeftY = lowerLeftY
        self.upperRightX = upperRightX
        self.upperRightY = upperRightY

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(self.lowerLeftX, self.lowerLeftY, self.upperRightX, self.upperRightY)

    def __eq__(self, obj):
        return self.getLowerLeftX() == obj.getLowerLeftX() and self.getLowerLeftY() == obj.getLowerLeftY() and self.getUpperRightX() == obj.getUpperRightX() and self.getUpperRightY() == obj.getUpperRightY()

    def setLowerLeftX(self, lowerLeftX):
        """
        Class method to set lowerLeftX of Rectangle.

        Parameters:
            lowerLeftX (int): x coordinate of the lower left point of Rectagle
        """
        self.lowerLeftX = lowerLeftX

    def setLowerLeftY(self, lowerLeftY):
        """
        Class method to set lowerLeftY of Rectangle.

        Parameters:
            lowerLeftY (int): y coordinate of the lower left point of Rectagle
        """
        self.lowerLeftY = lowerLeftY

    def setUpperRightX(self, upperRightX):
        """
        Class method to set upperRightX of Rectangle.

        Parameters:
            upperRightX (int): x coordinate of the upper right point of Rectagle
        """
        self.upperRightX = upperRightX

    def setUpperRightY(self, upperRightY):
        """
        Class method to set upperRightY of Rectangle.

        Parameters:
            upperRightY (int): y coordinate of the upper right point of Rectagle
        """
        self.upperRightY = upperRightY

    def getLowerLeftX(self):
        """
        Class method to return lowerLeftX of Rectangle.

        Returns:
            lowerLeftX (int): x coordinate of the lower left point of Rectagle
        """
        return float(self.lowerLeftX)

    def getLowerLeftY(self):
        """
        Class method to return lowerLeftY of Rectangle.

        Returns:
            lowerLeftY (int): y coordinate of the lower left point of Rectagle
        """
        return float(self.lowerLeftY)

    def getUpperRightX(self):
        """
        Class method to return upperRightX of Rectangle.

        Returns:
            upperRightX (int): x coordinate of the upper right point of Rectagle
        """
        return float(self.upperRightX)

    def getUpperRightY(self):
        """
        Class method to return upperRightY of Rectangle.

        Returns:
            upperRightY (int): y coordinate of the upper right point of Rectagle
        """
        return float(self.upperRightY)

    def getArea(self):
        """
        Method to compute the area of Rectangle.

        Returns:
            area: Area of rectangle.
        """
        length = self.getUpperRightX() - self.getLowerLeftX()
        width = self.getUpperRightY() - self.getLowerLeftY()
        area = length*width
        return area

class Ellipse:
    """
    This class store information about an Ellipse and returns important properties of Ellipse.

    Attributes:
        focalPoint1 (Point): Focal Point 1 of Ellipse
        focalPoint2 (Point): Focal Point 2 of Ellipse
        width (float): width of the Ellipse.
    """
    def __init__(self, focalPoint1, focalPoint2, width):
        """
        Constructor for Ellipse class.

        Parameters:
            focalPoint1 (Point): Focal Point 1 of Ellipse
            focalPoint2 (Point): Focal Point 2 of Ellipse
            width (float): width of the Ellipse.
        """
        self.focalPoint1 = focalPoint1
        self.focalPoint2 = focalPoint2
        self.width = width

    def __str__(self):
        """
        String repesentation for Ellipse.

        Returns:
            st: String represntation of Ellipse.
        """
        st = "Focal Point 1: {}\n"\
            "Focal Point 2: {}\n"\
            "Width: {}\n"\
            "Major Axis: {}\n"\
            "Minor Axis: {}\n"\
            "Area: {}\n"\
            "Circumference: {}\n".format(self.focalPoint1, self.focalPoint2, self.width, self.getMajorAxis(), self.getMinorAxis(), self.getArea(), self.getCircumference())
        return st

    def setFocalPoint1(self, focalPoint1):
        """
        Class method to set focalPoint1 of Ellipse.

        Parameters:
            focalPoint1 (Point): Focal Point 1 of Ellipse
        """
        self.focalPoint1 = focalPoint1

    def setFocalPoint2(self, focalPoint2):
        """
        Class method to set focalPoint2 of Ellipse.

        Parameters:
            focalPoint2 (Point): Focal Point 2 of Ellipse
        """
        self.focalPoint2 = focalPoint2

    def setWidth(self, width):
        """
        Class method to set width of Ellipse.

        Parameters:
            width (float): width of the Ellipse.
        """
        self.width = width

    def getFocalPoint1(self):
        """
        Class method to return focalPoint1 of Ellipse.

        Returns:
            focalPoint1 (Point): Focal Point 1 of Ellipse
        """
        return self.focalPoint1

    def getFocalPoint2(self):
        """
        Class method to return focalPoint2 of Ellipse.

        Returns:
            focalPoint2 (Point): Focal Point 2 of Ellipse
        """
        return self.focalPoint2

    def getWidth(self):
        """
        Class method to return width of Ellipse.

        Returns:
            width (float): width of the Ellipse.
        """
        return self.width

    def getDistanceBetweenFoci(self):
        """
        Calculate and return the distance between two focal points of Ellipse

        Returns:
            getDistanceBetweenFoci (float): width of the Ellipse.
        """
        distanceBetweenFoci = self.focalPoint1.getDistanceTo(self.focalPoint2)
        return distanceBetweenFoci

    def getMajorAxis(self):
        """
        Return the length of Major axis of Ellipse

        Returns:
            majorAxis (float): Length of Major Axis of the Ellipse.
        """
        majorAxis = self.width
        return majorAxis

    def getMinorAxis(self):
        """
        Calculate and Return the length of Minor axis of Ellipse

        Returns:
            minorAxis (float): Length of Minor Axis of the Ellipse.
        """
        minorAxis = round((sqrt(((self.getMajorAxis()/2)**2) - ((self.getDistanceBetweenFoci()/2)**2)))*2, 4)
        return minorAxis

    def getArea(self):
        """
        Calculate and Return the area of Ellipse

        Returns:
            area (float): Area of the Ellipse.
        """
        area = round(pi*(self.getMajorAxis()/2)*(self.getMinorAxis()/2), 4)
        return area

    def getCircumference(self):
        """
        Calculate and Return the circumference of Ellipse

        Returns:
            circumference (float): Circumference of the Ellipse.
        """
        circumference = pi*((3*((self.getMajorAxis()/2) + (self.getMinorAxis()/2))) - (sqrt((3*(self.getMajorAxis()/2) + (self.getMinorAxis()/2))* (3*(self.getMinorAxis()/2) + (self.getMajorAxis()/2)))))
        return round(circumference, 4)
