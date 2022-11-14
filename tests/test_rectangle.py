from src.Rectangle import Rectangle


def test_area():
    rectangle = Rectangle(2, 4)
    assert rectangle.area == 9
    

def test_perimeter():
    rectangle = Rectangle(2, 4)
    assert rectangle.perimeter == 16
