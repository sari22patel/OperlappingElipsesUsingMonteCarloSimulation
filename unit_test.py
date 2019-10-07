from unittest import TestCase
import unittest
import ellipse
import area_of_overlap
import sys
import logging

logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class TestPointMethods(TestCase):

    def setUp(self):
        self.p1 = ellipse.Point(5, -1)
        self.p2 = ellipse.Point(-1, -1)

    def test_getDistanceTo(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Point.getDistanceTo")
        logging.getLogger().info(ellipse.Point.getDistanceTo.__doc__)
        logging.getLogger().info("Test getDistanceTo method of Point class.")
        self.assertEqual(self.p1.getDistanceTo(self.p2), 6.0, "Distance calcualted does not matches the expected Distance between two points.")
        logging.getLogger().info("Distance = {}\nExpected Distance = {}".format(self.p1.getDistanceTo(self.p2), 6.0))

    def tearDown(self):
        del self.p1
        del self.p2

class TestRectangleMethods(TestCase):

    def setUp(self):
        self.rect = ellipse.Rectangle(-1, 2, 5, 10)

    def test_getArea(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Rectangle.getArea")
        logging.getLogger().info(ellipse.Rectangle.getArea.__doc__)
        logging.getLogger().info("Test getArea method of Rectangle class.")
        self.assertEqual(self.rect.getArea(), 48.0, "Area calcualted does not matches the expected Area of the rectangle.")
        logging.getLogger().info("Area = {}\nExpected Area = {}".format(self.rect.getArea(), 48.0))

    def tearDown(self):
        del self.rect

class TestEllipseMethods(TestCase):

    def setUp(self):
        eclipse1FocalPoint1 = ellipse.Point(5, -1)
        eclipse1FocalPoint2 = ellipse.Point(-1, -1)
        self.e = ellipse.Ellipse(eclipse1FocalPoint1, eclipse1FocalPoint2, 10)

    def test_getMajorAxis(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Ellipse.getMajorAxis")
        logging.getLogger().info(ellipse.Ellipse.getMajorAxis.__doc__)
        logging.getLogger().info("Test getMajorAxis method of Ellipse class.")
        self.assertEqual(self.e.getMajorAxis(), 10, "Major Axis calcualted does not matches the expected Major Axis.")
        logging.getLogger().info("Major Axis = {}\nExpected Major Axis = {}".format(self.e.getMajorAxis(), 10))

    def test_getMinorAxis(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Ellipse.getMinorAxis")
        logging.getLogger().info(ellipse.Ellipse.getMinorAxis.__doc__)
        logging.getLogger().info("Test getMinorAxis method of Ellipse class.")
        self.assertEqual(self.e.getMinorAxis(), 8.0, "Minor Axis calcualted does not matches the expected Minor Axis. {}")
        logging.getLogger().info("Minor Axis = {}\nExpected Minor Axis = {}".format(self.e.getMinorAxis(), 8.0))

    def test_getArea(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Ellipse.getArea")
        logging.getLogger().info(ellipse.Ellipse.getArea.__doc__)
        logging.getLogger().info("Test getArea method of Ellipse class.")
        self.assertEqual(self.e.getArea(), 62.8319, "Area calcualted does not matches the expected area.")
        logging.getLogger().info("Area = {}\nExpected Area = {}".format(self.e.getArea(), 62.8319))

    def test_getCircumference(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nMethod Name: Ellipse.getCircumference")
        logging.getLogger().info(ellipse.Ellipse.getCircumference.__doc__)
        logging.getLogger().info("Test getCircumference method of Ellipse class.")
        self.assertEqual(self.e.getCircumference(), 28.3617, "Circumference calcualted does not matches the expected area.")
        logging.getLogger().info("Circumference = {}\nExpected Circumference = {}".format(self.e.getCircumference(), 28.3617))

    def tearDown(self):
        del self.e

class TestAreaOfOverlapMethod(TestCase):
    def setUp(self):
        eclipse1FocalPoint1 = ellipse.Point(-2.236, 0)
        eclipse1FocalPoint2 = ellipse.Point(2.236, 0)
        self.e1 = ellipse.Ellipse(eclipse1FocalPoint1, eclipse1FocalPoint2, 6)
        eclipse2FocalPoint1 = ellipse.Point(-1.8284, -0.5)
        eclipse2FocalPoint2 = ellipse.Point(3.8284, -0.5)
        self.e2 = ellipse.Ellipse(eclipse2FocalPoint1, eclipse2FocalPoint2, 6)
        self.testRect = ellipse.Rectangle(-8.236, -6, 8.236, 6)

    def test_getRectangle(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nFunction Name: getRectangle")
        logging.getLogger().info(area_of_overlap.getRectangle.__doc__)
        logging.getLogger().info("Test getRectangle function.")
        self.assertEqual(area_of_overlap.getRectangle(self.e1,self.e2), self.testRect, "The definition of rectangle returned does not matches the expected definition of rectangle.")
        logging.getLogger().info("Rectangle = {}\nExpected Rectangle = {}".format(area_of_overlap.getRectangle(self.e1,self.e2), self.testRect))

    def test_computeAreaOfOverlap(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nFunction Name: computeAreaOfOverlap")
        logging.getLogger().info(area_of_overlap.computeAreaOfOverlap.__doc__)
        logging.getLogger().info("Test computeAreaOfOverlap function.")
        self.assertTrue((area_of_overlap.computeAreaOfOverlap(self.e1, self.e2, self.testRect) - 8.05) < 1, "The area of overlap returned does not match the estimated area of overlap between ellipse e1 and e2.")
        logging.getLogger().info("Area of Overlap = {}\nEstimated Area of Overlap = {}".format(area_of_overlap.computeAreaOfOverlap(self.e1, self.e2, self.testRect), 8.05))

    def test_getAreaOfOverlap(self):
        stream_handler.stream = sys.stdout
        logging.getLogger().info("\nFunction Name: getAreaOfOverlap")
        logging.getLogger().info(area_of_overlap.getAreaOfOverlap.__doc__)
        logging.getLogger().info("Test getAreaOfOverlap function.")
        self.assertTrue((area_of_overlap.getAreaOfOverlap(self.e1, self.e2) - 8.05) < 1, "The area of overlap returned does not match the estimated area of overlap between ellipse e1 and e2.")
        logging.getLogger().info("Area of Overlap = {}\nEstimated Area of Overlap = {}".format(area_of_overlap.getAreaOfOverlap(self.e1, self.e2), 8.05))

    def tearDown(self):
        del self.e1
        del self.e2
        del self.testRect

if __name__ == '__main__':
    unittest.main()
