"""
"""


class Figure:
    """
    базовый класс фигуры
    """
    def __init__(self, args):
        self.lines = args
        self.name = None
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        """
        расчет площади
        """
        return 0

    def get_perimeter(self):
        """
        расчет периметра
        """
        return 0

    def add_area(self, obj):
        """
        Сумма площадей текущей фигуры и переданной
        """
        if not isinstance(obj, Figure):
            raise ValueError("Вы редиска")

        return round(self.area + obj.area, 3)
