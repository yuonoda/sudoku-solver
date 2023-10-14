import numpy.typing as npt
import numpy as np


class SudokuSolver:
    def __init__(self):
        pass

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
        while stack:
            # マスが全て埋まっていたら成功
            matrix = stack.pop()
            if np.all(matrix):
                return matrix

            # 　最初の空マスを取得
            row = npt.NDArray
            column = npt.NDArray
            found = False
            for i in range(len(matrix)):
                row = matrix[i, :]
                for j in range(len(row)):
                    if row[j] == 0:
                        column = matrix[:, j]
                        found = True
                        break
                if found:
                    break

            # サブグリッドを取得
            subgrid = self.get_subgrid(matrix, i, j)
            nums_in_subgrid = np.unique(subgrid)

            #  そのマスに入れられる数字を計算
            all_nums = set(range(1, 10))
            used_nums = set(row) | set(column) | set(nums_in_subgrid)
            missing_nums = list(all_nums - used_nums)

            # 空マスに候補を入れた行列を追加
            for num in missing_nums:
                new_matrix = matrix.copy()
                new_matrix[i, j] = num
                stack.append(new_matrix)
                continue
