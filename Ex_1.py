# Задание 1 и Задание 2. Вариант 8.
class Shape:
    def __init__(self, identifier):
        self.identifier = identifier

    def move(self, new_position):
        raise NotImplementedError("Subclasses must implement abstract method")

    def is_include(self, point):
        raise NotImplementedError("Subclasses must implement abstract method")


class Triangle(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier)
        self.vertices = vertices

    def move(self, new_position):
        if len(new_position) != 2:
            raise ValueError("Invalid position. It should be a tuple of length 2.")
        self.vertices = [(x + new_position[0], y + new_position[1]) for x, y in self.vertices]

    def is_include(self, point):
        # Проверяем, находится ли точка внутри треугольника
        x, y = point
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]

        # Используем формулу для определения принадлежности точки треугольнику
        A = 1 / 2 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3)
        s = 1 / A * (y1 * x3 - x1 * y3 + (y3 - y1) * x + (x1 - x3) * y)
        t = 1 / A * (x1 * y2 - y1 * x2 + (y1 - y2) * x + (x2 - x1) * y)

        return 0 <= s <= 1 and 0 <= t <= 1 and s + t <= 1


class Tetragon(Shape):
    def __init__(self, identifier, vertices):
        super().__init__(identifier)
        self.vertices = vertices

    def move(self, new_position):
        if len(new_position) != 2:
            raise ValueError("Invalid position. It should be a tuple of length 2.")
        self.vertices = [(x + new_position[0], y + new_position[1]) for x, y in self.vertices]

    def is_include(self, point):
        # Проверяем, находится ли точка внутри четырехугольника
        x, y = point
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        x4, y4 = self.vertices[3]

        # Проверяем, является ли точка внутри четырехугольника
        a = 1 / 2 * (-y1 * x2 + x1 * y2 + x2 * y - y2 * x)
        b = 1 / 2 * (y3 * x4 - x3 * y4 + x3 * y - y3 * x)
        c = 1 / 2 * (-y4 * x1 + x4 * y1 + x4 * y - y4 * x)

        return a >= 0 and b >= 0 and c >= 0


# Пример использования классов
triangle = Triangle("T1", [(0, 0), (1, 0), (0, 1)])
tetragon = Tetragon("T2", [(0, 0), (1, 0), (1, 1), (0, 1)])

try:
    triangle.move((2, 2))
    tetragon.move((1, 1))

    print(triangle.vertices)
    print(tetragon.vertices)

    point = (2, 2)
    print(triangle.is_include(point))
    print(tetragon.is_include(point))

except ValueError as e:
    print(f"Error: {e}")
except NotImplementedError as e:
    print(f"Error: {e}")
