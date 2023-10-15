import copy

import numpy.typing as npt
import numpy as np


class SudokuSolver:
    def __init__(self):
        self.possible_number_map = {8: [2, 3, 6], 6: [2]}
        pass

    def is_valid_unit(self, unit):
        """
        Check if the unit (row/column/block) is valid.
        """
        unit = [num for num in unit if num != 0]  # Remove zeros (empty cells)
        return len(unit) == len(set(unit))  # Check for duplicates

    def is_move_valid(self, sudoku, row, col, num):
        """
        Check if placing `num` at the position `(row, col)` is valid in `sudoku` grid.

        Parameters:
        - sudoku (np.array): 9x9 sudoku grid
        - row (int): target row index
        - col (int): target column index
        - num (int): number to check

        Returns:
        - bool: True if placing `num` at `(row, col)` is valid, otherwise False.
        """
        # Check the row
        if num in sudoku[row, :]:
            return False

        # Check the column
        if num in sudoku[:, col]:
            return False

        # Check the 3x3 block
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in sudoku[start_row : start_row + 3, start_col : start_col + 3]:
            return False

        return True

    def is_valid_as_sudoku(self, grid) -> bool:
        # Check rows and columns
        for i in range(9):
            if not self.is_valid_unit(grid[i]) or not self.is_valid_unit(
                [grid[j][i] for j in range(9)]
            ):
                return False

        # Check 3x3 blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_unit(
                    [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                ):
                    return False

        return True

    def find_and_suggest_valid_grids(self, grid) -> npt.NDArray[np.int32]:
        suggested_grids = []
        for i in range(9):
            for j in range(9):
                num = grid[i][j]
                if grid[i][j] != 0:  # このセルに数字が入っている場合
                    # 誤りの可能性がある数字は、他の数字に入れ替えて、有効なら提案する
                    possible_nums = self.possible_number_map.get(num, [])
                    for new_num in possible_nums:
                        if self.is_move_valid(grid, i, j, new_num):
                            new_grid = copy.deepcopy(grid)
                            new_grid[i][j] = new_num
                            suggested_grids.append(new_grid)

        return np.array(suggested_grids)

    def get_subgrid(self, grid: npt.NDArray, i, j) -> npt.NDArray[np.int32]:
        # 座標(i, j)が属する3x3の領域を見つける。
        # // は床関数を表し、整数の商を取得します。
        subgrid_row = i // 3
        subgrid_col = j // 3

        # スライスを用いて3x3の領域を取得します。
        # 開始インデックスは subgrid_row/col * 3 で、終了インデックスは 開始インデックス + 3 です。
        subgrid = grid[
            subgrid_row * 3 : subgrid_row * 3 + 3, subgrid_col * 3 : subgrid_col * 3 + 3
        ]
        return subgrid

    # solve_by_backtrackingはバックトラック法による数独の解答処理
    def solve_by_backtracking(self, input: npt.NDArray) -> npt.NDArray[np.int32]:
        # npt.NDArrayのリストを作成
        stack = [input]
        i = 0

        # スタックにデータがあるかぎり繰り返す
        count = 0
        while len(stack) > 0:
            # TODO: remove this
            # 流石に1万回やっても解けなかったら諦める
            if count > 10000:
                return np.zeros((9, 9), dtype=np.int32)
            count += 1

            # マスが全て埋まっていたら成功
            grid = stack.pop()
            if np.all(grid):
                return grid.astype(np.int32)

            # 最初の空マスを取得
            row = npt.NDArray
            column = npt.NDArray
            found = False
            for i in range(len(grid)):
                row = grid[i, :]
                for j in range(len(row)):
                    if row[j] == 0:
                        column = grid[:, j]
                        found = True
                        break
                if found:
                    break

            # サブグリッドを取得
            subgrid = self.get_subgrid(grid, i, j)
            nums_in_subgrid = np.unique(subgrid)

            #  そのマスに入れられる数字を計算
            all_nums = set(range(1, 10))
            used_nums = set(row) | set(column) | set(nums_in_subgrid)
            missing_nums = list(all_nums - used_nums)

            # 空マスに候補を入れた行列を追加
            for num in missing_nums:
                new_grid = grid.copy()
                new_grid[i, j] = num
                if self.is_valid_as_sudoku(new_grid) == False:
                    continue
                stack.append(new_grid)

        return np.zeros((9, 9), dtype=np.int32)
