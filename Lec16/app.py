"""
Стартовая точка программы
"""

#  Импортирование модулей из пакета c разделенной областью
from geometry import circle, rectangle, trianlge
# С совмещенной
from geometry.circle import perimeter

print("Circle area(10):", circle.area(10))
print("Rectangle perimeter(10,10):", rectangle.perimeter(10, 10))
print("Triangle perimeter(10,10,10):", trianlge.perimeter(10, 10, 10))