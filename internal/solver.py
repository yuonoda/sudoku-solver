import numpy.typing as npt
import numpy as np


# solve_by_backtrackingはバックトラック法による数独の解答処理
def solve_by_backtracking(input: npt.NDArray) -> npt.NDArray[np.int32]:
    # npt.NDArrayのリストを作成
    stack = [input]
    i = 0
    while True:
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

        #  そのマスに入れられる数字を計算
        all_nums = set(range(1, 10))
        nums_in_arrays = set(row) | set(column)
        missing_nums = list(all_nums - nums_in_arrays)

        # 空マスに候補を入れた行列を追加
        for num in missing_nums:
            new_matrix = matrix.copy()
            new_matrix[i, j] = num
            stack.append(new_matrix)
            continue
