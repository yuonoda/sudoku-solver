import unittest
from unittest import TestCase

import numpy as np
from solver import SudokuSolver


class MyTestCase(unittest.TestCase):
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
        want = input
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()

    def test_solve_sudoku_by_backtracking_with_detection_error(self):
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
        got = solver.solve_by_backtracking(input)
        assert isinstance(got, np.ndarray), "Return NumPy's NDArray!"
        assert got.dtype == np.int32, "Return NumPy array with int32 data type!"
        assert got.ndim == 2, "#dimensions of NumPy array must be 2!"
        assert (
            got.shape[0] == 9 and got.shape[1] == 9
        ), "Size of the NumPy array must be 9x9!"
        assert (got == want).all()


if __name__ == "__main__":
    unittest.main()
