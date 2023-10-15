import gzip
import pickle

import cv2
import numpy.typing as npt
import numpy as np


class ImageHandler:
    def __init__(self):
        # モデル読み込み
        # TODO パスを動的にする
        with gzip.open("./internal/clf_svm.pkl.gz", "rb") as f:
            self.clf = pickle.load(f)
        # TODO エラー処理

    def clip_images(self, img: npt.NDArray[np.uint8]) -> npt.NDArray:
        # 二値データに変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

        # 輪郭を見つける
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # 各マス目の画像を抽出し、リストに保存
        cell_images = []
        stepx = w // 9
        stepy = h // 9
        trim_size_x = stepx // 7
        trim_size_y = stepy // 7
        EMPTY_THRESHOLD = 200
        for i in range(9):
            for j in range(9):
                cell = gray[
                    y + i * stepy + trim_size_y : y + (i + 1) * stepy - trim_size_y,
                    x + j * stepx + trim_size_x : x + (j + 1) * stepx - trim_size_x,
                ]
                resized_cell = cv2.resize(cell, (60, 60), interpolation=cv2.INTER_CUBIC)
                normalized = resized_cell / 255.0
                cell_images.append(normalized)
        return np.array(cell_images)

    def detect_numbers(self, image: npt.NDArray[np.uint8]) -> npt.NDArray:
        model_input = np.array(image)
        model_input_2d = model_input.reshape(model_input.shape[0], -1)
        predicted = self.clf.predict(model_input_2d)
        return predicted.reshape((9, 9))
