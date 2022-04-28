import os
import random
import time

import numpy as np
import cv2
from PIL import Image


def generation_image():
    """
    Создает тестовое изображение в папке test.
    """
    output_folder = "test"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    width = 1920
    height = 1080

    min_radius = 100
    max_radius = 450

    # Создание изображения
    img = np.zeros((height, width, 3), np.uint8)

    min_height = 50
    max_height = height - 50
    min_width = 50
    max_width = width - 50

    radius = random.randint(min_radius, max_radius)

    min_height += radius
    max_height -= radius

    center_y = random.randint(min_height, max_height)

    min_width += radius
    max_width -= radius

    center_x = random.randint(min_width, max_width)
    coordinates = (
        (center_x - radius, center_y - radius),
        (center_x + radius, center_y + radius)
    )
    t = int(time.time())
    file_name = f"{t}test_{coordinates[0][0]}_{coordinates[0][1]}_{coordinates[1][0]}_{coordinates[1][1]}_{center_x}_{center_y}.tiff"
    file_path = os.path.join("test", file_name)

    # Создание градиентного круга
 
    color1 = random.randint(200, 255)
    r1 = color1
    g1 = color1
    b1 = color1

        color2 = random.randint(50, 180)
    r2 = color2
    g2 = color2
    b2 = color2

       d_r = r1 - r2
    d_g = g1 - g2
    d_b = b1 - b2

    s_r = int(radius / d_r)
    s_r = 1 if s_r == 0 else s_r
    s_g = int(radius / d_g)
    s_g = 1 if s_g == 0 else s_g
    s_b = int(radius / d_b)
    s_b = 1 if s_b == 0 else s_b

        for i in range(radius):
        cv2.circle(img, (center_x, center_y), radius - i, (b2, g2, r2), -1)
        if i % s_r == 0:
            r2 += 1
        if i % s_g == 0:
            g2 += 1
        if i % s_b == 0:
            b2 += 1

    cv2.imwrite(file_path, img)

    im1 = Image.open(file_path)
    im2 = Image.open("shum.png")
    mask = Image.open("shum.png").convert("L")

    im1.paste(im2, mask=mask)
    im1.save(file_path)

    im1.close()
    im2.close()

    img = cv2.imread(file_path)
    cv2.rectangle(img, (1050, 0), (1100, 1080), (0, 0, 0), -1)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    cv2.imwrite(file_path, img)


if __name__ == '__main__':
    count = 900
    for i in range(count):
        generation_image()
        print(f"{i+1}/{count}")
