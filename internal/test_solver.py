import unittest
from unittest import TestCase

import numpy as np
from solver import solve_by_backtracking


class MyTestCase(unittest.TestCase):
    def test_solve_sudoku_by_backtracking_normal(self):
        input = np.array(
            [
                [1, 2, 3, 4, 5, 6, 0, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [6, 7, 8, 0, 1, 2, 3, 4, 5],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [9, 1, 2, 3, 4, 5, 6, 7, 0],
            ],
            dtype=np.int32,
        )
        got = solve_by_backtracking(input)
        want = np.array(
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [9, 1, 2, 3, 4, 5, 6, 7, 8],
            ],
            dtype=np.int32,
        )
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_no_change(self):
        input = np.array(
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [9, 1, 2, 3, 4, 5, 6, 7, 8],
            ],
            dtype=np.int32,
        )
        got = solve_by_backtracking(input)
        want = input
        assert (got == want).all()

    #
    # def test_solve_sudoku_by_backtracking_with_detection_error(self):
    #     input = np.array(
    #         [
    #             [1, 2, 3, 4, 5, 6, 0, 8, 9],
    #             [2, 3, 4, 5, 6, 7, 8, 9, 1],
    #             [3, 4, 5, 6, 7, 8, 4, 1, 2],  # 7th 4 is 9
    #             [4, 5, 6, 7, 8, 9, 1, 2, 3],
    #             [5, 6, 7, 8, 9, 1, 2, 3, 4],
    #             [6, 7, 4, 0, 1, 2, 3, 4, 5],  # 3rd 4 is 9
    #             [7, 8, 9, 1, 2, 3, 4, 5, 6],
    #             [8, 9, 1, 2, 3, 4, 5, 6, 7],
    #             [9, 1, 2, 3, 4, 5, 6, 7, 0],
    #         ],
    #         dtype=np.int32,
    #     )
    #
    # got = solve_by_backtracking(input)
    # want = np.array(
    #     [
    #         [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #         [2, 3, 4, 5, 6, 7, 8, 9, 1],
    #         [3, 4, 5, 6, 7, 8, 9, 1, 2],
    #         [4, 5, 6, 7, 8, 9, 1, 2, 3],
    #         [5, 6, 7, 8, 9, 1, 2, 3, 4],
    #         [6, 7, 8, 9, 1, 2, 3, 4, 5],
    #         [7, 8, 9, 1, 2, 3, 4, 5, 6],
    #         [8, 9, 1, 2, 3, 4, 5, 6, 7],
    #         [9, 1, 2, 3, 4, 5, 6, 7, 8],
    #     ],
    #     dtype=np.int32,
    # )
    # assert (got == want).all()


if __name__ == "__main__":
    unittest.main()
