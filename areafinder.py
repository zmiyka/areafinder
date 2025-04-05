import math

def calculate_cyrcle(radius):
    """Формула кола: π * (r * r)"""
    area = radius * 3.14 * 2
    return(area)

def calculate_parallelogram_area(side: float, height: float):
      """Обцислює площу паралелограма за стороною та висотою проведеною до неї"""
      return side * height

def calculate_free_triangle_area(side1, side2, side3):
    """Обцислює трикутника за трьома сторонами"""
    p = (side1 + side2 + side3)/2
    area = math.sqrt(p * (p - side1) * (p - side2) * (p -side3))
    return area
