import numpy.typing as npt
import numpy as np


class ImageHandler:
    def detect_numbers(self, image: npt.NDArray[np.uint8]) -> npt.NDArray:
        return np.zeros((9, 9), dtype="int32")
