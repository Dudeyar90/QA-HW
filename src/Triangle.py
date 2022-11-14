"""
"""
from .Figure import Figure


class Triangle(Figure):
    """
    Фигура - треугольник
    """
    def __init__(self, *args):
        Figure.__init__(self, args)
        self.name = "triangle"

    def get_area(self):
        """
        расчет площади треугольника
        """
        per = self.perimeter / 2
        return round((per * (per - self.lines[0]) * (per - self.lines[1]) * (per - self.lines[2])) ** 0.5, 3)

    def get_perimeter(self):
        """
        периметр треугольника
        """
        return sum(self.lines)
