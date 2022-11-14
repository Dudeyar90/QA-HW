"""
"""
from math import pi
from .Figure import Figure


class Circle(Figure):
    """
    Фигура - круг
    """
    def __init__(self, *args):
        Figure.__init__(self, args)
        self.name = "сircle"

    def get_area(self):
        """
        расчет площади круга
        """
        return round(pi * (self.lines[0] ** 2), 3)

    def get_perimeter(self):
        """
        расчет длинны окружности
        """
        return round(2 * pi * self.lines[0], 3)
