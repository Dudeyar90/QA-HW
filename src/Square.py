"""
"""
from .Figure import Figure


class Square(Figure):
    """
    Фигура - квадрат
    """
    def __init__(self, *args):
        Figure.__init__(self, args)
        self.name = "square"

    def get_area(self):
        """
        расчет площади квадрата
        """
        return self.lines[0] ** 2

    def get_perimeter(self):
        """
        расчет периметра квадрата
        """
        return self.lines[0] * 4

