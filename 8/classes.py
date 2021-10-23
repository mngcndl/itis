class Square:
    rect_type = "Square"

    def __init__(self, a):
        self.a = a

    def calculate_square(self):
        return self.a**2


my_rect = Square(4)
another_rect = Square(4)
one_more_rect = my_rect
print(one_more_rect.a)
my_rect.a = 15
one_more_rect.a = 50
one_more_rect = Square(3)
Square.rect_type = "Something wrong"
rects = [my_rect, another_rect, one_more_rect]
for rect in rects:
    print(rect.a, rect.rect_type, rect.calculate_square())

print(my_rect.a, another_rect.a, one_more_rect.a)

a = 15
b = a
a = 10
print(b)

# Создать класс Тамагочи
# У него есть имя, сытость и здоровье
# Его можно кормить
# И проверять состояние сытости и состояние здоровья
# Со временем сытость убавляется,
# когда сытость будет == 0 тогда будет убавляться здоровье
# Посмотреть как работать с системным временем!
# Каждую секунду убавляется единица сытости еслти есть, или же здоровье
