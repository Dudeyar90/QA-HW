from src.Triangle import Triangle


def test_Triangle():
    triangle = Triangle(2,2,3)
    assert triangle.area == 12