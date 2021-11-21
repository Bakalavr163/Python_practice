# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
 
class Triangle(object):
    def __init__(self, a, b, c):
        # Данная функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        self.a = a
        self.b = b
        self.c = c
        # В соответствии с соседними координатами вычисляем длину стороны ab
        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.ca = sideLen(self.c, self.a)
 
    # Применим формулу Герона для вычесления площади треугольника 
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2
 
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ca))


    # Вычисляем высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.ab / 2)


    # Вычисляем периметр треугольника
    def perimeterTriangle(self):
        return self.ab + self.bc + self.ca
 
    
treygolnik1 = Triangle((5, 4), (8, 10), (1, 14))
 
print(treygolnik1.areaTriangle())
print(treygolnik1.heightTriangle())
print(treygolnik1.perimeterTriangle())

# Результат
26.999999999999986
8.049844718999239
25.540791295066924


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3,x4 ,y4):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.x3 = int(x3)
        self.x4 = int(x4)
        self.y1 = int(y1)
        self.y2 = int(y2)
        self.y3 = int(y3)
        self.y4 = int(y4)
        # Здесь можно наверно было использовать метод и он бы брал данные самой точки...
        self._ab = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self._bc = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self._cd = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        self._da = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        self._ac = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        self._bd = math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
        self._apexA = [x1, y1]
        self._apexB = [x2, y2]
        self._apexC = [x3, y3]
        self._apexD = [x4, y4]

    def sides_trapezoid(self):
        list_sides = [self._ab, self._bc, self._cd, self._da, self._ac, self._bd]
        for i in range(len(list_sides) - 1):
            for j in range(len(list_sides) - i - 1):
                if list_sides[j] > list_sides[j + 1]:
                    list_sides[j], list_sides[j + 1] = list_sides[j + 1], list_sides[j]
        return list_sides[0], list_sides[1], list_sides[2], list_sides[3]

    def trapezoid_typing(self):
        list_sides = [self._ab, self._bc, self._cd, self._da, self._ac, self._bd]
        if len(set(list_sides)) == 4:
            return True
        else:
            return False
    def trapezoid_area(self):
        # здесь формала трапеции
        pass
    def trapezoid_perimeter(self):
        perimetr_tmp = list(self.sides_trapezoid())
        return sum(perimetr_tmp)


trapezoid_1 = Trapezoid(1, 8, 3, 5, -6, 0, 5, 10)
print(trapezoid_1.sides_trapezoid())
print(trapezoid_1.trapezoid_typing())
print(trapezoid_1.trapezoid_perimeter())