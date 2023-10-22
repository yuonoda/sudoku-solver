import gzip
import os
import pickle
from datetime import datetime

import cv2
import numpy.typing as npt
import numpy as np
import matplotlib.pyplot as plt


class ImageHandler:
    def __init__(self):
        # モデル読み込み
        current_script_path = os.path.abspath(__file__)
        current_script_dir = os.path.dirname(current_script_path)
        path = os.path.join(current_script_dir, "../internal/clf_svm_2.pkl.gz")
        with gzip.open(path, "rb") as f:
            self.clf = pickle.load(f)
        # TODO エラー処理

    def clip_images(self, img: npt.NDArray[np.uint8]) -> npt.NDArray:
        imgToShow = img.copy()
        # 白黒データに変換
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # ぼかし
        blurred = cv2.GaussianBlur(gray, (11, 11), 90)

        # 二値化
        _, thresh2 = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)

        # Canny法でエッジ検出
        canny = cv2.Canny(thresh2, 127, 200)

        # エッジ統合
        res = canny.copy()
        kerneal_size = 25
        res = cv2.dilate(canny, np.ones((kerneal_size, kerneal_size)))
        erode_kernel_size = 30
        res = cv2.erode(res, np.ones((erode_kernel_size, erode_kernel_size)))
        binary = res.copy()

        # 輪郭の外側を取得
        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # 輪郭の内側の座標を取得
        mask = np.zeros_like(binary)
        cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)
        inside_points = np.column_stack(np.where(mask == 255))

        for contour in contours:
            # 輪郭を近似
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 近似した輪郭が四角形であるか確認
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                cv2.drawContours(imgToShow, [approx], 0, (0, 255, 0), 2)  # 緑色で四角形の輪郭を描画
                x, y, w, h = cv2.boundingRect(approx)

        # # 画像を表示
        # plt.imshow(imgToShow, cmap="gray")
        # current_microsecond = datetime.datetime.now().microsecond
        # plt.savefig(f"{current_microsecond}.png")

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

                resized_cell = cv2.resize(cell, (30, 30), interpolation=cv2.INTER_CUBIC)
                np_image = np.array(resized_cell)
                _, thresh = cv2.threshold(np_image, 127, 255, cv2.THRESH_BINARY)
                normalized = thresh / 255.0
                cell_images.append(normalized)
        return np.array(cell_images)

    def detect_numbers(self, image: npt.NDArray[np.uint8]) -> npt.NDArray:
        model_input = np.array(image)
        model_input_2d = model_input.reshape(model_input.shape[0], -1)
        predicted = self.clf.predict(model_input_2d)
        return predicted.reshape((9, 9))
