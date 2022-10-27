"""
"""
from .Figure import Figure


class Rectangle(Figure):
    """
    Фигура - прямоугольник
    """
    def __init__(self, *args):
        Figure.__init__(self, args)
        self.name = "rectangle"

    def get_area(self):
        """
        расчет площади прямоугольника
        """
        return self.lines[0] * self.lines[1]

    def get_perimeter(self):
        """
        расчет периметра прямоугольника
        """
        return (self.lines[0] + self.lines[1]) * 2
