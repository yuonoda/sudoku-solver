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
    grid = image_handler.detect_numbers(clipped_images)
    print("recognized grid=", grid)

    # 数独の解決
    s = SudokuSolver()
    suggested_grids = s.find_and_suggest_valid_grids(grid)
    answer = np.zeros((9, 9), dtype=np.int32)
    for grid in suggested_grids:
        print("suggested_grid:", grid)
        got = s.solve_by_backtracking(grid)

        # すべてゼロでない時は、スキップ
        if np.all(got):
            answer = got
            continue

    print("answer:", answer)
    return answer
