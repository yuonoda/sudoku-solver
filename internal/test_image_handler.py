import unittest

import cv2
import matplotlib.pyplot as plt
import numpy as np
from pandas._typing import npt

from internal.image_handler import ImageHandler


class MyTestCase(unittest.TestCase):
    def test_load_image(self):
        #  画像の読み込み
        img = cv2.imread("./data/level1/sample.jpg", cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise IOError("Failed to load image: {:s}".format(filename))
        print(img.shape)

    def test_detect_numbers(self):
        filename = "../data/level1/sample.jpg"
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise IOError("Failed to load image: {:s}".format(filename))
        img
        got = ImageHandler().detect_numbers(img)
        want = np.array(
            [
                [0, 3, 5, 0, 9, 0, 0, 4, 8],
                [0, 0, 9, 0, 0, 8, 0, 0, 3],
                [0, 4, 0, 6, 0, 5, 0, 0, 1],
                [0, 0, 0, 0, 7, 4, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 6, 0],
                [0, 0, 0, 1, 5, 0, 0, 0, 0],
                [8, 0, 0, 9, 0, 2, 0, 7, 0],
                [9, 0, 0, 5, 0, 0, 2, 0, 0],
                [6, 1, 0, 0, 4, 0, 5, 3, 0],
            ]
        )
        assert (got == want).all()  # add assertion here


if __name__ == "__main__":
    unittest.main()
