from turtle import circle
from src.Circle import Circle


def test_area():
    circle = Circle(4)
    assert circle.area == 19

def test_perimetr():
    circle = Circle(5)
    assert circle.perimeter != 9