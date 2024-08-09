# Домашняя работа по уроку "Специальные методы классов"

# Цель: понять как работают базовые магические методы на практике.

# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

# Необходимо дополнить класс House следующими специальными методами:
# 1. __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# 2. __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

# Пример результата выполнения программы:

# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

# __str__
# print(h1)
# print(h2)

# __len__
# print(len(h1))
# print(len(h2))

# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor + 1):          # а по заданию надо поставить вместо 0 (или убрать) => 1
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
                continue
            if 0 == new_floor:
                print(f'Это подвал или парковка на нижнем этаже: {new_floor}')
                continue
            else:
                print(f'Такого этажа не существует: {new_floor}')
                break

# дополнено методами:
    def __len__(self):                                                                  # 1
        return self.number_of_floors

    def __str__(self):                                                                  # 2
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
print("*****************************")
h3 = House('ЖК Хвойная роща', 35)
# __str__
print(h3)
# __len__
print(len(h3))