import numpy.typing as npt
import numpy as np


# solve_by_backtrackingはバックトラック法による数独の解答処理
def solve_by_backtracking(input: npt.NDArray) -> npt.NDArray:
    stack = input
    i = 0
    while True:
        # マスが全て埋まっていたら成功
        if np.count_nonzero(stack == 0) == 0:
            return stack
        # 　最初の空マスを取得
        #  そのマスに入れられる数字を計算
        # そのマスに入れられる数字が一つだったらその数字を入れる

        if i > 100:
            break
        i += 1

    return np.zeros((9, 9), dtype=np.int32)
