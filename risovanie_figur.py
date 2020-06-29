# пример рисования фигур с полиморфизмом и без него
# Не выполнять
# рисование без полиморфизма стр 120
# shapes = [tr1, sq1, cr1]
# # shapes = [tr1, sq1, cr1]
# for a_shape in shapes:
#     if type(a_shape) == "Треугольник":
#         a_shape.draw_triangle()
#     if type(a_shape) == "Квадрат":
#         a_shape.draw_square()
#     if type(a_shape) == "Круг":
#         a_shape.draw_circle()

# рисование с полиморфизммом
# shapes = [tr1, sw1, cr1]
# for a_shape in shapes:
#     a_shape.draw()

# class Shape():
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#     def print_size(self):
#         print("""{} на {} """.format(self.width, self.len))
# my_shape = Shape(20, 25)
# my_shape.print_size()

class Rectangle():
    recs = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,
        self.len))
    def print_size(self):
        print("""{} на {}
            """.format(self.width,
            self.len))
r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
print(Rectangle.recs)