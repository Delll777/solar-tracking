import os
import time
from datetime import date

from otsu import get_coordinates
from displacement_sun import displacement_sun


def diameter_arc_seconds(day):
    return 1920


def get_files(folder):
    path = folder
    file_list = os.listdir(path)
    full_list = [os.path.join(path, i) for i in file_list]
    time_sorted_list = sorted(full_list, key=os.path.getctime)

    return time_sorted_list


def write_json(file_name, data):  
    """
    Записывает данные в файл в формате json.
    :param file_name: Путь к файлу
    :param data: Данные
    """
    import json
    import os

        directories = file_name.split("/")[:-1]
    path = ""
    for directory in directories:
        path = path + directory + "/"
        if os.path.exists(path):
            if os.path.isdir(path):
                pass
            else:
                os.mkdir(path)
        else:
            os.mkdir(path)

        with open(file_name, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    folder = "images"
    files = get_files(folder)
    coords = []
    diameters = []
    for file in files:
        coordinates = get_coordinates(file)
        diameters.append(diameter_arc_seconds(date.today()))
        coords.append(coordinates)
    results = []
    for i in range(len(files)):
        if i + 1 < len(files):
            displacement = displacement_sun(coords[i], coords[i + 1], diameters[i], diameters[i + 1])
            results.append(
                {
                    "file1": files[i],
                    "file2": files[i + 1],
                    "displacement": displacement
                }
            )
    file_name = f"displacement_{int(time.time())}.json"
    write_json(file_name, results)


if __name__ == '__main__':
    main()
