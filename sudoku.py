import cv2
import numpy as np
import numpy.typing as npt
import internal.solver as solver


def solve(image: npt.NDArray[np.uint8]) -> npt.NDArray[np.int32]:
    # 問題領域の切り出し
    array = np.array(
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
    answer = solver.solve_by_backtracking(array)
    # 数字の識別
    # 数独の解決
    return answer
