# Конвертация в список
greeting = 'Hello from Python'
greeting_letters = list(greeting)
print(greeting_letters)


my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)
# Наборы и кортежи тоже можно перевести в list


# Арифметические операции в list
# Есть встроенные функции min max sum

ratings = [2.5, 5.0, 4.3, 3.7]
print(sum(ratings) / len(ratings))

# Объединение списков
my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)


# Нарезка списков
ratings2 = [2.5, 5.0, 4.3, 3.7, 4.5]

first_two_ratings = ratings2[:2]
print(first_two_ratings)

a = 1
middle_ratings = ratings2[a:-1]
print(middle_ratings)

last_two_ratings = ratings2[-2:]
print(last_two_ratings)



# Копирование списка
my_cars = ['BMW', 'Mercedes']
copied_cars = my_cars
copied_cars.append('Audi')

# Копирование по ссылке
# смысл в том что обе переменные ссылаются на 1 объект
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars))

# Копирование в НОВЫЙ список (копирование slice)
copied_cars2 = my_cars[:]
copied_cars2.append('Suzuki')
print(copied_cars2)
print(my_cars)
print(id(my_cars) == id(copied_cars2))

# Можно сделать то же самое с помощью метода copy
copied_cars3 = copied_cars2.copy()
copied_cars3.append('Honda')
print(copied_cars3)
print(copied_cars2)


# 3 вариант copied cars4 = list(copied_cars3)
# Т.е. с помощью метода list
# принты лень писать


