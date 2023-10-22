import unittest

import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn import metrics

from internal.image_handler import ImageHandler


class MyTestCase(unittest.TestCase):
    def test_clip_images(self):
        image_path = "../data/level1/sudoku_028.jpg"
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ih = ImageHandler()
        images = ih.clip_images(image)

        # 画像の表示
        # 9x9のグリッドを作り、各セルに画像をプロット
        fig, axs = plt.subplots(9, 9, figsize=(9, 9))
        axs = axs.flatten()
        for ax, cell in zip(axs, images):
            ax.imshow(cell, cmap="gray")  # BGRからRGBへ変換
            ax.axis("off")  # 軸の情報をオフにするRA
        plt.savefig("./output/clipped_images.png")

    def test_integration(self):
        filepath = "../data/level1/sudoku_028"
        image_path = filepath + ".jpg"
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ih = ImageHandler()
        cell_images = ih.clip_images(image)
        detected = ih.detect_numbers(cell_images)
        predicted = detected.flatten()

        textname = filepath + ".txt"
        correct_labels = np.loadtxt(textname, dtype=int)
        correct_labels_flat = correct_labels.flatten()

        # Accuracyを計算して表示
        print(metrics.classification_report(correct_labels_flat, predicted))

        # 画像と予測結果を並べて表示します
        # 行と列の数を設定
        n_rows = 9
        n_cols = 9

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(10, 6))

        # サブプロットを行と列にわたってループ
        for i in range(n_rows):
            for j in range(n_cols):
                idx = i * n_cols + j  # インデックスを計算
                ax = axes[i, j]  # 現在のサブプロットを取得

                # インデックスが画像の数以上になったら終了
                if idx >= len(cell_images):
                    break

                ax.imshow(cell_images[idx], cmap="gray")
                ax.set_title(f"Pred: {predicted[idx]}")
                ax.axis("off")

        plt.tight_layout()
        plt.savefig("./output/detected_numbers.png")


if __name__ == "__main__":
    unittest.main()

# %%
