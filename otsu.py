import cv2 as cv
import numpy as np


def get_coordinates(file_name, shadow_error=60):
    """
    Нахождение координат на изображение методом ОЦУ.
    :param file_name: Путь к файлу;
    :param shadow_error:погрешность тени.
    :return: Координаты на снимке ((лево, верх), (право, низ), (центр x, центр y)),
             например, ((812, 246), (1441, 876), (1126, 561));
    """
    img = cv.imread(file_name, 0)  

    blur = cv.GaussianBlur(img, (5, 5), 0)
    _, otsu_img = cv.threshold(
        blur,
        0,
        255,
        cv.THRESH_BINARY + cv.THRESH_OTSU
    ) 

    matrix = np.where(otsu_img == 255) 

    top, bottom = matrix[0].min(), matrix[0].max()  
    left, right = matrix[1].min(), matrix[1].max() 

    Y = list(matrix[1])
    diameter = (bottom - top)
    radius = int(diameter / 2)
    if Y.count(left) > shadow_error:
        left = right - diameter
    elif Y.count(right) > shadow_error:
        right = left + diameter

    center = right - radius, bottom - radius

    return (left, top), (right, bottom), center


if __name__ == '__main__':
    import os
    import time

    folder = "images"
    files = os.listdir(folder)
    print(len(files))
    t0 = time.time()
    for file in files:
        coordinates = get_coordinates(os.path.join(folder, file))
        # print(f"{file=}")
        # print(f"{coordinates=}")
    print(time.time() - t0)