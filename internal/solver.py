import copy

import numpy.typing as npt
import numpy as np


class SudokuSolver:
    def __init__(self):
        self.possible_number_map = {8: [2, 3, 6], 6: [2, 8], 3: [1, 2], 5: [6], 9: [4]}
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
        if self.is_valid_as_sudoku(grid):
            return np.array([grid])

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

    def has_duplicates(self, array: list) -> bool:
        seen = set()
        for num in array:
            if num == 0:
                continue
            if num in seen:
                return True
            seen.add(num)
        return False

    def get_unique_and_duplicates(self, lst: list):
        seen = set()
        duplicates = set()
        unique = set()

        for num in lst:
            if num == 0:
                continue
            if num in seen:
                duplicates.add(num)
            else:
                unique.add(num)
                seen.add(num)

        return list(unique), list(duplicates)

    # solve_by_backtrackingはバックトラック法による数独の解答処理
    def solve_by_backtracking(self, input: npt.NDArray) -> npt.NDArray[np.int32]:
        # スタックにデータがあるかぎり繰り返す
        stack = [input]
        while len(stack) > 0:
            # マスが全て埋まっていて、有効な解答なら成功
            grid = stack.pop()
            if np.all(grid):
                if self.is_valid_as_sudoku(grid):
                    return grid.astype(np.int32)
                else:
                    continue

            # 最初の空マスを取得
            row = []
            column = []
            found = False
            i = 0
            j = 0
            for i in range(len(grid)):
                row = grid[i, :]
                for j in range(len(row)):
                    if row[j] == 0:
                        column = grid[:, j]
                        found = True
                        break
                if found:
                    break

            # ブロックを取得
            subgrid = self.get_subgrid(grid, i, j)
            nums_in_subgrid = np.unique(subgrid)

            #  そのマスに入れられる数字を計算
            all_nums = set(range(1, 10))
            uniq_row_nums, dup_row_nums = self.get_unique_and_duplicates(row)
            uniq_col_nums, dup_col_nums = self.get_unique_and_duplicates(column)
            uniq_block_nums, dup_block_nums = self.get_unique_and_duplicates(
                nums_in_subgrid
            )
            used_nums = set(uniq_col_nums) | set(uniq_row_nums) | set(uniq_block_nums)
            missing_nums = list(all_nums - used_nums)

            # 空マスに候補を入れたグリッドを追加
            new_grid = grid.copy()
            for missing_num in missing_nums:
                new_grid[i, j] = missing_num
                stack.append(new_grid)

            # 行の誤り訂正
            if len(dup_row_nums) > 0:
                for l in range(0, 9):
                    if l == j:
                        continue
                    original_num = new_grid[i, l]
                    if not original_num in dup_row_nums:
                        continue
                    possible_nums = self.possible_number_map.get(original_num, [])
                    for possible_num in possible_nums:
                        new_new_grid = new_grid.copy()
                        new_new_grid[i, l] = possible_num
                        stack.append(new_new_grid)

            # 列の誤り訂正
            if len(dup_col_nums) > 0:
                for k in range(0, 9):
                    if k == i:
                        continue
                    original_num = new_grid[k, j]
                    if not original_num in dup_col_nums:
                        continue
                    possible_nums = self.possible_number_map.get(original_num, [])
                    for possible_num in possible_nums:
                        new_new_grid = new_grid.copy()
                        new_new_grid[k, j] = possible_num
                        stack.append(new_new_grid)

            # ブロックの誤り訂正:
            if len(dup_block_nums) > 0:
                subgrid_start_row, subgrid_start_col = 3 * (i // 3), 3 * (j // 3)
                for k in range(subgrid_start_row, subgrid_start_row + 3):
                    for l in range(subgrid_start_col, subgrid_start_col + 3):
                        if k == i and l == j:
                            continue
                        original_num = new_grid[k, l]
                        if not original_num in dup_block_nums:
                            continue
                        possible_nums = self.possible_number_map.get(original_num, [])
                        for possible_num in possible_nums:
                            new_new_grid = new_grid.copy()
                            new_new_grid[k, l] = possible_num
                            stack.append(new_new_grid)

        return np.zeros((9, 9), dtype=np.int32)
