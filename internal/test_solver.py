import unittest
from unittest import TestCase

import numpy as np
from solver import SudokuSolver


class MyTestCase(unittest.TestCase):
    # def test_find_and_suggest_valid_grids(self):
    #     input = np.array(
    #         [
    #             [2, 3, 5, 7, 9, 1, 6, 4, 8],
    #             [1, 8, 9, 4, 2, 8, 7, 5, 3],  # 2nd 8 is truly 6
    #             [7, 0, 8, 6, 0, 5, 9, 2, 1],
    #             [3, 9, 6, 2, 7, 4, 8, 1, 5],
    #             [5, 2, 1, 3, 8, 9, 4, 0, 7],
    #             [4, 8, 7, 1, 0, 6, 3, 9, 2],
    #             [8, 0, 3, 9, 6, 2, 1, 7, 4],
    #             [9, 7, 4, 0, 1, 3, 2, 8, 6],
    #             [6, 1, 2, 8, 4, 7, 5, 3, 9],
    #         ],
    #         dtype=np.int32,
    #     )
    #     solver = SudokuSolver()
    #     got = solver.find_and_suggest_valid_grids(input)
    #     want = np.array(
    #         [
    #             [
    #                 [2, 3, 5, 7, 9, 1, 6, 4, 8],
    #                 [1, 6, 9, 4, 2, 8, 7, 5, 3],
    #                 [7, 0, 8, 6, 0, 5, 9, 2, 1],
    #                 [3, 9, 6, 2, 7, 4, 8, 1, 5],
    #                 [5, 2, 1, 3, 8, 9, 4, 0, 7],
    #                 [4, 8, 7, 1, 0, 6, 3, 9, 2],
    #                 [8, 0, 3, 9, 6, 2, 1, 7, 4],
    #                 [9, 7, 4, 0, 1, 3, 2, 8, 6],
    #                 [6, 1, 2, 8, 4, 7, 5, 3, 9],
    #             ],
    #             [
    #                 [2, 3, 5, 7, 9, 1, 6, 4, 8],
    #                 [1, 8, 9, 4, 2, 8, 7, 5, 3],
    #                 [7, 0, 8, 6, 0, 5, 9, 2, 1],
    #                 [3, 9, 6, 2, 7, 4, 8, 1, 5],
    #                 [5, 2, 1, 3, 8, 9, 4, 0, 7],
    #                 [4, 8, 7, 1, 0, 6, 3, 9, 2],
    #                 [8, 0, 3, 9, 5, 2, 1, 7, 4],
    #                 [9, 7, 4, 0, 1, 3, 2, 8, 6],
    #                 [6, 1, 2, 8, 4, 7, 5, 3, 9],
    #             ],
    #         ],
    #         dtype=np.int32,
    #     )
    #     print(got.shape)
    #     assert (got == want).all()

    def test_find_and_suggest_valid_grids_no_change(self):
        input = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 0, 8, 6, 0, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 0, 7],
                [4, 8, 7, 1, 0, 6, 3, 9, 2],
                [8, 0, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 0, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=np.int32,
        )
        solver = SudokuSolver()
        got = solver.find_and_suggest_valid_grids(input)
        want = np.array(
            [
                [
                    [2, 3, 5, 7, 9, 1, 6, 4, 8],
                    [1, 6, 9, 4, 2, 8, 7, 5, 3],
                    [7, 0, 8, 6, 0, 5, 9, 2, 1],
                    [3, 9, 6, 2, 7, 4, 8, 1, 5],
                    [5, 2, 1, 3, 8, 9, 4, 0, 7],
                    [4, 8, 7, 1, 0, 6, 3, 9, 2],
                    [8, 0, 3, 9, 6, 2, 1, 7, 4],
                    [9, 7, 4, 0, 1, 3, 2, 8, 6],
                    [6, 1, 2, 8, 4, 7, 5, 3, 9],
                ],
            ],
            dtype=np.int32,
        )
        print(got.shape)
        assert (got == want).all()

    def test_is_valid_as_sudoku(self):
        input = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 8, 9, 4, 2, 8, 7, 5, 3],  # 2nd 8 is truly 6
                [7, 0, 8, 6, 0, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 0, 7],
                [4, 8, 7, 1, 0, 6, 3, 9, 2],
                [8, 0, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 0, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=np.int32,
        )
        solver = SudokuSolver()
        got = solver.is_valid_as_sudoku(input)
        assert got == False

    def test_is_valid_as_sudoku_real_data(self):
        input = np.array(
            [
                [0, 0, 0, 2, 0, 0, 0, 0, 0],
                [6, 9, 5, 0, 0, 8, 2, 4, 3],
                [0, 0, 2, 5, 6, 0, 1, 0, 0],
                [5, 0, 6, 0, 0, 2, 0, 0, 1],
                [0, 0, 9, 4, 8, 5, 6, 0, 2],
                [0, 8, 0, 6, 1, 0, 4, 5, 0],
                [0, 0, 0, 9, 0, 3, 8, 0, 4],
                [3, 2, 0, 0, 4, 6, 9, 0, 5],
                [0, 0, 4, 8, 0, 1, 0, 2, 0],
            ],
            dtype=np.int32,
        )
        solver = SudokuSolver()
        got = solver.is_valid_as_sudoku(input)
        assert got == True

    def test_is_valid_as_sudoku_real_data2(self):
        input = np.array(
            [
                [0, 0, 0, 2, 0, 0, 0, 0, 0],
                [6, 9, 5, 0, 0, 3, 2, 1, 3],
                [0, 0, 2, 5, 6, 0, 1, 0, 0],
                [3, 0, 6, 0, 0, 2, 0, 0, 1],
                [0, 0, 3, 1, 3, 3, 6, 0, 2],
                [0, 8, 0, 6, 1, 0, 1, 3, 0],
                [0, 0, 0, 3, 0, 3, 3, 0, 1],
                [6, 2, 0, 0, 1, 6, 9, 0, 3],
                [0, 0, 4, 6, 0, 1, 0, 4, 0],
            ],
            dtype=np.int32,
        )
        solver = SudokuSolver()
        got = solver.is_valid_as_sudoku(input)
        assert got == False

    def test_get_subgrid(self):
        arg1 = np.array(
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
            ],
            dtype=int,
        )
        solver = SudokuSolver()
        got = solver.get_subgrid(arg1, 4, 2)
        want = np.array(
            [
                [0, 0, 0],
                [0, 2, 0],
                [0, 0, 0],
            ],
            dtype=int,
        )
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_normal(self):
        input = np.array(
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
            ],
            dtype=int,
        )
        solver = SudokuSolver()
        got = solver.solve_by_backtracking(input)
        want = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 4, 8, 6, 3, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 6, 7],
                [4, 8, 7, 1, 5, 6, 3, 9, 2],
                [8, 5, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 5, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=int,
        )
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"

    def test_solve_sudoku_by_backtracking_no_change(self):
        input = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 4, 8, 6, 3, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 6, 7],
                [4, 8, 7, 1, 5, 6, 3, 9, 2],
                [8, 5, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 5, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=np.int32,
        )
        solver = SudokuSolver()
        got = solver.solve_by_backtracking(input)
        want = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 4, 8, 6, 3, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 6, 7],
                [4, 8, 7, 1, 5, 6, 3, 9, 2],
                [8, 5, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 5, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=int,
        )
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_with_correction(self):
        input = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 9, 9, 4, 2, 8, 7, 5, 3],  # 2nd 9 is truly 6
                [7, 0, 8, 6, 0, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 0, 1, 3, 8, 9, 4, 0, 7],
                [4, 8, 7, 1, 0, 6, 3, 9, 2],
                [8, 0, 3, 9, 6, 2, 1, 0, 4],
                [9, 7, 4, 0, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 0, 9],
            ],
            dtype=np.int32,
        )

        want = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 4, 8, 6, 3, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 6, 7],
                [4, 8, 7, 1, 5, 6, 3, 9, 2],
                [8, 5, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 5, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=int,
        )

        solver = SudokuSolver()
        got = solver.solve_by_backtracking_with_correction(input)
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_with_correction_normal(self):
        input = np.array(
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
            ],
            dtype=int,
        )
        solver = SudokuSolver()
        got = solver.solve_by_backtracking_with_correction(input)
        want = np.array(
            [
                [2, 3, 5, 7, 9, 1, 6, 4, 8],
                [1, 6, 9, 4, 2, 8, 7, 5, 3],
                [7, 4, 8, 6, 3, 5, 9, 2, 1],
                [3, 9, 6, 2, 7, 4, 8, 1, 5],
                [5, 2, 1, 3, 8, 9, 4, 6, 7],
                [4, 8, 7, 1, 5, 6, 3, 9, 2],
                [8, 5, 3, 9, 6, 2, 1, 7, 4],
                [9, 7, 4, 5, 1, 3, 2, 8, 6],
                [6, 1, 2, 8, 4, 7, 5, 3, 9],
            ],
            dtype=int,
        )
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_with_correction_norma2(self):
        input = np.array(
            [
                [0, 0, 0, 1, 0, 0, 8, 0, 9],
                [3, 0, 0, 0, 0, 4, 1, 0, 7],
                [0, 1, 9, 0, 7, 0, 0, 0, 0],
                [0, 0, 5, 3, 2, 1, 9, 0, 8],
                [9, 3, 0, 4, 0, 8, 0, 1, 2],
                [0, 8, 0, 0, 6, 0, 0, 0, 5],
                [6, 0, 1, 5, 4, 7, 0, 8, 0],
                [2, 0, 0, 0, 1, 3, 5, 9, 4],
                [5, 0, 3, 0, 0, 0, 0, 6, 1],
            ],
            dtype=int,
        )
        solver = SudokuSolver()
        got = solver.solve_by_backtracking_with_correction(input)
        want = np.array(
            [
                [7, 5, 4, 1, 3, 6, 8, 2, 9],
                [3, 2, 6, 9, 8, 4, 1, 5, 7],
                [8, 1, 9, 2, 7, 5, 4, 3, 6],
                [4, 6, 5, 3, 2, 1, 9, 7, 8],
                [9, 3, 7, 4, 5, 8, 6, 1, 2],
                [1, 8, 2, 7, 6, 9, 3, 4, 5],
                [6, 9, 1, 5, 4, 7, 2, 8, 3],
                [2, 7, 8, 6, 1, 3, 5, 9, 4],
                [5, 4, 3, 8, 9, 2, 7, 6, 1],
            ],
            dtype=int,
        )
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()

    # def test_solve_sudoku_by_backtracking_with_real_data(self):
    #     input = np.array(
    #         [
    #             [0, 3, 0, 4, 0, 0, 0, 7, 9],
    #             [0, 4, 0, 0, 0, 0, 3, 0, 0],
    #             [6, 7, 1, 0, 8, 0, 2, 0, 0],
    #             [0, 5, 6, 1, 0, 0, 0, 0, 7],
    #             [0, 9, 0, 0, 4, 3, 5, 3, 0],
    #             [0, 2, 0, 0, 0, 0, 8, 3, 6],
    #             [4, 0, 5, 0, 0, 0, 0, 9, 3],
    #             [7, 5, 3, 5, 0, 4, 0, 3, 6],
    #             [9, 0, 0, 7, 3, 3, 9, 0, 5],
    #         ],
    #         dtype=np.int32,
    #     )
    #
    #     # # correct
    #     # input = np.array(
    #     #     [
    #     #         [0, 3, 0, 4, 0, 0, 0, 7, 9],
    #     #         [0, 4, 0, 0, 0, 0, 3, 0, 0],
    #     #         [6, 7, 1, 0, 8, 0, 2, 0, 0],
    #     #         [0, 5, 6, 1, 0, 0, 0, 0, 7],
    #     #         [0, 9, 0, 0, 4, 3, 5, "1", 0],
    #     #         [0, 2, 0, 0, 0, 0, 8, 3, 6],
    #     #         [4, 0, 5, 0, 0, 0, 0, 9, 3],
    #     #         [7, "6", 3, 5, 0, 4, 0, "2", "8"],
    #     #         [9, 0, 0, 7, 3, "1", "4", 0, 5],
    #     #     ],
    #     #     dtype=np.int32,
    #     # )
    #     want = np.array(
    #         [
    #             [2, 3, 8, 4, 1, 5, 6, 7, 9],
    #             [5, 4, 9, 2, 7, 6, 3, 8, 1],
    #             [6, 7, 1, 3, 8, 9, 2, 5, 4],
    #             [3, 5, 6, 1, 2, 8, 9, 4, 7],
    #             [8, 9, 7, 6, 4, 3, 5, 1, 2],
    #             [1, 2, 4, 9, 5, 7, 8, 3, 6],
    #             [4, 1, 5, 8, 6, 2, 7, 9, 3],
    #             [7, 6, 3, 5, 9, 4, 1, 2, 8],
    #             [9, 8, 2, 7, 3, 1, 4, 6, 5],
    #         ],
    #         dtype=np.int32,
    #     )
    #     solver = SudokuSolver()
    #     got = solver.solve_by_backtracking(input)
    #     # print("answer:", got)
    #     assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
    #     assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
    #     assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
    #     assert (
    #         got.shape[0] == 9 and got.shape[1] == 9
    #     ), "Size of the NumPy array must be 9x9!"
    #     assert (got == want).all()


if __name__ == "__main__":
    unittest.main()
