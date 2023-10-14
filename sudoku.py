import cv2
import numpy as np
import numpy.typing as npt
from internal.solver import SudokuSolver
from internal.image_handler import ImageHandler


def solve(image: npt.NDArray[np.uint8]) -> npt.NDArray[np.int32]:
    # 問題領域の切り出し
    image_handler = ImageHandler()
    clipped_images = image_handler.clip_images(image)
    # 数字の識別
    array = image_handler.detect_numbers(clipped_images)
    # 数独の解決
    s = SudokuSolver()
    answer = s.solve_by_backtracking(array)
    return answer
