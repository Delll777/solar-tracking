def get_diameter(coordinates):
    """
    Находит диаметр по оси Y.
    :param coordinates: Координаты на снимке ((лево, верх), (право, низ), (центр x, центр y)),
                        например, ((773, 242), (1413, 884), (1093, 563));
    :return: диаметр в пикселях.
    """
    diameter = coordinates[1][1] - coordinates[0][1]
    return diameter


def to_arc_seconds(value, ratio):
    """
    Переводит значение в угловые секунды.
    :param value: значение;
    :param ratio: соотношение;
    :return: значение в угловые секунды.
    """
    return int(value * ratio)


def displacement_sun(coordinates1, coordinates2, diameter_arc_seconds1, diameter_arc_seconds2):
    """
    Рассчитывает смещение в угловых секундах.
    :param coordinates1: Координаты на первом снимке ((лево, верх), (право, низ), (центр x, центр y)),
                         например, ((773, 242), (1413, 884), (1093, 563));
    :param coordinates2: Координаты на втором снимке ((лево, верх), (право, низ), (центр x, центр y)),
                         например, ((1003, 282), (1648, 924), (1325, 603));
    :param diameter_arc_seconds1: диаметр солнца в угловых секундах в момент снятия первого снимка;
    :param diameter_arc_seconds2: диаметр солнца в угловых секундах в момент снятия второго снимка;
    :return: смещение в угловых секундах, например, (694, 120).
    """
    diameter1 = get_diameter(coordinates1)
    ratio1 = diameter_arc_seconds1 / diameter1
    c1x, c1y = coordinates1[2]
    c1x, c1y = to_arc_seconds(c1x, ratio1), to_arc_seconds(c1y, ratio1)
    diameter2 = get_diameter(coordinates2)
    ratio2 = diameter_arc_seconds2 / diameter2
    c2x, c2y = coordinates2[2]
    c2x, c2y = to_arc_seconds(c2x, ratio2), to_arc_seconds(c2y, ratio2)
    return c2x - c1x, c2y - c1y


def main():
    displacement_sun(
        ((773, 242), (1413, 884), (1093, 563)),
        ((1003, 282), (1648, 924), (1325, 603)),
        1920,
        1920
    )


if __name__ == '__main__':
    main()
