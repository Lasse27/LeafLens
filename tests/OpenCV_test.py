import cv2 as cv
from unittest import TestCase
import os


class UUT(TestCase):
    # Test OpenCV.imread on .ico files
    def test_imread_ico(self):
        try:
            path: str = os.path.join(os.path.dirname(__file__), "ressources", "icon.ico")
            img = cv.imread(path)
            if img is None:
                raise Exception("Image couldn't be loaded")
        except Exception as e:
            self.fail(e)
